# #scatter 
import matplotlib.pyplot as plt
# hours_study=[1,2,3,4,5,6,7,8]
# scores = [30,40,50,60,70,80,90,100]
# plt.scatter(hours_study,scores,color='green',marker='o',label='Scores by hours')
# plt.xlabel('hours')
# plt.ylabel('scores')
# plt.title('hours vs scores')
# plt.legend()
# plt.grid()
# plt.show()

#subplot
fig, ax=plt.subplots(1,2,figsize = (10,5))
x=[1,2,3,4,5]
y=[5,10,15,20,25]
ax[0].plot(x,y)
ax[1].bar(x,y,color='green')
plt.tight_layout()
plt.savefig('subplot.png',dpi=300,bbox_inches='tight')
plt.show()
