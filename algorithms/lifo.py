import unittest
from bisect import bisect_right
from time import time
from namedlist import namedlist


Process = namedlist('Process', ['name', 'ti', 't', ('tf', None), ('T', None), ('E', None), ('I', None)])


def find_le(a, x, lo, hi):
    # Find rightmost value less than or equal to x
    i = bisect_right(a, x, lo, hi)
    if i == lo:
        return None
    else:
        return i -1


def schedule(process, clock):
    clock += process.t
    process.tf = clock
    process.T = process.tf - process.ti
    process.E = process.T - process.t
    process.I = round(process.t / process.T, 4)
    return clock


def LIFOScheduler(processes, processesTi, clock = 0, lo = 0, hi = None, acceptGreater = True):
    if hi is None:
        hi = len(processes) - 1

    if lo > hi:
        return (clock, lo, hi)

    i = find_le(processesTi, clock, lo, hi + 1)

    if i is None:
        if acceptGreater:
            i = lo
            clock = processes[i].ti
        else:
            return (clock, lo, hi)

    clock = schedule(processes[i], clock)
    lo1, hi1, lo2, hi2 = lo, i - 1, i + 1, hi

    while lo1 <= hi1:
        if lo2 > hi2 or clock < processes[lo2].ti:
            clock = schedule(processes[hi1], clock)
            hi1 -= 1
        else:
            clock, lo2, hi2 = LIFOScheduler(processes, processesTi, clock, lo2, hi2, False)

    return LIFOScheduler(processes, processesTi, clock, lo2, hi2, acceptGreater)


def runLIFOScheduler(processes):

    processes.sort(key = lambda process: process.ti)
    processesTi = [r[1] for r in processes]

    LIFOScheduler(processes, processesTi)


class TestLIFOAlgorithm(unittest.TestCase):

    def test_1(self):
        processesList = []
        processesList.append(Process('A', 7, 5))
        processesList.append(Process('B', 2, 3))
        processesList.append(Process('C', 1, 1))

        runLIFOScheduler(processesList)

        self.assertEqual(processesList,
                         [Process('C', 1, 1, 2),
                          Process('B', 2, 3, 5),
                          Process('A', 7, 5, 12)])

    def test_2(self):
        processesList = []
        processesList.append(Process('A', 3, 1))
        processesList.append(Process('B', 1, 8))
        processesList.append(Process('C', 2, 10))
        processesList.append(Process('D', 4, 9))
        processesList.append(Process('E', 7, 3))

        runLIFOScheduler(processesList)

        self.assertEqual(processesList,
                         [Process('B', 1, 8, 9),
                          Process('E', 7, 3, 12),
                          Process('D', 4, 9, 21),
                          Process('A', 3, 1, 22),
                          Process('C', 2, 10, 32)])

    def test_3(self):
        processesList = []
        processesList.append(Process('A', 0, 3))
        processesList.append(Process('B', 1, 5))
        processesList.append(Process('C', 4, 2))
        processesList.append(Process('D', 5, 6))
        processesList.append(Process('E', 8, 4))

        runLIFOScheduler(processesList)

        self.assertEqual(processesList,
                         [Process('A', 0, 3, 3),
                          Process('B', 1, 5, 8),
                          Process('E', 8, 4, 12),
                          Process('D', 5, 6, 18),
                          Process('C', 4, 2, 20)])


if __name__ == '__main__':
    unittest.main()
