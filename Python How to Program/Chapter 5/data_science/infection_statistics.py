import statistics
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import animation
import sys
import random


#def update(frame_number, infected_per_day, day, infected):
    
#    for i in range(infected_per_day):
#        infected[random.randrange(1,21)-1] +=1
        
#    plt.cla()
#    axes = sns.barplot(day, infected, palette='bright')
#    axes.set_title(f'COVID-19 Infection Rate by {len(day)} Days')
#    axes.set(xlabel='Days', ylabel='Infections')
    
#number_of_frames = int(sys.argv[1])
#rolls_per_frame = int(sys.argv[2])

#sns.set_style('whitegrid')
#figure = plt.figure('number of infected per day')
#values = list(range(1,21))

infected_per_day = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123,
1376, 1502, 894, 665, 1704, 1656, 1342]

mini = min(infected_per_day)
maxi = max(infected_per_day)
rangi = maxi - mini
mean_var = statistics.mean(infected_per_day)
mode_var = statistics.mode(infected_per_day)
median_var = statistics.median(infected_per_day)
vari = statistics.variance(infected_per_day)
sd = statistics.stdev(infected_per_day)


infected, day = np.unique(infected_per_day, return_index=True)
print(infected)
print(day)

title = f'COVID-19 Infection Rate by {len(day)} Days'
sns.set_style('whitegrid')
axes = sns.barplot(x=day, y=infected, palette='bright')
axes.set_title(title)
axes.set(xlabel='Days', ylabel='Infections')

plt.show()