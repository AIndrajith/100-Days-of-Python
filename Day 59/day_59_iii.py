# Generating HTML Content

import markdown

def convert_markdown_to_html(markdown_text):
    html_content = markdown.markdown(markdown_text)
    return html_content

def read_markdown_file(file_path):
    with open(file_path, "r") as file: 
        return file.read()
    
markdown_text = read_markdown_file("day_59_i.md")
html_content = convert_markdown_to_html(markdown_text)

def write_html_file(html_content, output_path):
    with open(output_path, "w") as file:
        file.write(html_content)

write_html_file(html_content, "example.html")