import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bloggingwebsite.settings")

import django
django.setup()

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

def create_superuser(username="admin", password="123456", email="admin@localhost.com"):
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser created: {username}")
    else:
        print(f"Superuser already exists: {username}")

def insert_site(id=2, domain='127.0.0.1:8000', name='127.0.0.1:8000'):
    site = Site.objects.create(id=id, domain=domain, name=name)
    site.save()
    print(f"Site created: {site}")

def insert_socialapp(provider='google', 
                     name='Blogging Webiste', 
                     client_id='526192306673-mo1raipbh35emfrrunj8ttf6m5pj7jeu.apps.googleusercontent.com', 
                     secret='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', 
                     site_id=1):
    site = Site.objects.get(id=site_id)
    socialapp = SocialApp.objects.create(provider=provider, name=name, client_id=client_id, secret=secret)
    socialapp.sites.add(site)
    socialapp.save()
    print(f"SocialApp created: {socialapp}")





create_superuser()
insert_site()
insert_socialapp()

