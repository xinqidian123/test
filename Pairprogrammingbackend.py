import random
from typing import List, Dict

# 初始化
# 玩家
# 筹码
# 骰子
# 倍率
# 每轮统计结果：
# 输入玩家盘面
# 得到分数
# 筹码重新分配
# 如果有人筹码小于0则终止游戏
# 倍率换算

nums: List[int] = [11156, 12255, 12346, 55566, 22223, 12345, 66666]
reward_nums: List[int] = [10, 10, 30, 20, 40, 60, 100]
names: List[str] = ['三连', '双对', '小顺子', '葫芦', '四连', '大顺子', '五连']
dist: Dict[int, int] = {}
name_num: Dict[int, str] = {}
count_all: int = 0
count_reward: int = 0


# 最后输出分数
class Player:
    chip: int
    dices: List[int]

    def __init__(self):
        self.chip = 50
        self.dices = []


count = 1
p1 = Player()
p2 = Player()
lock_1: List[int] = []
lock_2: List[int] = []
odds = 1
max_index = 0
count_p1 = 0
count_p2 = 0


# suggest_lock: List[int] = []

# 每一轮初始化
def init():
    global odds
    odds = 1
    for index, num in enumerate(nums):
        dist[num] = reward_nums[index]
        lock_1.clear()
        lock_2.clear()
        p1.dices.clear()
        p2.dices.clear()

    for _ in range(0, 5):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        p1.dices.append(x)
        p2.dices.append(y)

    for index, name in enumerate(names):
        name_num[nums[index]] = name


def roll_dice(lock_1: List[int], lock_2: List[int]):
    print(f"一号玩家锁定的骰子是：{lock_1}")
    print(f"二号玩家锁定的骰子是：{lock_2}")
    for i in range(0, 5):
        if i + 1 not in lock_1:
            p1.dices[i] = random.randint(1, 6)
        if i + 1 not in lock_2:
            p2.dices[i] = random.randint(1, 6)


# 计算得分与奖励得分
def reward(dices: List[int], dist: Dict[int, int], kind: int) -> int:
    global count_reward
    tmp: List[int] = []
    for i in dices:
        tmp.append(i)
    tmp.sort(reverse=False)
    count = 0
    reward_0 = 0
    score = 0
    for i in tmp:
        count = count * 10 + i
        score += i
    reward_0 += score
    if count in dist.keys():
        reward_0 += dist[count]
        # print(f"{name_num[count]}出现了")
        if kind == 1:
            count_reward += 1
    return reward_0


# 判断一轮谁赢谁输
def judge(score_1: int, score_2: int, p1: Player, p2: Player, odds: int):
    if score_1 == score_2:
        print(f"玩家一筹码{p1.chip},玩家二筹码{p2.chip}")
        print("两位玩家得分相同！")
        return

    if score_1 > score_2:
        p1.chip += (score_1 - score_2) * odds
        p2.chip -= (score_1 - score_2) * odds
        if p2.chip <= 0:
            p1.chip += p2.chip
            print("玩家二被击飞")
            # global count_p1
            # count_p1 += 1
            print(f"玩家一从玩家二获得筹码{p2.chip + (score_1 - score_2) * odds}")
            p2.chip = 0
            return
        print(f"玩家一筹码{p1.chip},玩家二筹码{p2.chip}")
        print(f"玩家一从玩家二获得筹码{(score_1 - score_2) * odds}")
    else:
        p2.chip += (score_2 - score_1) * odds
        p1.chip -= (score_2 - score_1) * odds
        if p1.chip <= 0:
            p2.chip += p1.chip
            print("玩家一被击飞")
            # global count_p2
            # count_p2 += 1
            print(f"玩家二从玩家一获得筹码{p1.chip + (score_2 - score_1) * odds}")
            p1.chip = 0
            return
        print(f"玩家一筹码{p1.chip},玩家二筹码{p2.chip}")
        print(f"玩家二从玩家一获得筹码{(score_2 - score_1) * odds}")


def play_round(count: int, dist: Dict[int, int]):
    score_1 = 0
    score_2 = 0
    # 玩家一人一次投掷骰子
    p1.dices.sort(reverse=False)
    p2.dices.sort(reverse=False)
    print(p1.dices)
    print(p2.dices)
    # 锁定0-5个骰子
    global odds, lock_1, lock_2
    if count < 2:
        print("第一位玩家要锁定的骰子是：（举例：您要锁定第1、2、4个骰子则输入1 2 4）")
        lock_1 = [eval(x) for x in input().split(" ")] #双人对站
        #lock_1 = suggest(p1.dices)  # 人机对战
        print(f"一号玩家锁定的骰子是：{lock_1}")
        print("第二位玩家要锁定的骰子是：（举例：您要锁定第1、2、4个骰子则输入1 2 4）")
        lock_2 = [eval(x) for x in input().split(" ")]
        # try:
        #     lock_2 = random_choice(p2.dices)
        # except ValueError:
        #     print("请确保输入数字")
        #     lock_2 = random_choice(p2.dices)
        # except NameError:
        #     print("请确保输入数字")
        #     lock_2 = random_choice(p2.dices)
        # except IndexError:
        #     print("输入数字在1-5之间")
        #     lock_2 = random_choice(p2.dices)
        # except:
        #     print("末尾不要有空格")
        #     lock_2 = random_choice(p2.dices)

        # lock_2 = suggest(p2.dices)
        # lock_2 = random_choice(p2.dices)
        print(f"二号玩家锁定的骰子是：{lock_2}")

        # 选定倍率
        while True:
            tmp = int(input("第一位玩家要输入的倍数（0123）"))
            #tmp = suggest_odds(p1, p2, odds=odds)  # tmp表示要增加的倍数

            if 0 <= tmp <= 3:
                odds += tmp
                break
            else:
                print("请重新输入您要增加的倍率")

        while True:
            tmp_1 = int(input("第二位玩家要输入的倍数（0123）")) # tmp_1表示要增加的倍数
            #tmp_1 = random.randint(0, 3)
            # if tmp == 0:
            #     tmp_1 = 3
            # else:
            #     tmp_1 = 0
            if 0 <= tmp_1 <= 3:
                odds += tmp_1
                break
            else:
                print("请重新输入您要增加的倍率")
        # 计分：奖、惩、判断是否击飞玩家
        print(f"当前倍率来到{odds}!")
        print(f"第一位玩家要输入的倍数（0123）:{tmp}")
        print(f"第二位玩家要输入的倍数（0123）:{tmp_1}")

    score_1 += reward(p1.dices, dist, 1)
    score_2 += reward(p2.dices, dist, 2)
    if count == 2:
        judge(score_1, score_2, p1, p2, odds)
    # roll_dice(lock_1, lock_2)
    # 给第二轮预备摇骰子
    for i in range(0, 5):
        if i + 1 not in lock_1:
            p1.dices[i] = random.randint(1, 6)
        if i + 1 not in lock_2:
            p2.dices[i] = random.randint(1, 6)


