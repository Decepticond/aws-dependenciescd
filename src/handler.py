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
  list_of_entries = [] 

  for entry in entries:
    dict = {
      'title': entry.xpath('title/text()').get(),
      'link': entry.xpath('link').attrib['href'],
      'id': entry.xpath('id').get()
    }
    list_of_entries.append(dict)

    print(json.dumps(list_of_entries[0], indent=2))


if __name__ == '__main__':
  main()