import sys, getopt
import re
import argparse
import platform
import subprocess
from ipaddress import ip_address
from multiprocessing import Pool, Queue
from concurrent.futures import ThreadPoolExecutor
import json
import socket
import time

ip_validator = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

def ip_scan(host):
    '''
    Return True if host (str) response to a ping request
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    '''

    # option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # building the command. E.g. "ping -c www.baidu.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def port_scan(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip.get('host'),ip.get('port')))
    sock.close()
    if result == 0:
        print(ip)
        return True
    return False

class IpAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
        pass

    def __call__(self, parser, namespace, values, option_string=None):

        ip_list = values.split("-",1)
        for ip in ip_list:
            if not ip_validator.match(ip):
                print(f'invalid ip address: {ip}')
                raise argparse.ArgumentTypeError('')
        
        values = self.ips(*ip_list)
        
        # Save the results in the namespace using the destination
        # variable given to our constructor.
        setattr(namespace, self.dest, values)
    
    def ips(self, start, end = None):
        '''Return IPs in IPv4 range, inclusive.'''
        start_int = int(ip_address(start).packed.hex(), 16)
        end_int = int(ip_address(end).packed.hex(), 16) if end else start_int
        start_int, end_int = [start_int, end_int] if start_int <= end_int else [end_int, start_int]
        return [ip_address(ip).exploded for ip in range(start_int, end_int + 1)]

def parseargs():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', action='store', dest='num', type=int, default=4, help='Store an ip range')

    parser.add_argument('-ip', action=IpAction, dest='ip_range', help='Store an ip range')

    parser.add_argument('-f', action='store', dest='func', default='ping', help='Store an function name')

    parser.add_argument('-w', action='store', dest='output', default='result.json', help='Store an ip range')

    parser.add_argument('-v', action='store_true', dest='verbose', help='Store an ip range')

    parser.add_argument('-m', action='store', dest='mode', default='proc', help='Store an ip range')

    results = {}
    try:
        results = parser.parse_args()
    except argparse.ArgumentTypeError:
        sys.exit(2)

    if not results.ip_range:
        print(f'-ip value is necessary')
        sys.exit(2)
    
    # print(results.ip_range)

    if results.func not in ['ping', 'tcp']:
        print(f'-f value must be ping or tcp')
        sys.exit(2)

    if results.mode not in ['proc', 'thread']:
        print(f'-m value must be proc or thread')
        sys.exit(2)

    return results

def pool_filter(pool, func, candidates):
    return [c for c, keep in zip(candidates, pool.map(func, candidates)) if keep]

if __name__ == "__main__":
    opts = parseargs()

    output = open(opts.output,'w',encoding='utf-8')

    st = time.time()
    
    pool = Pool(processes=opts.num) if opts.mode == 'proc' else ThreadPoolExecutor(max_workers=opts.num)
    if opts.func == 'ping':
        filtered_ping_list = pool_filter(pool,ip_scan,opts.ip_range)
        json.dump({'ip_scan': filtered_ping_list},fp=output,ensure_ascii=False)
    else:
        ip_with_ports = [{'host': opts.ip_range[0], 'port': port} for port in range(1, 1025)]
        filtered_tcp_list = pool_filter(pool,port_scan,ip_with_ports)
        json.dump({'port_scan': filtered_tcp_list},fp=output,ensure_ascii=False)

    if opts.verbose:
        print('time:', time.time() - st)
