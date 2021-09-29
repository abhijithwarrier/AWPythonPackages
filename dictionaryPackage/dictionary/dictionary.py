from PyDictionary import PyDictionary
import argparse
import sys

def word_meaning(word_input):
    """
    This method takes the word as the parameter. The input word is then passed to the
    PyDictionary() Object to obtain the meaning of the input word
    """
    dictionary_object = PyDictionary()
    word_dict_meaning = dictionary_object.meaning(word_input)
    meaning_details = ""
    if "Noun" in word_dict_meaning:
        meaning_details += "Noun:\n- " + "\n- ".join(word_dict_meaning['Noun'])
    if "Verb" in word_dict_meaning:
        meaning_details += "\n\nVerb:\n- " + "\n- ".join(word_dict_meaning['Verb'])
    print(meaning_details)

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
        word_meaning(word_input)

if __name__ == '__main__':
    run()