import random

# 玩家输入要出的拳
print("石头 剪刀 布")
player = input("你要出的拳是：")

# 电脑随机出拳
computer = "剪刀"
print("玩家出的拳是：%s ，电脑出的拳是：%s" % (player, computer))

# 玩家胜（石头——>剪刀；剪刀——>布；布——>石头）
if ((player == "石头" and computer == "剪刀")
        or (player == "剪刀" and computer == "布")
        or (player == "布" and computer == "石头")):
    print("今晚电脑弱爆了！")
# 平局
elif player == computer:
    print("再来一局，一决胜负！")
# 电脑胜
else:
    print("调整状态，再来一局！")
