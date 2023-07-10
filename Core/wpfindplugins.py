import re
import mechanize


class FindPlugins:
    def __init__(self, url) -> None:
        self.url = url
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.useragent = [
            ('User-agent', 'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')
        ]
        self.br.addheaders = self.useragent

    def get_plugins(self) -> set:
        plugin_list = []

        self.br.open(self.url)
        response = self.br.response().read()

        plugins = re.findall("wp-content/plugins/.*?/.*?\'", str(response))

        for plugin in plugins:
            parsed_string = plugin[19:]
            if parsed_string[:14] == "fusion-builder":
                plugin_list.append(parsed_string[:14])
            else:
                pass

            parsed_plugin = parsed_string.split("/")
            plugin_list.append(parsed_plugin[0])

        return set(plugin_list)  # remove duplicates
