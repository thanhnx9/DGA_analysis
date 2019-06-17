import os
import numpy as np
import matplotlib.pyplot as plt
import re
import os
name = input("Name of DGA Botnet: ")
os.system("python \"analysis log.py\" -i 1.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 2.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 3.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 4.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 5.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 6.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 7.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 8.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 9.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 10.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 11.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 12.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 13.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 14.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 15.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 16.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 17.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 18.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 19.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 20.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 21.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 22.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 23.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 24.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 25.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 26.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 27.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 28.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 29.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 30.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 31.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 32.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 33.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 34.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 35.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 36.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 37.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 38.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 39.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 40.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 41.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 42.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 43.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 44.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 45.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 46.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 47.txt -o out-new.txt")
os.system("python \"analysis log.py\" -i 48.txt -o out-new.txt")
one = re.compile(r'Tong so queries la:.*?([0-9.-]+)')
two = re.compile(r'So luong domain sinh ra:.*?([0-9.-]+)') 
def getvalue(regexp):
	result = []
	with open('out-new.txt') as f:
		for line in f:
			match = regexp.match(line)
			if match:
				result.append(match.group(1))
	return result
queries=list(map(float,getvalue(one)))
print(queries)
domain=list(map(float,getvalue(two)))
print(domain)

data=[domain,queries]
fig, ax = plt.subplots()
#X = np.arange(24)
X=np.arange(48) #2 days
width=0.35
p1=ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
p2=ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)

ax.set_xticks(X + width / 2)
ax.set_xticklabels(('1h', '', '', '', '','6h','','','','','','12h',
                    '','','','','','18h','','','','','','24h',
                    '','','','','','30h','','','','','','36h',
                    '','','','','','42h','','','','','','48h'))
ax.legend((p1[0], p2[0]), ('Domains', 'Queries'))
#Thêm các giá trị trên mỗi cột
for x, y in zip(X, data[0]):
    plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom', fontsize='7')
for x, y in zip(X, data[1]):
    plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom', fontsize='7')
plt.title(name)
ax.autoscale_view()
plt.show()
