def sum(i, j):
    valsum = 0
    for k in range(i, j):
        valsum += k
    print("at ft()/valsum ---", valsum)
    return(valsum)

print("<--> at main()/sum(1,10) = ", sum(1,10))
print()
print("<--> at main()/sum(1,20) = ", sum(1,20))
print()
print("<--> at main()/sum(1,30) = ", sum(1,30))