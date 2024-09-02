from flask import Flask,render_template, request, redirect, url_for, flash,send_file
import os
from static import item
import os
import cv2
import tempfile
from YOLOv6 import YOLOv6
from data import class_names,class_details,plant_health_detection

app=Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max size


model_path = "best_ckpt.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.35, iou_thres=0.5)



# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def home1():
    return render_template('Home.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)

@app.route('/home')
def home():
    return render_template('Home.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)
@app.route('/about')
def about():
    return render_template('About.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)
@app.route('/business')
def business():
    return render_template('Business.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)

@app.route('/contact')
def contact():
    return render_template('Contact.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)
@app.route('/team')
def team():
    return render_template('Team.html',team = item.team,navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)


@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files[]' not in request.files:
        flash('No files selected.')
        return redirect(request.url)
    
    files = request.files.getlist('files[]')
    uploaded_file_paths = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # type: ignore
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            uploaded_file_paths.append(file_path)
    
    flash(f'Successfully uploaded {len(uploaded_file_paths)} files.')
    return redirect(url_for('index'))

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'wmv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions





@app.route('/landing', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image_file' not in request.files:
            return "No file uploaded"

        image_file = request.files['image_file']

        # If the user does not select a file, the browser also submits an empty part without filename
        if image_file.filename == '':
            return "No selected file"

        # Save the image temporarily
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            image_file.save(temp_filename)

        # Read the image
        img = cv2.imread(temp_filename)

        # Object detection
        boxes, scores, class_ids = yolov6_detector(img)

        # Handling detection results
        if len(class_ids) > 0:
            # Get the detected class name using the first class ID
            # detected_class = class_names.get(class_ids[0], "Unknown Class")
            detected_class = class_names[class_ids[0]]

            # Fetch corresponding details for the detected class
            if detected_class in class_details:
                precautions = "<br>".join(class_details[detected_class]["Precautions"])
                avoidance = "<br>".join(class_details[detected_class]["Avoidance"])
                cure = "<br>".join(class_details[detected_class]["Cure"])
                details = (
                        f"<strong>Precautions:</strong><br>{precautions}<br>"
                        f"<strong>Avoidance:</strong><br>{avoidance}<br>"
                        f"<strong>Cure:</strong><br>{cure}"
                    )
            
            elif detected_class in plant_health_detection:
                summary_report = plant_health_detection[detected_class]["Summary Report"]
                health_status = plant_health_detection[detected_class]["Health Status Indicator"]
                visual_confirmation = plant_health_detection[detected_class]["Visual Confirmation"]["Description"]
                recommendations = plant_health_detection[detected_class]["Recommendation"]

                # Format details for display
                precautions = "<br>".join([f"{key}: {value}" for key, value in recommendations.items()])
                details = (
                    f"<strong>Summary Report:</strong><br>Plant Type: {summary_report['Plant Type']}<br>"
                    f"Detection Date: {summary_report['Detection Date']}<br>"
                    f"Leaf Health: {summary_report['Leaf Health']}<br>"
                    f"Explanation: {summary_report['Explanation']}<br><br>"
                    f"<strong>Health Status:</strong> {health_status}<br><br>"
                    f"<strong>Visual Confirmation:</strong><br>{visual_confirmation}<br><br>"
                    f"<strong>Recommendations:</strong><br>{precautions}"
                )

            else:
                details = "No details available for the detected class."

            # Draw bounding boxes on the image
            combined_img = yolov6_detector.draw_detections(img)

            # Save the image with detections to the static folder
            result_filename = os.path.join("static", "detected_objects.jpg")
            cv2.imwrite(result_filename, combined_img)

            # Remove the temporary file
            os.remove(temp_filename)

            # Render the results page
            return render_template('Results.html', detected_class=detected_class, details=details,navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)
        else:
            # No objects detected
            os.remove(temp_filename)
            return "No objects detected in the image."

    # If GET request, render the landing page
    return render_template('landing.html')


@app.route('/get_image')
def get_image():
    image_path = "static/detected_objects.jpg"

 
    img = cv2.imread(image_path)

    # Define the new dimension
    new_width = int(request.args.get('width', 600)) 
    new_height = int(request.args.get('height', 500))  

    # Resize the image
    resized_img = cv2.resize(img, (new_width, new_height))

    # writing back the original image 
    cv2.imwrite(image_path, resized_img)
    return send_file("static/detected_objects.jpg")

if __name__=="__main__":
    app.run(debug=True)