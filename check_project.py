import os
import sys

project_dir = os.path.dirname(os.path.abspath(__file__))

def check_readme():
    readme_path = os.path.join(project_dir, "README.md")
    if os.path.isfile(readme_path):
        if os.path.getsize(readme_path) > 0:
            print("[OK] README.md exists and is not empty.")
        else:
            print("[MISSING] README.md is empty.")
    else:
        print("[MISSING] README.md does not exist.")

def check_manage_py():
    manage_path = os.path.join(project_dir, "manage.py")
    if os.path.isfile(manage_path):
        print("[OK] manage.py exists.")
    else:
        print("[MISSING] manage.py does not exist.")

def check_settings():
    settings_path = os.path.join(project_dir, "LibraryProject", "settings.py")
    if os.path.isfile(settings_path):
        print("[OK] settings.py exists.")
        check_settings_content(settings_path)
    else:
        print("[MISSING] settings.py does not exist.")

def check_settings_content(settings_path):
    required_keys = ["INSTALLED_APPS", "MIDDLEWARE", "DATABASES"]
    with open(settings_path, "r", encoding="utf-8") as f:
        content = f.read()
        for key in required_keys:
            if key in content:
                print(f"[OK] '{key}' found in settings.py.")
            else:
                print(f"[MISSING] '{key}' not found in settings.py.")

def main():
    print("Checking LibraryProject...")
    check_readme()
    check_manage_py()
    check_settings()
    print("Check complete.")

if __name__ == "__main__":
    main()
