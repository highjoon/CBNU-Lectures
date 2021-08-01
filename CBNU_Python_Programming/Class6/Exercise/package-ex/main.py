from game import user, computer, play

while True:
    you = user.choose_user()
    com = computer.choose_computer()
    result = play.run(you, com)
    print('You:', you, ', Computer:', com, ', Result:', result)
    answer = input('게임을 더 하시겠습니까?(y/n) ').lower()
    if answer.startswith('n'):
        break

play.print_result()
