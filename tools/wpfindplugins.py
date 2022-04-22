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

        plugins = re.findall("wp-content/plugins/.*?/.*?\'", str(response))
        plugin_list = []
        for plugin in plugins:
            parsed_string = plugin[19:]
            version = parsed_string.split("?")
            parsed_plugin = parsed_string.split("/")
            full_plugin = (f"{parsed_plugin[0]} {version[1][:-2]}")
            plugin_list.append(full_plugin)
        return set(plugin_list)


fp = FindPlugins('https://www.cybertutorials.org/2022/python-wpnuker-a-collection-of-wordpress-pentesting-tools/')
print(fp.get_plugins())