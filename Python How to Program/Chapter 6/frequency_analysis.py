from collections import Counter

def clean_text(test_text):
    return ''.join(char for char in test_text if char.isalnum())

def text_analysis(test_text):
    letter_collection = Counter(clean_text(test_text))
    return letter_collection


my_text = ('DJ DK C QLXDWI WF SDGDU PCX'
           'XLRLU KQCSLKBDQK, KJXDHDET FXWZ C BDIILE RCKL,'
           'BCGL PWE JBLDX FDXKJ GDSJWXO CTCDEKJ JBL LGDU TCUCSJDS LZQDXL. '
           'IYXDET JBL RCJJUL, XLRLU KQDLK ZCECTLI JW KJLCU KLSXLJ QUCEK JW JBL LZQDXL’K '
           'YUJDZCJL PLCQWE, JBL ILCJB KJCX, CE CXZWXLI KQCSL KJCJDWE PDJB LEWYTB QWPLX JW ILKJXWO CE LEJDXL' 
           'QUCELJ. QYXKYLI RO JBL LZQDXL’K KDEDKJLX CTLEJK, QXDESLKK ULDC XCSLK BWZL CRWCXI BLX KJCXKBDQ,' 
           'SYKJWIDCE WF JBL KJWULE QUCEK JBCJ SCE KCGL BLX QLWQUL CEI XLKJWXL FXLLIWZ JW JBL TCUCV')

mydict = text_analysis(my_text)
print(mydict.items())