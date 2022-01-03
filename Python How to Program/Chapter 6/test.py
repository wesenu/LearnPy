#country_codes = {'Findland': 'fi', 'South Africa':'za', 'Nepal': 'np'}
#print(country_codes)

#country_codes.clear()

#ays_per_month = {'January': 31, 'February': 28, 'March': 31}

#for month, days in days_per_month.items():
#    print(f'{month} has {days} days')
    
    
    
from collections import Counter
text = ('to be or not to be that is the question')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')