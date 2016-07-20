import nmap

def run(**args):
    nm = nmap.PortScanner()
    nm.scan('192.168.0.1/24', '21-443')
    result = nm.command_line() + '\n'
    for host in nm.all_hosts():
        result += '----------------------------------------------------\n'
        result += 'Host : %s (%s)\n' % (host, nm[host].hostname())
        result += 'State : %s\n' % nm[host].state()
        for proto in nm[host].all_protocols():
            result += '----------\n'
            result += 'Protocol : %s\n' % proto

            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                result += 'port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state'])

    return result

print run()
