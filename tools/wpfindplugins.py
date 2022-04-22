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
        self.br.open(self.url)
        response = self.br.response().read()

        plugins = re.findall("wp-content/plugins/.*?/.*?\'", str(response))
        plugin_list = []

        for plugin in plugins:
            parsed_string = plugin[19:]
            if parsed_string[:14] == "fusion-builder":
                plugin_list.append(parsed_string[:14])
                parsed_string = ""
            else:
                pass
            version = parsed_string.split("?")
            parsed_plugin = parsed_string.split("/")
            try:
                full_plugin = (f"{parsed_plugin[0]} {version[1][:-2]}")
            except Exception as e:
                pass
            plugin_list.append(full_plugin)
        return set(plugin_list)
