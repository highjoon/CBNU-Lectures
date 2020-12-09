def my_function(food):
    print("in sub, food = ", food)
    food = 200

fruits = 100
my_function(fruits)
print("\n")
print("in main, fruits = ", fruits)