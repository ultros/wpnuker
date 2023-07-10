import re
import mechanize
from faker import Faker


class WPComment:
    def __init__(self, site_to_comment: str, site_to_advertise: str, site_anchor_text: str) -> None:
        self.fake = Faker()
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.useragent = [
            ('User-agent', 'Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')
        ]
        self.br.addheaders = self.useragent
        self.site_to_comment = site_to_comment
        self.site_to_advertise = site_to_advertise
        self.site_anchor_text = site_anchor_text

    def get_first_name(self) -> str:
        return self.fake.first_name()

    def get_last_name(self) -> str:
        return self.fake.last_name()

    def get_comment(self, hyperlink: str, anchor_text="") -> str:
        if hyperlink and anchor_text:
            return f'<a href="{hyperlink}">{anchor_text}</a> - {self.fake.text()}'
        else:
            return self.fake.text()

    def get_email(self) -> str:
        return self.fake.email()

    def post_comment(self) -> None:
        try:
            if self.site_to_comment[:4] != "http":
                self.br.open(f"http://{self.site_to_comment}", timeout=20)
            else:
                self.br.open(self.site_to_comment)
            self.br.select_form(nr=0)

            try:
                self.br.form['author'] = self.get_first_name()
            except Exception as e:
                pass
            try:
                self.br.form['email'] = self.get_email()
            except Exception as e:
                pass
            try:
                self.br.form['url'] = self.site_to_advertise
            except Exception as e:
                pass
            try:
                self.br.form['comment'] = self.get_comment(self.site_to_advertise, self.site_anchor_text)
            except Exception as e:
                pass
            try:
                self.br.form['message'] = self.get_comment(self.site_to_advertise, self.site_anchor_text)
            except Exception as e:
                pass

            #self.response = self.br.submit()
            page_content = self.br.response().read()
            match = re.search("Your comment is awaiting moderation.", str(page_content))
            match2 = re.search(self.site_to_advertise, str(page_content))

            if match:
                print(f"[!] {self.site_to_comment} - Comment is in the moderation queue.")
            elif match2:
                print(f"[+] {self.site_to_comment} - Comment has auto-posted.")
            else:
                print(f"[!] Failed to post comment.")

        except Exception as e:
            print(self.site_to_comment, e)