# 人队对战的ai算法，决定ai锁定的骰子数
def suggest(dices: List[int]) -> List[int]:
    suggest_lock: List[int] = []
    suggest_lock.clear()
    # 计算获得奖励的期望加上总分的期望，和对大于3的数进行锁定+3.5*（小于4）的数的值进行比较
    Exp_0 = 0.000
    global max_index
    max_index = -1
    p = 0
    arr: List[int] = []
    temp: List[int] = []
    dices.sort(reverse=False)
    for i in dices:  ## 计算不考虑奖励机制的分数期望
        if i < 4:
            Exp_0 += 3.5
        Exp_0 += i
    for i in range(0, len(nums)):  ## 骰子列表和每一种情况比较，计算奖励期望和分数期望
        Exp_reward = 0.000
        count = 0
        exp = []
        arr.clear()
        tmp = nums[i]
        while tmp > 1:
            arr.append(int(tmp % 10))
            tmp /= 10
        arr.reverse()
        for j in range(0, len(arr)):
            Exp_reward += arr[j]
            if arr[j] == dices[j]:
                count += 1
        p = pow(5 - count, 6)
        p = max(1, p)
        try:
            Exp_reward = (dist[nums[i]] + Exp_reward) / p
        except ZeroDivisionError:
            p = 1
            Exp_reward = (dist[nums[i]] + Exp_reward) / p

        if Exp_0 < Exp_reward:
            max_index = max(max_index, i)
    if max_index == -1:  # 没有凑的意义
        for i in range(0, len(dices)):
            if dices[i] > 3:
                suggest_lock.append(i + 1)
    else:  # 可以凑数字
        arr.clear()
        suggest_lock.clear()
        tmp = nums[max_index]
        while tmp > 1:
            arr.append(int(tmp % 10))
            tmp /= 10
        arr.reverse()
        for i in range(0, len(dices)):
            if dices[i] == arr[i]:
                suggest_lock.append(i + 1)
        # print(f"有机会出现{name_num[nums[max_index]]}")
    # print(suggest_lock)
    return suggest_lock


# 用来给玩家二的锁定骰子赋值，可以不予理会
def random_choice(dices: list[int]) -> list[int]:
    rc = []
    # for i in range(0, len(dices)):
    #     if dices[i] > 3:
    #         rc.append(i + 1)
    for i in range(1, 6):
        x = random.randint(0, 1)
        if x == 1:
            rc.append(i)
    return rc  #


# n = int(input("您要玩的游戏局数是："))
def suggest_odds(p1: Player, p2: Player, odds: int) -> int:
    # 根据分差计算增加倍率多少，己方得分小不增加倍率
    score_1 = reward(p1.dices, dist, 1)
    score_2 = reward(p2.dices, dist, 2)
    if score_1 < score_2:
        return 0
    elif odds * (score_1 - score_2) > 13:
        return 3
    elif odds * (score_1 - score_2) > 4:
        return 2
    else:
        return 1
    # else:
    #     return random.randint(1,3)


if __name__ == "__main__":  # 主程序
    m = 1
    # global count_p1, count_p2

    while m > 0:
        m -= 1
        n = 5 # 每次五局
        p1.chip = 100
        p2.chip = 100
        # count_p1 = 0
        # count_p2 = 0
        init()
        for i in nums:
            print(f"{i},{dist[i]},{name_num[i]}")
        for i in range(0, n):
            flag = 1
            init()
            print(f'\n第{i + 1}局\n')
            for j in range(0, 3):
                count_all += 1
                print(f"第{j + 1}轮")
                play_round(j, dist=dist)
                if p1.chip <= 0 or p2.chip <= 0:
                    flag = 0
                    break
            if flag == 0:
                break
        # if p1.chip == 0:

        # else:

        lock_1.clear()
        lock_2.clear()
        if p1.chip > p2.chip:
            count_p1 += 1
            print("恭喜玩家一获胜")
        else:
            count_p2 += 1
            print("恭喜玩家二获胜")

    print(f'玩家一获胜{count_p1}次，玩家二获胜{count_p2}次')
    print(f"玩家二奖励情况出现几率{count_reward * 1.00},{count_all * 1.00}")
