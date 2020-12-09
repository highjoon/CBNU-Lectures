def my_function(food):
    print("in sub, food = ", food)
    food[0] = "melon"

fruits = ['apple', 'banana', 'cherry']
my_function(fruits)
print("in main, fruits = ", fruits)