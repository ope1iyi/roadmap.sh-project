import requests
from bs4 import BeautifulSoup
import csv

url = 'https://realpython.github.io/fake-jobs/'

res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, features='html.parser')
job_listing = []

for job in soup.find_all('div', class_='card-content'): # Each job listing is stored in the div tag with class 'card-content'
    location = job.find('p', class_='location').text.strip()
    job_title = job.find('h2', class_='title is-5').text.strip()
    company_name = job.find('h3', class_='subtitle is-6 company').text.strip()
    link = job.find('a')['href']

    job_listing.append({'Title':job_title,
                        'Company': company_name,
                        'Location': location,
                        'Link': link})

with open('jobs.csv', 'w', newline="") as f:
    writer = csv.DictWriter(f, fieldnames=['Title', 'Company', 'Location', 'Link'])
    writer.writeheader() #Write the fieldnames above as headers
    writer.writerows(job_listing) #Write each row in the job_listing into the csv file

