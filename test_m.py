from main import minim, maxim, summ, proizv
import math
import time
import unittest

class SolutionTestCase(unittest.TestCase):
    def test_minim(self):
        with open("input.txt", 'r') as file:
            a = list(map(int, file.read().split()))
        assert min(a) == minim(a)


    def test_maxim(self):
        with open("input.txt", 'r') as file:
            a = list(map(int, file.read().split()))
        assert max(a) == maxim(a)


    def test_summ(self):
        with open("input.txt", 'r') as file:
            a = list(map(int, file.read().split()))
        assert sum(a) == summ(a)


    def test_proizv(self):
        with open("input.txt", 'r') as file:
            a = list(map(int, file.read().split()))
        assert math.prod(a) == proizv(a)

    def test_minmax(self):
        with open("input.txt", 'r') as file:
            a = list(map(int, file.read().split()))
        assert maxim(a) == minim(a)


    def test_time(self):
        with open("input.txt", 'r') as file:
            a = list(map(int, file.read().split()))
        time_start = time.time()
        maxim(a)
        minim(a)
        proizv(a)
        summ(a)
        time_finish = time.time()
        time_nach = time_finish - time_start
        b = a
        b.append(23)
        b.append(323)
        maxim(b)
        minim(b)
        proizv(b)
        summ(b)
        time_new= time.time()
        time_f = time_new - time_finish
        print("начальное время", time_finish)
        print("разница", time_f)