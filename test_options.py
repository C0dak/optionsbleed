import subprocess
import sys

with open(sys.argv[1], 'r') as f:
    hosts_list = f.read().splitlines()

output_list = []
for h in hosts_list:
    tmp_cmd = 'python optionsbleed -a {}'.format(h)
    output = subprocess.check_output(tmp_cmd, shell=True)
    print h,output
    output_list.append((h,output))

with open('output.txt', 'w') as f:
    for l in output_list:
        f.write(l+'\n')
