# Extracting Target information

from bs4 import BeautifulSoup

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def extract_posts(soup):
    posts = []
    post_elements = soup.find_all("div", class_="post")
    for post in post_elements:
        username = post.find("h2", class_="username").text.strip()
        content = post.find("p", class_="content").text.strip()
        timestamp = post.find("span", class_="timestamp").text.strip()
        posts.append({"username":username, "content":content, "timestamp":timestamp})
    return posts

html_content = load_html("day_61_i_social_media.html")
soup = BeautifulSoup(html_content, "html.parser")
posts = extract_posts(soup)
for post in posts:
    print(f"User: {post['username']}")
    print(f"Post: {post['content']}")
    print(f"Time: {post['timestamp']}")
    print("-"*20)