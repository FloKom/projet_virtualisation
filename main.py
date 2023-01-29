import os
import sys
import json
import time


os.system('xl create /etc/xen/myvm2.cfg')

while not os.path.exists('/home/florian/logFiles/features_list.json'):
    pass

os.system('xl destroy myvm2')

f = open('/home/florian/logFiles/features_list.json')
listFeatures = json.load(f)

time.sleep(15)

os.system('cp /etc/xen/myvm2.cfg /etc/xen/myvm2.cfg.old')

for x in listFeatures:

    os.system('rm /etc/xen/myvm2.cfg')
    os.system('cp /etc/xen/myvm2.cfg.old /etc/xen/myvm2.cfg')
    file = open('/etc/xen/myvm2.cfg', 'a')
    file.write("\n")
    command = 'cpuid="host,{}=0"'        
    file.write(command.format(x))
    file.close()
    os.system('xl create /etc/xen/myvm2.cfg')

    lastTime = time.time()
    while not (os.path.exists('/home/florian/logFiles/log')):
        if (time.time()-lastTime > 8):
            lastTime = time.time()
            os.system('xl list -l > status.json')
            #lire status de la vm
            f = open('status.json')
            status = json.load(f)
            f.close()
            present = False
            for vm in status:
                if vm['config']['c_info']['name'] == "myvm2":
                    present = True
            if not present:
                command = 'echo {} >> /home/florian/logFiles/some_useful_features'
                os.system(command.format(x))
                # os.system('xl destroy myvm2')
                break

    if os.path.exists('/home/florian/logFiles/log'):
        command = 'cp /home/florian/logFiles/log /home/florian/logFiles/log_test_suite_{}'
        os.system(command.format(x))
        os.system('rm /home/florian/logFiles/log')
        os.system('xl destroy myvm2')
        time.sleep(15)