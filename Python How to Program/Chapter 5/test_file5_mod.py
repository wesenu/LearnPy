import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

rolls = [random.randrange(1,7) for i in range(6000000)]
value, frequence = np.unique(rolls, return_counts= True)

title = f'Rolling a SIX-Sided die {len(rolls): ,} Times'

sns.set_style('whitegrid')

axes = sns.barplot(x=value, y=frequence, palette='bright')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequence) * 1.10)

for bar, frequency in zip(axes.patches, frequence):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text,
              fontsize=11, ha='center', va='bottom')
    
plt.show()