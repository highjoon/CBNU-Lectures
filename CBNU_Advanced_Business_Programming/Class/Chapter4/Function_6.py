def max(a):
    i = 0
    maximum = 0
    while a[i] > 0:
        if a[i] > maximum:
            maximum = a[i]
        i += 1
    return maximum


def min(a):
    i = 0
    minimum = 100
    while a[i] > 0:
        if a[i] < minimum:
            minimum = a[i]
        i += 1
    return minimum


salary = [10, 50, 40, 90, 45, 77, 95, 25, -1]


print("max = ", max(salary))
print("min = ", min(salary))