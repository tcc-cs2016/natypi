import subprocess
import shlex

def run(**args):
    f_result = '../natypi/data/nmap_scan_result.txt'
    command = 'nmap -T4 -A -v 192.168.0.1/24'

    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, err = process.communicate()
    result  = '********** [ STDOUT ] **********\n%s********** [ STDERR ] **********\n%s' % (output, err)
    with open(f_result, 'w') as f:
        f.write(result)
    return result
