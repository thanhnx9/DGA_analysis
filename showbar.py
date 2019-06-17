import numpy as np
import matplotlib.pyplot as plt

data=[[44,50,144,40,4192,20,228,248,49,1000,174,777,169,800,33],[
4499,172783,10262,5923,723206,1660,8890,1340,8153,39386,8303,136968,863,968,105]]
fig, ax = plt.subplots()
X = np.arange(15)
#X=np.arange(48) #2 days
width=0.35
p1=ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
p2=ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)

ax.set_xticks(X + width / 2)
ax.set_xticklabels(('Sisron','Dircrypt','PadCrypt','Banjori','Symmi','Tofsee','Kraken','Shiotob','Ramnit','GameOver','Nivdort','Shifu','VolatileCedar','Murofet','Ranbyus'))
ax.legend((p1[0], p2[0]), ('Domains', 'Queries'))
#Thêm các giá trị trên mỗi cột
for x, y in zip(X, data[0]):
    plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom', fontsize='7')
for x, y in zip(X, data[1]):
    plt.text(x+0.02, y+0.05, '%d' % y, ha='center', va= 'bottom', fontsize='7')
plt.xticks(fontsize=7)
plt.yticks(fontsize=18)
ax.autoscale_view()
plt.show()
