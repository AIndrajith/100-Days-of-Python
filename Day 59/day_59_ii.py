# Parsing Markdown Syntax

import markdown

def convert_markdown_to_html(markdown_text):
    html_content = markdown.markdown(markdown_text)
    return html_content

markdown_text = "#Hello world\n This is a **bold** statement."
html_content = convert_markdown_to_html(markdown_text)
print(html_content)