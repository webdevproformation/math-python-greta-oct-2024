from bs4 import BeautifulSoup

page = """
<ul>
    <li>premier</li>
    <li>deuxieme</li>
</ul>
"""

soup = BeautifulSoup(page , features="html.parser")
elements = soup.findAll("li")

result = []
for i in elements:
    result.append(i.text)

print(result) # ['premier', 'deuxieme']

