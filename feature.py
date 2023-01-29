import os
import sys
import json

featuresListEdx = ['fpu','vme', 'de', 'pse', 'tsc', 'msr', 'pae', 'mce', 'cx8','apic', 'reserved', 'sep', 'mtrr', 'pge', 'mca', 'cmov', 'pat', 'pse-36', 'psn', 'clfsh', 'reserved', 'ds', 'acpi', 'mmx', 'fxsr', 'sse', 'sse2', 'ss', 'htt', 'tm', 'ia64', 'pbe']
featuresListEcx = ['sse3', 'pclmulqdq', 'dtes64', 'monitor', 'ds-cpl','vmx', 'smx', 'est', 'tm2', 'ssse3', 'cnxt-id', 'sdbg','fma', 'cx16', 'xtpr', 'pdcm', 'reserved', 'pcid', 'dca', 'sse4.1', 'sse4.2', 'x2apic', 'movbe','popcnt', 'tsc-deadline', 'aes', 'xsave', 'osxsave', 'avx', 'f16c', 'rdrnd', 'hypervisor']
os.system('./exec+ > result')
file = open('result')
result = file.readline()
result = result[0:32]
print(result)
#consider les features des autres registres

tab = []


# print(sys.argv)

for i in range(32):
    if result[i] == '1':
        tab.append(featuresListEcx[-i-1])

if os.path.exists('features_list.json'):
    os.system('rm features_list.json')

result = file.readline()
result = result[0:32]
print(len(featuresListEdx))

for a in range(32):
    if result[a] == '1':
        tab.append(featuresListEdx[-a-1])
f = open('features_list.json', 'a')
featuresList = json.dump(tab, f)

file.close()



