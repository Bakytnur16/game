import random
from sys import exit

dic = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

print("""Let's play tic-tac-toe together :》   
Would you see the chessboard below? Each grid is arranged from 1 to 9
Enter the corresponding number to place the chess pieces ~ \n""")

print('  1  |  2  |  3  ')
print('-----+-----+-----')
print('  4  |  5  |  6  ')
print('-----+-----+-----')
print('  7  |  8  |  9  ')

# Keyword search:  ? Convert it to the corresponding string according to the input and then compare and think
wordBefore = ['go first', 'First', 'I\'ll go first', 'GO FIRST', 'FIRST', 'GO', 'X', 'x']
wordAfter = ['Go after', 'I\'ll go after', 'Let\'s go after', 'hou', 'wohouzou', 'After', 'AFTER', 'o', 'O']

print("\nDo you want to go first or later? Go first is 'X', go later is 'O'")

howGo = input('I want：')


# board function
def printBoard(dic):
    print(f"  {dic['1']}  |  {dic['2']}  |  {dic['3']}")
    print('-----+-----+-----')
    print(f"  {dic['4']}  |  {dic['5']}  |  {dic['6']}")
    print('-----+-----+-----')
    print(f"  {dic['7']}  |  {dic['8']}  |  {dic['9']}")


# judgment win or lose
list = [['1', '2', '3'], ['1', '4', '7'], ['1', '5', '9'], ['2', '5', '8'], ['3', '6', '9'], ['3', '5', '7'],
        ['4', '5', '6'], ['7', '8', '9']]  # win method


def Iswin():
    for i in list:
        # print(dic[i[0]], dic[i[1]], dic[i[2]])
        if dic[i[0]] == dic[i[1]] == dic[i[2]]:
            if dic[i[0]] == turn:
                print(f"\n----Congratulation! Your win-----")
                exit(0)
            elif dic[i[0]] == r_turn:
                print(f"\n----Computer wins-------")
                exit(0)
            else:
                return
    return False


# computer move
def robotMove():
    for i in dic:
        i = str(random.randint(1, 9))
        # i = b
        if dic[i] == ' ':
            dic[i] = r_turn
            print("\n-----Computer------\n")
            printBoard(dic)
            print('\ncomputer moved: ', i)
            break
        elif dic[i] != ' ':
            if ' ' not in dic.values():
                break
            else:
                # print('repeated',i)
                continue
    else:
        robotMove()
    Iswin()

"""After looping nine times, if no vacancy is found, enter the loop again until a vacancy is found and filled"""



# Judge first and then enter
# man move
def manMove():
    if ' ' not in dic.values():
        return

    a = input('Enter number： ')
    if dic[a] == ' ':
        dic[a] = turn
        print("\n-------You-------\n")
        printBoard(dic)
        # print(dic)

    elif dic[a] != ' ':
        print("  The number is repeated, choose another one.")
        manMove()
    Iswin()

# Solved the problem of redundant loops
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
        print("Ok, bye!")
        break
else:
    print("End!")

# don't forget to write try
