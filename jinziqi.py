import random

dic = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

print("一起来玩井字棋吧 :》 看到下面的棋盘了吗，每个宫格从1到9排列，输入对应的数字就可以放棋子啦 ~ \n")

print("  1  |  2  |  3")
print('-----+-----+-----')
print(f"  4  |  5  |  6")
print('-----+-----+-----')
print(f"  7  |  8  |  9")


wordBefore = ['先走','我先走','我先走吧','我先','先','xian','xianzou','woxianzou','X','x']  #关键词检索：先 走 我 吧（ ？ 按照输入转成对应字符串再对比 想想）
wordAfter = ['后走','我后走','houzou','hou','wohouzou','后走吧','后','o','O']

print("\n你想先走还是后走？ 先走是'X'，后走是'O'")

howGo = input('我想：')

if howGo in wordBefore:
    turn = 'X'
    r_turn = 'O'

elif howGo in wordAfter:
    turn = 'O'
    r_turn = 'X'
else:
    print("好的，再见！")
    exit(0)

#棋盘函数
def printBoard(dic):
    print(f"  {dic['1']}  |  {dic['2']}  |  {dic['3']}")
    print('-----+-----+-----')
    print(f"  {dic['4']}  |  {dic['5']}  |  {dic['6']}")
    print('-----+-----+-----')
    print(f"  {dic['7']}  |  {dic['8']}  |  {dic['9']}")

# 电脑走位
def robotMove(b):
    b = str(b)
    for b in dic:
        if dic[b] == ' ':
            dic[b] = r_turn
            # print('1')
            break
        else:
            # print('2')
            continue

#想法：在不改动循环的情况下，设置两个方法：先走：人先输机器再随机（没报错，后走：dic［a］报错
# 设置先后，轮流填空
# 想清楚为什么循环转了6次，输入放合适的地方 后期换掉while
while True:
    a = input('输入1-9:')
    if dic[a] == ' ':
        dic[a] = turn
        # print('3')

    elif dic[a] != ' ':
        if ' ' not in dic.values():
            # print("4")
            break
        else:
            print("已经走过了")
            continue
    b = random.randint(1,9)
    robotMove(b)
    printBoard(dic)

else:
    print("done")

 #设置输赢
# try:
#     dic[a]
# except KeyError:
#     print("只能输入1到9")