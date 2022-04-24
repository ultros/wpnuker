import mechanize
import re


class GetVersion:
    def __init__(self, url):
        self.url = url
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.useragent = [
            ('User-agent', 'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')
        ]
        self.br.addheaders = self.useragent

    def locate_version(self):
        self.br.open(self.url)
        response = self.br.response().read()
        results = re.search(f'content="WordPress.*?"', str(response))
        return results.group(0)[9:-1]
