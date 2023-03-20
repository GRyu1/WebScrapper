from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  #사이트 & 검색어
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  #search_term = "python"
  #사이트 형식화
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request Website.")

  else:
    results=[]
    soup = BeautifulSoup(response.text, "html.parser") #html >> python entity
    jobs=soup.find_all('section', class_="jobs") #jobs=list
    for job_section in jobs: #job post 가져오기
      job_posts=job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:#job post 중 필요 요소 빼오기
        anchors=post.find_all('a')
        anchor = anchors[1]
        link=anchor['href']
        company, kind, region =anchor.find_all('span',class_="company")
        title=anchor.find('span',class_="title")
        job_data={
          'link':link,
          'company':company.string.replace(","," "),
          'location':region.string.replace(","," "),
          'title':title.string.replace(","," "),
          'kind':kind.string.replace(","," ")
        }
        results.append(job_data)#결과값에 저장
    return results