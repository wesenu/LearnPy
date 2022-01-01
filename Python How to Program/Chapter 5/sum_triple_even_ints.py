my_list = list(range(1,11))

triple_even = list((map(lambda x: x**3,
                       filter(lambda x: x%2==0, my_list))))
sum_triple_even = sum(triple_even)
print(sum_triple_even)

triple_even_lsit_comp = [x**3 for x in range(1, 11) if x%2==0]

print(triple_even_lsit_comp)