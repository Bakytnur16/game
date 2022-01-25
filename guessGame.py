import random
from sys import exit

print("""
\t 今天是1月24号，被困在这座废弃古宅的第382天...
\t 我想我已经没有任何再逃出的机会了...
\t 但是就在昨天...
\t 我收到了一张纸条
""")
print('-' * 10)
print("是 / 否 打开纸条")
choice = input("你的选择是： ")

strList = ['是', 'shi', '是的', '好','hao','行', '太好了']

if choice in strList:
    print('-' * 10)
    print("""信上写着：
    \t嘻嘻 ~ 
    \t我在想一个1到20之间的整数，给你10次机会，你要是猜出来我就放过你 ~ 
    \t 但你要是猜不出来，嘻嘻..""")
    print('-' * 10)
    numGive = random.randint(1, 20)
    for guessTime in range(10):
        print('你认为这个数字是: ', end='')
        guess = int(input())

        while 0 < guess < 21:
            if guess < numGive:
                print(f'猜 错 啦~ 比{guess}大')
                break
            elif guess > numGive:
                print(f'猜 错 啦~ 比{guess}小')
                break
            elif guess == numGive:
                print("""
    猜对了！
    你颤抖地身体不敢相信这一刻的到来 这是数百个绝望且充满恐惧的日夜换来的一丝生机        
    "嘻嘻 竟然被你猜对了 门就在那"...
    那道腐朽不堪的门被无形的力量打开了 瞬间无数道光填满了漆黑的空间
    你空洞的眼神瞬间有了光泽 伴随着黎明的到来 倒映着一道炽热的光芒 那是对生的渴望
    全身沸腾的血液在剧烈跳动的心脏里收缩绽放 迎着初生的阳光
    你连滚带爬地从地上冲向光去..这一刻终于到来
                    """)
                print('解锁结局：迟来的光明')
                exit(0)
                # 再检查一遍循环逻辑，exit暂时放着；再丰富些内容结局
        else:
            print('嘻嘻，都说了只能猜1到20之间的数字')
        print(f"你还剩{9 - guessTime}次机会了呦")

    print("""
    ”猜了十次都没猜出来嘻嘻“, ...
    听到着 你僵硬地朝着声音的方向看去
    黑影却在身后慢慢靠近 一把抓住你的脚踝 身体被重重的摔在地上
    你被无形的力量拖拽着...身体与地面摩擦留下一道黑色的痕迹
    那是已经发黑的血液...丧失的嗅觉闻不出黑夜里弥漫的腐臭
    正如那具麻木的身体已感受不到恐惧
    你的眼神涣散 像是已经宣告自己的结局...身体被残忍地肆意摧毁
    至少这一次你再也不用醒来...再也不用对着惨不忍睹地身体发呕
    再也不用看见满身密密麻麻蠕动的蛆虫在身体里钻进钻出
    想到这 你合上双眼 露出了诡异的笑容...
    黑夜褪去 黎明破晓 死寂的房间里 一具尸体 大卸八块
    完
    """)
    print("解锁结局：不完整的身体")

else:
    print('-' * 10)
    print("""
    “喜欢什么死法都满足你嘻嘻...” ，
    耳边是刺耳的嗡嗡声..震得你耳膜发疼..你再也没听清楚任何声音
    身边是鲜红蔓延的血泊...肢体已经没有任何感觉..
    只觉得眼神逐渐模糊，迷离，你在痛苦中失去了意识...再也没有醒来
    泪水划过尚有余温的眼角，你万分后悔...
    如果..能再来一次..
    漆黑的夜晚 只剩下一具似在喧嚣的尸体
    完
    """)
    print("解锁结局：与黎明只差半毫")
