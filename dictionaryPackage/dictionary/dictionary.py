from PyDictionary import PyDictionary
import argparse
import sys

def run():
    argParse = argparse.ArgumentParser(description="GET THE MEANING OF ANY ENTERED WORD")
    argParse.add_argument('-u', '--usage', help="COMMAND USAGE FORMAT")
    req_args_grp = argParse.add_argument_group('REQUIRED ARGUMENTS')
    req_args_grp.add_argument('-w', '--word', help="WORD TO SEARCH", required=True)

    if len(sys.argv) == 1:
        argParse.print_help()
        sys.exit(1)
    elif '-h' in sys.argv or '--help' in sys.argv:
        argParse.print_help()
        sys.exit(1)
    elif '-u' in sys.argv or '--usage' in sys.argv:
        argParse.print_usage()
        sys.exit(1)
    elif '-w' in sys.argv or '--word' in sys.argv:
        arguments = argParse.parse_args()
        word_input = arguments.word
        dictionaryObject = PyDictionary()
        wordMeaning = dictionaryObject.meaning(word_input)
        meaningDetails = ""
        if "Noun" in wordMeaning:
            meaningDetails += "Noun:\n- " + "\n- ".join(wordMeaning['Noun'])
        if "Verb" in wordMeaning:
            meaningDetails += "\n\nVerb:\n- " + "\n- ".join(wordMeaning['Verb'])
        print(meaningDetails)


if __name__ == '__main__':
    run()