#scatter 
import matplotlib.pyplot as plt
hours_study=[1,2,3,4,5,6,7,8]
scores = [30,40,50,60,70,80,90,100]
plt.scatter(hours_study,scores,color='green',marker='o',label='Scores by hours')
plt.xlabel('hours')
plt.ylabel('scores')
plt.title('hours vs scores')
plt.legend()
plt.grid()
plt.show()