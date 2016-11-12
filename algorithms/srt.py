import unittest
from time import time
from namedlist import namedlist


Process = namedlist('Process', ['name', 'ti', 't', ('tf', None), ('T', None), ('E', None), ('I', None)])


def runSRTScheduler(processes):
    clock = 0

    for process in processes:
        process.t = [process.t, process.t]

    while not all(r[3] for r in processes):
        filtered_processes = [i for i in processes if i.ti <= clock and i.tf is None]
        filtered_processes.sort(key = lambda process: process.t[1])
        clock += 1
        if len(filtered_processes) > 0:
            process = filtered_processes[0]
            process.t[1] -= 1
            if process.t[1] == 0:
                process.t = process.t[0]
                process.tf = clock
                process.T = process.tf - process.ti
                process.E = process.T - process.t
                process.I = round(process.t / process.T, 4)
                
    processes.sort(key = lambda process: process.ti)


class TestSRTAlgorithm(unittest.TestCase):

    def test_3(self):
        processesList = []
        processesList.append(Process('A', 3, 2))
        processesList.append(Process('B', 2, 4))
        processesList.append(Process('C', 4, 3))
        processesList.append(Process('D', 10, 1))
        processesList.append(Process('E', 12, 5))
        processesList.append(Process('F', 6, 8))

        runSRTScheduler(processesList)
        #
        # self.assertEqual(processesList,
        #                  [Process('B', 2, 4, 8),
        #                   Process('A', 3, 2, 5),
        #                   Process('C', 4, 3, 11),
        #                   Process('F', 6, 8, 25),
        #                   Process('D', 10, 1, 12),
        #                   Process('E', 12, 5, 17)])
        #

        processesList.sort(key = lambda process: process.ti)

        self.assertEqual(processesList,
                         [Process('B', 2, 0, 8),
                          Process('A', 3, 0, 5),
                          Process('C', 4, 0, 11),
                          Process('F', 6, 0, 25),
                          Process('D', 10, 0, 12),
                          Process('E', 12, 0, 17)])


if __name__ == '__main__':
    unittest.main()
