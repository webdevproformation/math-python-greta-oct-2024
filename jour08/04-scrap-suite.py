from bs4 import BeautifulSoup


page = requests.get("https://webdevpro.net/")

page.encoding = page.apparent_encoding
encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None

soup = BeautifulSoup(page.content , features="html.parser", from_encoding=encoding)
# print(soup)

elements = soup.findAll("div" , {"class" : "single-except"})

result = []
for i in elements:
    result.append(i.text)

# print(result)

# File path for the CSV file
csv_file_path = 'example.csv'

# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)
    # Write data to the CSV file
    writer.writerow(result)