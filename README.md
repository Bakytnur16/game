# game
#### 猜数字小游戏
> 随机生成1到20之间的一个整数，10次机会内猜对获胜。 ~~恐怖游戏~~

#### 井字游戏（第一阶段）
字典/列表 赋值
人机：九次循环内分胜负 【电脑随机走位】
1. 先走：人 - 电脑 （给函数设置先走还是后走的路线）
3. 后走: 电脑 - 人

要点：
1. 确定输赢：三个棋子连成一条线获胜  
列表赢法： 
横着 竖着 斜着

0.0 1.0 2.0  
0.1 1.1 2.1  
0.2 1.2 2.2  

字典？？判断位置 


2.确定谁先赢
放主循环最后 从第三次循环开始观察有没有执行
赢了打印停止循环

2. 如何让电脑想赢  ？不随机？
