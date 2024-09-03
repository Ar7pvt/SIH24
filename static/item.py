import os

# Define the path to your templates folder
template_folder = 'templates'
static_folder = "static"

# Dictionary with URLs pointing to specific HTML files in the templates folder
navBarItems = {
   "Home": {"url": os.path.join(template_folder, "Home.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "About": {"url": os.path.join(template_folder, "About.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Business": {"url": os.path.join(template_folder, "Business.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Contact": {"url": os.path.join(template_folder, "Contact.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Team": {"url": os.path.join(template_folder, "Team.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")}
}
# print(navBarItems["Home"])
footerOrganizationItems = {
   "Kheti.Ai" :{"url" : os.path.join(template_folder, "Home.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Donate" :{"url" : "#",},
   "Team" :{"url" : os.path.join(template_folder, "Team.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
}
footerResourcesItems = {
    "FAQ" :{"url" : "#",},
   "Open data" :{"url" : "#",},
   "API" :{"url" : "#",},
   "Stats" :{"url" : "#",},
   "Translations" :{"url" : "#",},
}
footerLegalItems = {
    "About" :{"url" : os.path.join(template_folder, "About.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Terms of use" :{"url" : "#",},
   "Legal terms" :{"url" : "#",},
}
footerContactUsItems = {
    "Contact" :{"url" :  os.path.join(template_folder, "Contact.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html") },
   "System health" :{"url" : "#",},
}


# About Team
team = [
        {
            "name": "Mohit Naman",
            # "title": "creative leader",
            # "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "Mohit-Naman.jpeg",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "https://x.com/?lang=en-in",
                "instagram": "https://www.instagram.com/accounts/login/",
                "linkedin": "https://www.linkedin.com/in/mohit21/",
                "github": "https://github.com/login",
                "email": "#",
            }
        },
        {
            "name": "Alok Raj",
            # "title": "creative leader",
            # "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "alok.jpeg",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "https://x.com/home?lang=en",
                "instagram": "https://www.instagram.com/accounts/login/",
                "linkedin": "https://www.linkedin.com/in/alok-raj-4a6947202/",
                "github": "https://github.com/Ar7pvt",
                "email": "mailto:alokrajgrd8@gmail.com.com",
            }
        },
        {
            "name": "Ashutosh Raj",
            # "title": "strategy director",
            # "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "ashutosh-raj.png",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "https://x.com/?lang=en-in",
                "instagram": "https://www.instagram.com/accounts/login/",
                "linkedin": "https://www.linkedin.com/in/ashutoshraj100/",
                "github": "https://github.com/ASHUTOSHRAZZ100",
                "email": "mailto:ashutoshrazz100@gmail.com.com",
            }
        },
        {
            "name": "Prateek Singh",
            # "title": "lead developer",
            # "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "prateek-singh.jpeg",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "https://x.com/?lang=en-in",
                "instagram": "https://www.instagram.com/accounts/login/",
                "linkedin": "https://www.linkedin.com/in/prateek-xe/",
                "github": "https://github.com/login",
                "email": "#",
            }
        },
        {
            "name": "Aprajita Kumari",
            # "title": "head of product management",
            # "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "Aprajita-Kumari.jpeg",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "https://x.com/?lang=en-in",
                "instagram": "https://www.instagram.com/accounts/login/",
                "linkedin": "https://www.linkedin.com/in/aprajita-kumari05/",
                "github": "https://github.com/login",
                "email": "#",
            }
        },
        {
            "name": "Dipanjan Sahoo",
            # "title": "manager",
            # "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "Dipanjan-Sahoo.jpeg",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "https://x.com/?lang=en-in",
                "instagram": "https://www.instagram.com/accounts/login/",
                "linkedin": "https://www.linkedin.com/in/dipanjan-sahoo/",
                "github": "https://github.com/login",
                "email": "#",
            }
        }
    ]