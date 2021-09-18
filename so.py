import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  pages = soup.find("div", {"class":"pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return last_page

def extract_job(html):
    title = html.find("div",{"class":"-title"}).find("h2").find("a")["title"]
    company, location = html.find("div",{"class":"-company"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\n")
    print(company, location)
    return {'title': title}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs