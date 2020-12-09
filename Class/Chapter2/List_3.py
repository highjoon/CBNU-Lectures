letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print("* In letters [] = ", letters)

letters[2:5] = ['C', 'D', 'E']
print("** After letters[2;5] = ['C', 'D', 'E'], letters [] = ", letters)

letters[2:5] = []
print("** After letters[2:5] = [], letters [] = ", letters)
# 2 ~ 5 번째 인덱스를 빼고 출력

letters[ : ] = []
print("** After letters [ : ] = [], letters [] = ", letters)
# 전체 다 빼고 출력