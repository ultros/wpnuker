import tools.wplogin
import tools.wpversioncheck
import tools.wpcomment
import tools.wpfindplugins


if __name__ == "__main__":
    # need to argparse
    url = "https://cybertutorials.org/"
    username = ""
    wordlist = ""

    site_to_comment = "https://www.cybertutorials.org/2022/python-wpnuker-a-collection-of-wordpress-pentesting-tools" \
                      "/#comment-72 "
    site_to_advertise = ""
    site_anchor_text = ""

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

def post_comment():
    wpc = tools.wpcomment.WPComment(site_to_comment, site_to_advertise, site_anchor_text)
    wpc.post_comment()

def get_plugins():
    gp = tools.wpfindplugins.FindPlugins(url)
    print(gp.get_plugins())

#check_version()
#brute_wp_login()
#post_comment()
get_plugins()