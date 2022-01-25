import random

dic = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}

def robotMove(b):
    b = str(b)
    for b in dic:
        if dic[b] == '':
            dic[b] = 'O'
            # print('1')
            break
        else:
            # print('2')
            continue

while True:
    a = input('输入1-9:')
    if dic[a] =='':
        dic[a] = 'X'
        # print('3')

    elif dic[a] !='':
        if '' not in dic.values():
            # print("4")
            break
        else:
            print("5")
            continue
    b = random.randint(1,9)
    robotMove(b)
    print(dic)

else:
    print("done")
