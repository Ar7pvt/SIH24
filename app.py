from flask import Flask,render_template, request, redirect, url_for, flash,send_file
import os
from static import item
import os
import cv2
import tempfile
from YOLOv6 import YOLOv6

app=Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max size


model_path = "best_ckpt.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.35, iou_thres=0.5)


class_names =  [
    "Cashew-anthracnose",
    "Cashew-healthy",
    "Cashew-leaf-miner",
    "Cassava-bacterial-blight",
    "Cassava-brown-spot",
    "Cassava-healthy",
    "Maize-healthy",
    "Maize-leaf-beetle",
    "Maize-leaf-blight",
    "Tomato-healthy",
    "Tomato-leaf-curl",
    "Tomato-verticillium-wilt"
]

# plant_conditions = 



# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


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
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extension




@app.route('/landing', methods=['GET', 'POST'])
# @login_required
def upload_image():
    if request.method == 'POST':
        # file upload checking
        if 'image_file' not in request.files:
            return "No file uploaded "

        image_file = request.files['image_file']

        # For filename purpose
        if image_file.filename == '':
            return "No selected file are"

        # Saving the image in a folder
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            image_file.save(temp_filename)

        # Reading image
        img = cv2.imread(temp_filename)

        # Detect Objects
        boxes, scores, class_ids = yolov6_detector(img)

        # Mapping respective details accord to class
        class_details = {
            'Aloevera': [
        '<strong>1. Anti-inflammatory:</strong> Aloevera leaves contain compounds like bradykinase, which help reduce inflammation when applied topically. It is commonly used for soothing burns, wounds, and skin irritations.',
        '<strong>2.Antimicrobial:</strong> The gel within the leaves has natural antimicrobial properties, making it effective against bacteria, viruses, and fungi.',
        '<strong>3.Moisturizing:</strong> Aloevera leaves are rich in water content and mucilage, making them an excellent natural moisturizer for the skin.',
        ],
            'Amla': [
        '<strong>1. Rich in Vitamin C:</strong> Amla leaves are a great source of vitamin C, which boosts the immune system and helps fight off various infections.',
        '<strong>2. Antioxidant Properties:</strong> The leaves of Amla are packed with antioxidants that protect cells from damage caused by free radicals and help in preventing chronic diseases.',
        '<strong>3. Digestive Aid:</strong> Amla leaves can aid in digestion, as they stimulate the secretion of gastric juices.',
        
        ],
            'Bamboo': [
        '<strong>1. Antibacterial:</strong> Extracts from bamboo leaves have been found to have antibacterial properties, making them useful in traditional medicine for treating infections.',
        '<strong>2. Rich in Silica:</strong> Bamboo leaves are a good source of silica, which is essential for healthy skin, hair, and nails.',
        '<strong>3. Anti-inflammatory:</strong> Compounds in bamboo leaves can have anti-inflammatory effects, potentially aiding in conditions involving inflammation.',
        
        ],
           
            'Betel': [
        '<strong>1. Antimicrobial:</strong> Betel leaves have natural antimicrobial properties and are used traditionally for oral hygiene and treating minor infections.',
        '<strong>2. Digestive Aid:</strong> Chewing betel leaves is believed to aid in digestion and alleviate gastrointestinal issues.',
        '<strong>3. Anti-inflammatory:</strong> The leaves contain compounds that can help reduce inflammation when applied topically.',
        
        ],
            'Curry': [
        '<strong>1. Rich in Antioxidants:</strong> Curry leaves are packed with antioxidants that help in neutralizing harmful free radicals in the body.',
        '<strong>2. Improves Digestion:</strong> The leaves of the curry plant can help improve digestion and treat conditions like indigestion and diarrhea.',
        '<strong>3. Hair Health:</strong> Curry leaves are known for promoting hair health and are often used in hair care remedies.',
        
        ],
            'Amruthaballi': [
        '<strong>1.Immunomodulatory:</strong> Amruthaballi leaves possess immunomodulatory properties, which means they help regulate and strengthen the immune system.',
        '<strong>2. Anti-inflammatory:</strong> The leaves have anti-inflammatory compounds that can help reduce inflammation in the body.',
        '<strong>3. Antioxidant:</strong> Giloy leaves are rich in antioxidants that protect cells from damage and support overall health.',
        
        ],
            'Arali': [
        '<strong>1. Antipyretic:</strong> Arali leaves have been traditionally used as an antipyretic agent, helping to reduce fever.',
        '<strong>2. Analgesic:</strong> They also have analgesic properties, potentially providing pain relief.',
        '<strong>3. Antimicrobial:</strong> Arali leaves may have natural antimicrobial properties useful in treating infections.',
        
        ],
            'Ashoka': [
        '<strong>1. Uterine Tonic:</strong> Ashoka leaves are often used as a uterine tonic, supporting women reproductive health.',
        '<strong>2. Antioxidant:</strong> They contain antioxidants that help protect cells from oxidative damage.',
        '<strong>3. Anti-inflammatory:</strong> Ashoka leaves may possess anti-inflammatory properties, potentially aiding in conditions involving inflammation.',
        
        ],
            'Astma_weed': [
        '<strong>1. Expectorant:</strong> Asthma Weed leaves are known for their expectorant properties, helping to clear mucus from the respiratory system.',
        '<strong>2. Antimicrobial:</strong> They may have natural antimicrobial properties, which can be beneficial in treating infections.',
        '<strong>3. Anti-inflammatory:</strong> Asthma Weed leaves could have anti-inflammatory effects when applied topically.',
        
        ],
            'Badipala': [
        '<strong>1. Digestive Aid:</strong> Badipala leaves are traditionally used to alleviate digestive issues and promote healthy digestion.',
        '<strong>2. Antimicrobial:</strong> They may possess natural antimicrobial properties, aiding in fighting off infections.',
        
        ],
            'Ballon_Vine':[
        '<strong>Anti-inflammatory:</strong> Balloon Vine leaves may have antiinflammatory properties, potentially useful in treating inflammatory conditions.',
        '<strong>Analgesic:</strong> They may provide pain relief when applied topically.',
        '<strong>Antimicrobial:</strong> Balloon Vine leaves could have natural antimicrobial properties useful in treating infections.',

         
        ],
            'Beans': [
        '<strong>1. Rich in Nutrients:</strong> Bean leaves are packed with essential nutrients like vitamins, minerals, and fiber, contributing to overall health.'
        '<strong>2. Antioxidant Properties:</strong> They contain antioxidants that help protect cells from damage caused by free radicals.'
        '<strong>3. Digestive Health:</strong> Bean leaves can aid in digestion due to their fiber content.'
        
        ],
            'Bharmi': [
        '<strong>1. Anti-inflammatory:</strong> Bharmi leaves may possess anti-inflammatory properties, potentially useful in managing inflammatory conditions.',
        '<strong>2. Analgesic:</strong> They may provide pain relief when applied topically.',
        '<strong>3. Antioxidant:</strong> Bharmi leaves could contain antioxidants that help protect cells.',
        
        ],
            'Bringarja': [
        '<strong>1. Hair Health:</strong> Bhringaraja leaves are known for their benefits to hair health, promoting growth and preventing hair loss.',
        '<strong>2. Liver Support:</strong> They are traditionally used to support liver function and detoxification.',
        '<strong>3. Antimicrobial:</strong> Bhringaraja leaves may have natural antimicrobial properties, aiding in treating infections.',
        
        ],
            'camphor': [
        '<strong>1. Topical Analgesic:</strong> Camphor leaves are a source of natural camphor oil which, when applied topically, can provide pain relief and soothe sore muscles.',
        '<strong>2. Respiratory Benefits:</strong> Inhaling the aroma of camphor leaves can help in relieving congestion and is commonly used in decongestant ointments.',
        '<strong>3. Insect Repellent:</strong> Camphor leaves and oil are known to repel insects, making them useful for insect bites and as a natural insecticide.',
        
        ],
           
        }

        # collecting label
        detected_class = class_names[class_ids[0]]

        # mapping deails wrt label
        details = class_details.get(detected_class, ['No details available'])

        details = '<br>'.join(details)

        # Drawing box
        combined_img = yolov6_detector.draw_detections(img)

        # Saving the image + box 
        result_filename = os.path.join("static", "detected_objects.jpg")
        cv2.imwrite(result_filename, combined_img)

        # Remove the temporary file
        os.remove(temp_filename)

        return render_template('Results.html', detected_class=detected_class, details=details,navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)

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