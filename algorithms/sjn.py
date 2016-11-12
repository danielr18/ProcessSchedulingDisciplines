import unittest
from namedlist import namedlist
from namedlist import namedlist


Process = namedlist('Process', ['name', 'ti', 't', ('tf', None), ('T', None), ('E', None), ('I', None)])


def runSJNScheduler(processes):
    clock = 0

    while not all(r[3] for r in processes):
        filtered_processes = [i for i in processes if i.ti <= clock and i.tf is None]
        filtered_processes.sort(key = lambda process: process.t)
        if len(filtered_processes) > 0:
            process = filtered_processes[0]
            clock += process.t
            process.tf = clock
            process.T = process.tf - process.ti
            process.E = process.T - process.t
            process.I = round(process.t / process.T, 4)
        else:
            clock += 1
