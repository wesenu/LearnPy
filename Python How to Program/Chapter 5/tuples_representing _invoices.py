#each tuple has (part ID string, description string, int quantity, float item price)
store_invoice = [
    ('83', 'Electric sander', 7, 57.98),
    ('24', 'Power saw', 18, 99.99),
    ('7', 'Sledge hammer', 11, 21.50),
    ('77', 'Hammer', 76, 11.99),
    ('39', 'Jig saw', 3, 79.50),
]

#sorted with a key argument to sort the 
#tuples by part description, then display the results
#use itemgetter

from operator import itemgetter

sort_invoice_name = sorted(store_invoice, key=itemgetter(1))
print(sort_invoice_name)

#Sort by price and display
sort_invoice_price = sorted(store_invoice, key=itemgetter(3))
print(sort_invoice_price)
