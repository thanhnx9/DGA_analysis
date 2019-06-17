import numpy as np
import matplotlib.pyplot as plt

data=[[0,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777,777],
     [8,4137,4767,4603,4805,4850,4831,4772,4727,4783,4283,4928,3474,3312,4018,4458,4043,2789,3898,3104,4180,5102,4814,4930

     ]]
normal_data=[[196,9,5,5,6,6,5,6,5,58,37,20,62,29,13,26,10,9,9,57,69,80,112,52,
              #91,168,49,18,6,8,7,6,6,6,57,33
              #,30,7,3,5,64,46,33,35,11,20,8,17
              ],
            [583,19,11,11,13,12,11,13,11,162,74,104,167,79,49,171,34,19,20,102,115,107,302,109,
            # 502,330,110,36,17,19,18,17,17,17,106,205
             #,70,12,5,7,75,88,70,63,21,31,14,92
            ]]
fig, ax = plt.subplots()
X = np.arange(24)
#X=np.arange(48) #2 days
width=0.35
p1=ax.bar(X + 0.00, data[0], color = 'blue', width = 0.25, bottom=normal_data[0])
p2=ax.bar(X + 0.25, data[1], color ='g', width = 0.25,bottom=normal_data[1])
p3=ax.bar(X + 0.00, normal_data[0], color ='m', width = 0.25)
p4=ax.bar(X + 0.25, normal_data[1], color = 'y', width = 0.25)

ax.set_xticks(X + width / 2)
ax.set_xticklabels(('1h', '', '', '', '','6h','','','','','','12h',
                    '','','','','','18h','','','','','','24h'))
                    #'','','','','','30h','','','','','','36h',
                   # '','','','','','42h','','','','','','48h'))
#ax.legend((p1[0], p2[0]), ('Domains', 'Queries'))
ax.legend((p1[0], p2[0],p3[0],p4[0]), ('Generated Domains', 'NXDOMAIN Responses','Normal domains','Normal Responses'))
#Thêm các giá trị trên mỗi cột
for x, y in zip(X, normal_data[0]):
    plt.text(x-0.25, y+0.25, '%d' % y, ha='center', va= 'bottom', fontsize='6')
for x, y in zip(X, normal_data[1]):
    plt.text(x+0.5, y-0.5, '%d' % y, ha='center', va= 'bottom', fontsize='6')
for x, y, z in zip(X,data[0],normal_data[0]):
    plt.text(x-0.25, y-0.25+z, '%d' % y, ha='center', va= 'bottom', fontsize='6')
for x, y, z in zip(X,data[1],normal_data[1]):
    plt.text(x+0.5, y+0.2+z, '%d' % y, ha='center', va= 'bottom', fontsize='6')
plt.title('Shifu Mixed')
ax.autoscale_view()
plt.show()
