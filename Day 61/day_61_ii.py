# Using Python to Parse HTML Files

from bs4 import BeautifulSoup

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

html_content = load_html("day_61_i_social_media.html")
soup = BeautifulSoup(html_content, "html.parser")