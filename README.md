# game
#### 猜数字小游戏
> 随机生成1到20之间的一个整数，10次机会内猜对获胜。 ~~恐怖游戏~~

#### 井字游戏（第二阶段）
字典 赋值
人机：九次循环内分胜负 【电脑随机走位】
1. 先走：人 - 电脑
2. 后走: 电脑 - 人

要点：
1. 确定输赢：三个棋子连成一条线获胜  
列表： 
横着 竖着 斜着  
list = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]

字典：  
1 2 3  
4 5 6  
7 8 9  

数字不分前后  
123  147  159  
258  369  357
456  789 

确定谁先赢
放主循环最后 从第三次循环开始观察有没有执行
赢了打印停止循环

2. 如何让电脑想赢  ？不随机？
