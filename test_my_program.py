import unittest
from typing import List, Dict
import random
from Pairprogrammingbackend import reward

from Pairprogrammingbackend import suggest
from Pairprogrammingbackend import suggest_odds

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


p1 = Player()
p2 = Player()

class MyTestCase(unittest.TestCase):
    p1.dices = [1, 2, 3, 4, 5]
    p2.dices = [1, 1, 1, 1, 3]
    global odds
    for index, num in enumerate(nums):
        dist[num] = reward_nums[index]
        lock_1.clear()
        lock_2.clear()

    for index, name in enumerate(names):
        name_num[nums[index]] = name

    def test_something(self):
        self.assertEqual(suggest_odds(p1, p2, 3), 3)  # add assertion here

    def test_reward(self):
        self.assertEqual(reward(p1.dices, dist=dist, kind=1), 75)

    def test_reward_1(self):
        self.assertEqual(dist[11156], 10)
    def test_suggest(self):
        lock = suggest(p1.dices)
        self.assertEqual(lock, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
    init()
