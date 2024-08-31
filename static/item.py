import os

# Define the path to your templates folder
template_folder = 'templates'

# Dictionary with URLs pointing to specific HTML files in the templates folder
navBarItems = {
   "Home": {"url": os.path.join(template_folder, "Home.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "About": {"url": os.path.join(template_folder, "About.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Contact": {"url": os.path.join(template_folder, "Contact.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
   "Team": {"url": os.path.join(template_folder, "Team.html").removeprefix(template_folder + os.path.sep).lower().removesuffix(".html")},
}
# print(navBarItems["Home"])
footerOrganizationItems = {
   "Kheti.Ai" :{"url" : "#",},
   "Donate" :{"url" : "#",},
   "Team" :{"url" : "#",},
}
footerResourcesItems = {
    "FAQ" :{"url" : "#",},
   "Open data" :{"url" : "#",},
   "API" :{"url" : "#",},
   "Stats" :{"url" : "#",},
   "Translations" :{"url" : "#",},
}
footerLegalItems = {
    "About" :{"url" : "#",},
   "Terms of use" :{"url" : "#",},
   "Legal terms" :{"url" : "#",},
}
footerContactUsItems = {
    "Contact" :{"url" : "#",},
   "System health" :{"url" : "#",},
}


# About Team
team = [
        {
            "name": "Mary Brown",
            "title": "creative leader",
            "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "https://via.placeholder.com/300x300",
            "social_links": {
                "facebook": "https://www.facebook.com/",
                "twitter": "#",
                "instagram": "#",
                "linkedin": "#",
                "github": "#",
                "email": "mailto:ashutoshrazz100@gmail.com.com",
            }
        },
        {
            "name": "Ann Richmond",
            "title": "creative leader",
            "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "https://via.placeholder.com/300x300",
            "social_links": {
                "facebook": "#",
                "twitter": "#",
                "instagram": "#",
                "linkedin": "#",
                "github": "#",
                "email": "#",
            }
        },
        {
            "name": "Chung Schlueter",
            "title": "strategy director",
            "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "https://via.placeholder.com/300x300",
            "social_links": {
                "facebook": "#",
                "twitter": "#",
                "instagram": "#",
                "linkedin": "#",
                "github": "#",
                "email": "#",
            }
        },
        {
            "name": "Kelly Savala",
            "title": "lead developer",
            "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "https://via.placeholder.com/300x300",
            "social_links": {
                "facebook": "#",
                "twitter": "#",
                "instagram": "#",
                "linkedin": "#",
                "github": "#",
                "email": "#",
            }
        },
        {
            "name": "David Bell",
            "title": "head of product management",
            "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "https://via.placeholder.com/300x300",
            "social_links": {
                "facebook": "#",
                "twitter": "#",
                "instagram": "#",
                "linkedin": "#",
                "github": "#",
                "email": "#",
            }
        },
        {
            "name": "Lindsay Watson",
            "title": "manager",
            "description": "Glavi amet rintis libero molestie ante ut fringilla purus eros quis glavirid from dolor amet iquam lorem bibendum.",
            "image_url": "https://via.placeholder.com/300x300",
            "social_links": {
                "facebook": "#",
                "twitter": "#",
                "instagram": "#",
                "linkedin": "#",
                "github": "#",
                "email": "#",
            }
        }
    ]