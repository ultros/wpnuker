import re
import mechanize
from selenium import webdriver
import requests

class FindPlugins:
    def __init__(self, url):
        self.url = url
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.useragent = [
            ('User-agent', 'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')
        ]
        self.br.addheaders = self.useragent

    def get_plugins(self):
        # response = requests.get(self.url)
        # print(response.text)
        # driver = webdriver.Chrome(executable_path="./chromedriver")
        # driver.get(self.url)

        self.br.open(self.url)
        response = self.br.response().read()

        plugins = re.findall("plugins/.*?/", str(response))
        # need to parse version number
        dupe = ""
        for plugin in plugins:
            if plugin == dupe:
                pass
            else:
                print(plugin)
            dupe = plugin

fp = FindPlugins('https://www.cybertutorials.org/2022/python-wpnuker-a-collection-of-wordpress-pentesting-tools/')
fp.get_plugins()