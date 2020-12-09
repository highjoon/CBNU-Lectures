L = [1,2,3,4,5,6,7,8,9,10]

for i in L:
    if i % 2 == 0:
        continue
    print("Item: {0}".format(i))
    
# 나누어 떨어지면 continue

"""
Item: 1
Item: 3
Item: 5
Item: 7
Item: 9
"""