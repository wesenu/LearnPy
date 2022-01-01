queue_list = []


for i in range(3, 0, -1):
    print(f'Current list: {queue_list}' )
    print(f'Current element to enqueue: {i}')
    queue_list.append(i)
    
print(f'list after enqueue all elements: {queue_list}')


print(f'\nStarting dequeue')

for _ in range(len(queue_list)):
    print(f'Current list: {queue_list}' )
    print(f'Current element to to dequeue: {queue_list[0]}')
    queue_list.pop(0)
    

print(f'list after dequeue all elements: {queue_list}')

