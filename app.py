from flask import Flask, render_template, url_for
from static import item

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index1')
def index1():
    return render_template('index1.html')

# item = ["Home","About","contact",]
@app.route('/index2')
def index2():
    return render_template('index2.html',items = item.navBarItems)
@app.route('/index3')
def index3():
    return render_template('index3.html',navbarItems = item.navBarItems,footerOrganizationItems = item.footerOrganizationItems,footerResourcesItems=item.footerResourcesItems,footerLegalItems=item.footerLegalItems,footerContactUsItems=item.footerContactUsItems)

if __name__=="__main__":
    app.run(debug=True)