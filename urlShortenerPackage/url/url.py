from urllib.request import urlopen
import argparse
import sys

def shorten_url(url):
    tinyurl_request = 'http://tinyurl.com/api-create.php?url=' + url
    url_response = urlopen(tinyurl_request)
    shortened_url = url_response.read().decode()
    print(f"\nSHORTENED URL : {shortened_url}\n")

def run():
    argParse = argparse.ArgumentParser(description="SHORTENER TO REDUCE THE ENTERED LINK")
    argParse.add_argument('-u', '--usage', help="COMMAND USAGE FORMAT")
    req_args_grp = argParse.add_argument_group('REQUIRED ARGUMENTS')
    req_args_grp.add_argument('-l', '--link', help="URL TO SHORTEN", required=True)

    if len(sys.argv) == 1:
        argParse.print_help()
        sys.exit(1)
    elif '-h' in sys.argv or '--help' in sys.argv:
        argParse.print_help()
        sys.exit(1)
    elif '-u' in sys.argv or '--usage' in sys.argv:
        argParse.print_usage()
        sys.exit(1)
    elif '-l' in sys.argv or '--link' in sys.argv:
        arguments = argParse.parse_args()
        url_input = arguments.link
        shorten_url(url_input)

if __name__ == '__main__':
    run()