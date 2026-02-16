# 1) Parse HTML – Extract title and h1
#
# from bs4 import BeautifulSoup
#
# html = '''
# <html>
# <head><title>My Page</title></head>
# <body>
# <h1>Welcome</h1>
# <p>This is a paragraph.</p>
# </body>
# </html>
# '''
# 2) Extract All Paragraphs
# 3) Extract All Links and Count
# 4) Extract Attributes
# 5) Extract First h2
# 6) Extract Bold Text
# 7) Extract All href Values
# 8) Get All Text Without Tags
# 9) Extract Title from Website
# 10) Extract All Headings
# 11) Extract Table Data
# 12) Extract Images
#

import requests
from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>My Page</title>
</head>
<body>
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<p>This is paragraph 1</p>
<p>This is paragraph 2</p>
<a href="https://google.com" id="googleLink">Google</a>
<a href="https://youtube.com">YouTube</a>
<b>This is bold text</b>
<img src="image1.jpg" alt="Image1">
<img src="image2.png" alt="Image2">
<table border="1">
<tr>
<td>John</td>
<td>25</td>
</tr>
<tr>
<td>Alice</td>
<td>30</td>
</tr>
</table>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# parse html EXtract title and h1
print("1. Extract title and h1")
print("Title: ", soup.title.text)
print("H1: ", soup.h1.text)
# extract all paragraphs
print("2. Extract all paragraphs")
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)
# Extract all links and count
print("3. Extract All Links and Count")
links = soup.find_all("a")
print("Total links: ", len(links))
for link in links:
    print(link.text, link.get("href"))
# Extract Attributes
print("4. Extract Attributes")
link = soup.find("a")
print("href:", link.get("href"))
print("id:", link.get("id"))
print("All attributes:", link.attrs)
# Extract First h2
print("5. Extract First h2")
h2 = soup.find("h2")
print(h2.text)
# Extract Bold Text
print("6. Extract Bold Text")
bold = soup.find("b")
print(bold.text)
# Extract All href Values
print("7. Extract All href values")
for link in soup.find_all("a"):
    print(link.get("href"))
# Get All Text Without Tags
print("8. Get All Text Without Tags")
print(soup.get_text())
# Extract Title from Website
print("9. Extract Title from Website")
url = "https://example.com"
response = requests.get(url, verify=False)
website_soup = BeautifulSoup(response.text, "html.parser")
print("Website Title:", website_soup.title.text)
# Extract All Headings
print("10. Extract All Headings")
for heading in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
    print(heading.text)
# Extract Table Data
print("11. Extract Table Data")
rows = soup.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    for col in cols:
        print(col.text)
# Extract Images
print("\n12) Extract Images")
images = soup.find_all("img")
for img in images:
    print(img.get("src"))