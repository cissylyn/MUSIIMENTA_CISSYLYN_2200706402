# Libraries for web scraping
# Request, BeautifulSoup, lxml, scrapy, selenium
# API keys
# exercise : openweathermap.org

import requests
from bs4 import BeautifulSoup
import json
import csv

# Step 2 
url = "http://ryeko.org"
response = requests.get(url)
html_content = response.text

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 4: Find specific data
data = []
for item in soup.find_all("a"):
    title = item.text.strip()
    link = item.get("href")
    data.append({"title": title, "link": link})

# Step 5: Save data to the CSV file
csv_file = "scrapped_data.csv"
with open(csv_file, "w", newline="", encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    for item in data:
        writer.writerow(item)

# Step 6: Save the data to the JSON file
json_file = "scrapped_data.json"
with open(json_file, "w", encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Step 7: Print success message
print(f'Data has been saved successfully to {csv_file} and {json_file}')

# Further exercises: Scrape data from http://openweathermap.org

# exercise :scrape data from the Http://openweathermap.org