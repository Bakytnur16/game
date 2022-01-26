import random
from sys import exit

dic = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

print("一起来玩井字棋吧 :》 看到下面的棋盘了吗，每个宫格从1到9排列，输入对应的数字就可以放棋子啦 ~ \n")

print('  1  |  2  |  3  ')
print('-----+-----+-----')
print('  4  |  5  |  6  ')
print('-----+-----+-----')
print('  7  |  8  |  9  ')


wordBefore = ['先走','我先走','我先走吧','我先','先','xian','xianzou','woxianzou','X','x']  #关键词检索：先 走 我 吧（ ？ 按照输入转成对应字符串再对比 想想）
wordAfter = ['后走','我后走','houzou','hou','wohouzou','后走吧','后','o','O']

print("\n你想先走还是后走？ 先走是'X'，后走是'O'")

howGo = input('我想：')

#棋盘函数
def printBoard(dic):
    print(f"  {dic['1']}  |  {dic['2']}  |  {dic['3']}")
    print('-----+-----+-----')
    print(f"  {dic['4']}  |  {dic['5']}  |  {dic['6']}")
    print('-----+-----+-----')
    print(f"  {dic['7']}  |  {dic['8']}  |  {dic['9']}")

#判断输赢
list = [['1', '2', '3'], ['1', '4', '7'], ['1', '5', '9'], ['2', '5', '8'], ['3', '6', '9'], ['3', '5', '7'],
        ['4', '5', '6'], ['7', '8', '9']] #赢法
def Iswin():
    for i in list:
        # print(dic[i[0]], dic[i[1]], dic[i[2]])
        if dic[i[0]] == dic[i[1]] == dic[i[2]]:
            if dic[i[0]] == turn:
                print(f"\n----恭喜您赢了-----")
                exit(0)
            elif dic[i[0]] == r_turn:
                print(f"\n----电脑赢了-------")
                exit(0)
            else:
                return
    return False

# 电脑走位
def robotMove():
        for i in dic:
            i = str(random.randint(1, 9))
            # i = b
            if dic[i] == ' ':
                dic[i] = r_turn
                print("\n-------电脑-------\n")
                printBoard(dic)
                print('\n电脑走了: ',i)
                break
            elif dic[i] != ' ':
                if ' ' not in dic.values():
                    break
                else:
                    # print('重复了',i)
                    continue
        else:#循环九次后，没找到空位就再次进入循环，知道找到空位并填补
            robotMove()
        Iswin()

#先判断后输入
# 人走位
def manMove():
    if ' ' not in dic.values():
        return

    a = input('输入数字： ')
    if dic[a] == ' ':
        dic[a] = turn
        print("\n--------您-------\n")
        printBoard(dic)
        # print(dic)
    elif dic[a] != ' ':
        print("     数字重复了，从新选一个吧。")
        manMove()
    Iswin()

# 解决了循环多余的问题
while ' ' in dic.values():
    if howGo in wordBefore:
        turn = 'X'
        r_turn = 'O'
        manMove()
        robotMove()

    elif howGo in wordAfter:
        turn = 'O'
        r_turn = 'X'
        robotMove()
        manMove()
    else:
        print("好的，再见！")
        break
else:
    print("结束！")
