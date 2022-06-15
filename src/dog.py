import json
import requests
import sys
sys.path.insert(0, 'src/vendor')
from parsel import Selector

def main():
  r = requests.get('https://stackoverflow.com/feeds/tag?tagnames=python&sort=newest')
  selector = Selector(text=r.text, type='xml')
  selector.remove_namespaces()
  entries = selector.xpath('//entry')

  dict = {
    'title': entries[0].xpath('title/text()').get(),
    'link': entries[0].xpath('link').attrib['href'],
      'id': entries[0].xpath('id').get()
  }

  print(json.dumps(dict, indent=2))

if __name__ == '__main__':
  main()