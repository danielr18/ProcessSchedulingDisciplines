import unittest
from namedlist import namedlist
from time import time

from namedlist import namedlist


Process = namedlist('Process', ['name', 'ti', 't', ('tf', None), ('T', None), ('E', None), ('I', None)])


def runRRScheduler(processes, q=3):
    processes.sort(key = lambda process: process.ti)

    for process in processes:
        process.t = [process.t, process.t]

    clock = 0

    while not all(r[3] for r in processes):
        processed = False
        for process in processes:
            if process.ti <= clock and process.tf is None:
                processed = True
                process.t[1] -= q
                if process.t[1] <= 0:
                    clock += process.t[1] + q
                    process.t = process.t[0]
                    process.tf = clock
                    process.T = process.tf - process.ti
                    process.E = process.T - process.t
                    process.I = round(process.t / process.T, 4)
                else:
                    clock += q
        if not processed:
            clock += 1


class TestRRAlgorithm(unittest.TestCase):

    def test_1(self):
        processesList = []
        processesList.append(Process('A', 7, 5))
        processesList.append(Process('B', 2, 3))
        processesList.append(Process('C', 1, 1))

        runRRScheduler(processesList, q=3)

        self.assertEqual(processesList,
                         [Process('C', 1, 1, 2, 1, 0, 1),
                          Process('B', 2, 3, 5, 3, 0, 1),
                          Process('A', 7, 5, 12, 5, 0, 1)])

    def test_2(self):
        processesList = []
        processesList.append(Process('A', 3, 1))
        processesList.append(Process('B', 1, 8))
        processesList.append(Process('C', 2, 10))
        processesList.append(Process('D', 4, 9))
        processesList.append(Process('E', 7, 3))

        runRRScheduler(processesList, q=5)

        self.assertEqual(processesList,
                         [Process('B', 1, 8, 23, 22, 14, 0.3636),
                          Process('C', 2, 10, 28, 26, 16, 0.3846),
                          Process('A', 3, 1, 12, 9, 8, 0.1111),
                          Process('D', 4, 9, 32, 28, 19, 0.3214),
                          Process('E', 7, 3, 20, 13, 10, 0.2308)])

    def test_3(self):
        processesList = []
        processesList.append(Process('A', 0, 3))
        processesList.append(Process('B', 1, 5))
        processesList.append(Process('C', 4, 2))
        processesList.append(Process('D', 5, 6))
        processesList.append(Process('E', 8, 4))

        runRRScheduler(processesList, q=4)

        self.assertEqual(processesList,
                         [Process('A', 0, 3, 3, 3, 0, 1),
                          Process('B', 1, 5, 18, 17, 12, 0.2941),
                          Process('C', 4, 2, 9, 5, 3, 0.4000),
                          Process('D', 5, 6, 20, 15, 9, 0.4000),
                          Process('E', 8, 4, 17, 9, 5, 0.4444)])


if __name__ == '__main__':
    unittest.main()
