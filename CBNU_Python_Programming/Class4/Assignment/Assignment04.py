def EnglishDictionary():
    engdict = {}
    while True:
        word = str(input("단어 입력 : "))

        if (word in engdict) or (word.lower() in engdict):
            print("뜻 : {0}".format(engdict[word.lower()]))

        elif word == '종료':
            print("종료되었습니다." + '\n')
            print("======== 등록된 단어 목록입니다. ========" + '\n')

            for key, value in engdict.items():
                print("Eng : {0}  /  Kor : {1}".format(key, value))
            print('\n' + "=====================================")
            break

        elif not (word in engdict):
            meaning = str(input("사전에 없는 단어입니다. 뜻을 등록해주세요 : "))
            engdict[word.lower()] = meaning

def main():
    EnglishDictionary()

if __name__ == '__main__':
    main()


