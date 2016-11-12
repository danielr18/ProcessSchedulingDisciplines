import sys
from process import Process, draw_processes_table
from algorithms.rr import runRRScheduler
from algorithms.fifo import runFIFOScheduler
from algorithms.lifo import runLIFOScheduler
from algorithms.srt import runSRTScheduler
from algorithms.sjn import runSJNScheduler
from algorithms.ljn import runLJNScheduler

algorithms = {
    'lifo': {
        'run': runLIFOScheduler,
        'name': 'LIFO'
    },
    'srt': {
        'run': runSRTScheduler,
        'name': 'SRT'
    },
    'fifo': {
        'run': runFIFOScheduler,
        'name': 'FIFO'
    },
    'sjn': {
        'run': runSJNScheduler,
        'name': 'SJN'
    },
    'ljn': {
        'run': runLJNScheduler,
        'name': 'LJN'
    },
    'rr': {
        'run': runRRScheduler,
        'name': 'Round Robin'
    }
}

if  __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    algorithm = data[0]
    n = int(data[1])
    names = data[2:n+2]
    TIs = list(map(int, data[n+2:2*n+2]))
    Ts = list(map(int, data[2*n+2:3*n+2]))
    processes = [Process(name, ti, t) for name, ti, t in zip(names, TIs, Ts)]

    if algorithm == 'all':
        for alg, value in algorithms.items():
            processes = [Process(name, ti, t) for name, ti, t in zip(names, TIs, Ts)]
            value['run'](processes)
            print('{} - q3'.format(value['name']) if 'rr' == alg else value['name'])
            print(draw_processes_table(processes))

    elif 'rrq' in algorithm:
        q = int(algorithm.split('q')[1])
        algorithms['rr']['run'](processes, q)
        print('{} - q{}'.format(algorithms['rr']['name'], q))
        print(draw_processes_table(processes))

    else:
        algorithms[algorithm]['run'](processes)
        print(algorithms[algorithm]['name'])
        print(draw_processes_table(processes))
