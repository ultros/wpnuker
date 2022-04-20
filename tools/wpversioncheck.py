import mechanize
import re


class GetVersion:
    def __init__(self, url):
        self.url = url
        self.br = mechanize.Browser()

    def locate_version(self):
        self.br.open(self.url)
        response = self.br.response().read()
        results = re.findall(f'content="WordPress.*?"', str(response))
        for link in results:
            return link[9:-1]

