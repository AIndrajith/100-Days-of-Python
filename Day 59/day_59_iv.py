import markdown

def wrap_in_html_template(content):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Markdown to HTML</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 20px;
                }}
                h1, h2, h3 {{
                    color: #333;
                }}
                a {{
                    color: #1a73e8;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            {content}
        </body>
    </html>
    """
    return html_template

def convert_markdown_to_html(markdown_text):
    html_content = markdown.markdown(markdown_text)
    return html_content

def read_markdown_file(file_path):
    with open(file_path, "r") as file: 
        return file.read()
    
markdown_text = read_markdown_file("day_59_i.md")
html_content = convert_markdown_to_html(markdown_text)
html_with_template = wrap_in_html_template(html_content)

def write_html_file(html_content, output_path):
    with open(output_path, "w") as file:
        file.write(html_content)

write_html_file(html_content, "example.html")