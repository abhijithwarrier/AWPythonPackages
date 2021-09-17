import json
import yaml
import argparse
import sys

def run():
    argParse = argparse.ArgumentParser(description="CONVERT JSON TO YAML & YAML TO JSON")
    argParse.add_argument('-u', '--usage', help="COMMAND USAGE FORMAT")
    req_args_grp = argParse.add_argument_group('REQUIRED ARGUMENTS')
    req_args_grp.add_argument('-j', '--json', help="JSON FILE", required=True)
    req_args_grp.add_argument('-y', '--yaml', help="YAML FILE", required=True)
    req_args_grp.add_argument('-m', '--mode', help="CONVERSION MODE", choices=['j2y','json2yaml', 'y2j', 'yaml2json'], required=True)

    if len(sys.argv) == 1:
        argParse.print_help()
        sys.exit(1)
    elif '-h' in sys.argv or '--help' in sys.argv:
        argParse.print_help()
        sys.exit(1)
    elif '-u' in sys.argv or '--usage' in sys.argv:
        argParse.print_usage()
        sys.exit(1)
    elif '-j' in sys.argv or '--json' in sys.argv and '-y' in sys.argv or '--yaml' in sys.argv:
        arguments = argParse.parse_args()
        json_input = arguments.json
        yaml_input = arguments.yaml
        mode_input = arguments.mode
        if 'j2y' in mode_input or 'json2yaml' in mode_input:
            json_data = json.load(open(json_input, 'r'))
            yaml_file = open(yaml_input, 'w')
            yaml.safe_dump(json_data, yaml_file, allow_unicode=True, default_flow_style=False)

            yaml_data = yaml.load_all(open(yaml_input, 'r'), Loader=yaml.FullLoader)
            print("\n"+yaml.dump_all(yaml_data))
            print("\n############################################################################")
            print("\nOUTPUT: JSON FILE " + json_input.split('/')[-1] + " CONVERTED TO YAML FILE " + yaml_input.split('/')[-1] + "\n")
            print("############################################################################\n")

        elif 'y2j' in mode_input or 'yaml2json' in mode_input:
            yaml_data = yaml.safe_load(open(yaml_input, 'r'))
            # print(yaml_data)
            json_file = open(json_input, 'w')
            json.dump(yaml_data, json_file, indent=2)
            json_file.close()

            json_data = open(json_input,'r').read()
            print("\n" + json_data)

            print("\n############################################################################")
            print("\nOUTPUT: YAML FILE " + yaml_input.split('/')[-1] + " CONVERTED TO JSON FILE " + json_input.split('/')[-1] + "\n")
            print("############################################################################\n")


if __name__ == '__main__':
    run()