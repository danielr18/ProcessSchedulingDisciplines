import unittest
from namedlist import namedlist
from collections import deque
from namedlist import namedlist


Process = namedlist('Process', ['name', 'ti', 't', ('tf', None), ('T', None), ('E', None), ('I', None)])


def runFIFOScheduler(processesList):
    clock = 0
    processesList.sort(key = lambda process: process.ti)

    for process in processesList:
        if(clock < process.ti):
            clock = process.ti

        clock += process.t
        process.tf = clock
        process.T = process.tf - process.ti
        process.E = process.T - process.t
        process.I = round(process.t / process.T, 4)


class TestFIFOAlgorithm(unittest.TestCase):

    def test_1(self):
        processesList = []
        processesList.append(Process('A', 7, 5))
        processesList.append(Process('B', 2, 3))
        processesList.append(Process('C', 1, 1))

        runFIFOScheduler(processesList)

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

        runFIFOScheduler(processesList)

        self.assertEqual(processesList,
                         [Process('B', 1, 8, 9),
                          Process('C', 2, 10, 19),
                          Process('A', 3, 1, 20),
                          Process('D', 4, 9, 29),
                          Process('E', 7, 3, 32)])

    def test_3(self):
        processesList = []
        processesList.append(Process('A', 0, 3))
        processesList.append(Process('B', 1, 5))
        processesList.append(Process('C', 4, 2))
        processesList.append(Process('D', 5, 6))
        processesList.append(Process('E', 8, 4))

        runFIFOScheduler(processesList)

        self.assertEqual(processesList,
                         [Process('A', 0, 3, 3),
                          Process('B', 1, 5, 8),
                          Process('C', 4, 2, 10),
                          Process('D', 5, 6, 16),
                          Process('E', 8, 4, 20)])

if __name__ == '__main__':
    unittest.main()
