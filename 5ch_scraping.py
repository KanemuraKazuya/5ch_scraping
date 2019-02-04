from pyquery import PyQuery as pq
from pprint import pprint
import sys


class scrape():
  def __init__(self, url):
    self.url = url

  def Scrape(self):
    self.q = pq(url = self.url)

    self.messages = self.q('div.message span')

  def get_all(self):
    all_res = []
    for line in self.messages:
      all_res.append(self.messages(line).text())
    return all_res

if __name__=='__main__':
  args = sys.argv

  if len(args) != 2:
    print("Please input url")
    print("ex: python3 5ch_scraping https://xxx.xxx")
  
  scrape_5ch = scrape(args[1])
  scrape_5ch.Scrape()


  all_res = scrape_5ch.get_all()
  pprint(all_res)
