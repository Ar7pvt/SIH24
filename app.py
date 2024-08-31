from flask import Flask,render_template, request, redirect, url_for, flash
import os
from static import item

app=Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB max size


# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/home')
def home():
    return render_template('Home.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)
@app.route('/about')
def about():
    return render_template('About.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)

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

if __name__=="__main__":
    app.run(debug=True)