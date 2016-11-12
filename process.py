from texttable import Texttable

from namedlist import namedlist


Process = namedlist('Process', ['name', 'ti', 't', ('tf', None), ('T', None), ('E', None), ('I', None)])


def draw_processes_table(processes):
    t = Texttable()
    t.set_precision(4)
    t.add_rows([list(Process._fields),
                *[list(x) for x in processes],
                ['Avg.','','','',sum(p.T for p in processes) / len(processes),sum(p.E for p in processes) / len(processes),sum(p.I for p in processes) / len(processes)]])
    return t.draw()
