import webbrowser
import wikipedia
import argparse
import sys

def run():
    argParse = argparse.ArgumentParser(description="OPENING WIKIPEDIA PAGE OF THE ENTERED INPUT")
    argParse.add_argument('-u', '--usage', help="COMMAND USAGE FORMAT")
    req_args_grp = argParse.add_argument_group('REQUIRED ARGUMENTS')
    req_args_grp.add_argument('-i', '--input', help="TERM TO SEARCH", required=True)

    if len(sys.argv) == 1:
        argParse.print_help()
        sys.exit(1)
    elif '-h' in sys.argv or '--help' in sys.argv:
        argParse.print_help()
        sys.exit(1)
    elif '-u' in sys.argv or '--usage' in sys.argv:
        argParse.print_usage()
        sys.exit(1)
    elif '-i' in sys.argv or '--input' in sys.argv:
        arguments = argParse.parse_args()
        wiki_input = arguments.input
        wiki_url = wikipedia.page(wiki_input).url
        webbrowser.open_new_tab(wiki_url)

if __name__ == '__main__':
    run()