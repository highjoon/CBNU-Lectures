"""
메시지 입력받고, 메시지 길이와 메시지를 단어로 분리하여 출력 (공백으로 분리)
"""

message = str(input("메시지 입력 : "))
length = len(message)
answer = message.split(" ")

print(length)
print(answer)