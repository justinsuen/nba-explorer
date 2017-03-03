from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.justinsuen.com")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
