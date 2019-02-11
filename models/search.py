from bs4 import BeautifulSoup
import urllib.parse

class Search():
    
    def __init__(self, query):
        self.query = query
        self.url_encoded_query = urllib.parse.urlencode(query)
        self.results = self.performSearch()

    def performSearch(self):
        soup = BeautifulSoup('https://www.google.com/search?q=site%3Adivinityoriginalsin2.wiki.fextralife.com+{}'.format(url_encoded_query))
        count = 0
        for result in soup.findAll('div', attrs={'class': 'g'}):
            count += 1
        return count