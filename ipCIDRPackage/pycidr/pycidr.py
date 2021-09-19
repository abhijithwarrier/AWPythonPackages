import ipaddress
import argparse
import sys

def run():
    argParse = argparse.ArgumentParser(description="IPv4 CIDR CALCULATOR")
    argParse.add_argument('-u', '--usage', help="COMMAND USAGE FORMAT")
    req_args_grp = argParse.add_argument_group('REQUIRED ARGUMENTS')
    req_args_grp.add_argument('-a', '--address', help="IPv4 ADDRESS", required=True)

    if len(sys.argv) == 1:
        argParse.print_help()
        sys.exit(1)
    elif '-h' in sys.argv or '--help' in sys.argv:
        argParse.print_help()
        sys.exit(1)
    elif '-u' in sys.argv or '--usage' in sys.argv:
        argParse.print_usage()
        sys.exit(1)
    elif '-a' in sys.argv or '--address' in sys.argv:
        arguments = argParse.parse_args()
        ip_address = arguments.address
        ip_address = ipaddress.ip_interface(ip_address)
        network_address = ip_address.network
        first_ip_address = list(network_address.hosts())[0]
        last_ip_address = list(network_address.hosts())[-1]
        number_of_usable_ips = len(list(network_address.hosts()))
        broadcast_address = network_address.broadcast_address
        wildcard = ip_address.hostmask
        subnet_mask = ip_address.with_netmask.split('/')[1]

        print(f"\nNETWORK ADDRESS : {str(network_address).split('/')[0]}\nFIRST HOST IP ADDRESS : {first_ip_address}"
              f"\nLAST HOST IP ADDRESS : {last_ip_address}"f"\nNUMBER OF USABLE IPs : {number_of_usable_ips}"
              f"\nBROADCAST ADDRESS : {broadcast_address}\nSUBNET MASK : {subnet_mask}\nWILDCARD : {wildcard}")

if __name__ == '__main__':
    run()