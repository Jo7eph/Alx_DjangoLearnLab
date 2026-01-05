import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def check_readme():
    readme_path = os.path.join(BASE_DIR, "README.md")
    if not os.path.exists(readme_path):
        print("❌ README.md is missing!")
    elif os.path.getsize(readme_path) == 0:
        print("❌ README.md is empty!")
    else:
        print("✅ README.md exists and is not empty.")

def check_manage_py():
    manage_path = os.path.join(BASE_DIR, "manage.py")
    if not os.path.exists(manage_path):
        print("❌ manage.py is missing!")
    else:
        print("✅ manage.py exists.")

def check_settings():
    settings_path = os.path.join(BASE_DIR, "LibraryProject", "settings.py")
    if not os.path.exists(settings_path):
        print("❌ settings.py is missing!")
        return None
    else:
        print("✅ settings.py exists.")
        return settings_path

def check_settings_content(settings_path):
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    checks = {
    "INSTALLED_APPS": "'django.contrib.admin'" in content,
    "MIDDLEWARE": "'django.contrib.sessions.middleware.SessionMiddleware'" in content,
    "DATABASES": "'ENGINE': 'django.db.backends.sqlite3'" in content,
    "TEMPLATES": "'django.template.backends.django.DjangoTemplates'" in content,
}
