import os
from lxml import html

def validate_html_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        html.fromstring(content)
                        print(f"✅ {file_path} is valid.")
                except Exception as e:
                    print(f"❌ {file_path} is invalid: {e}")

# Validate HTML files in the current directory
validate_html_files(".")
