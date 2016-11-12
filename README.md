#Process Scheduling Disciplines
The process scheduler is a part of the operating system that decides which process runs at a certain point in time.

##Algorithms:
- fifo : First In First Out
- lifo : Last In First Out
- sjn : Shortest Job Next
- ljn : Longest Job Next
- rrqX : Round Robin (where x is the quantum)
- srt: Shortest Remaining Time

- all: Run each of the previous algorithms

##Usage
`python3 main.py`

Expected input:
- --algorithm
- --numberOfProcesses
- --nameOfProcesses
- --initialTimeOfProcesses
- --executionTimeOfProcesses

##Examples

Round Robin - q3
```
$ python3 main.py

rrq3
3
A B C
1 3 5
2 5 4

Round Robin - q3
+------+----+---+----+--------+---+--------+
| name | ti | t | tf |   T    | E |   I    |
+======+====+===+====+========+===+========+
| A    | 1  | 2 | 3  | 2      | 0 | 1      |
+------+----+---+----+--------+---+--------+
| B    | 3  | 5 | 11 | 8      | 3 | 0.6250 |
+------+----+---+----+--------+---+--------+
| C    | 5  | 4 | 12 | 7      | 3 | 0.5714 |
+------+----+---+----+--------+---+--------+
| Avg. |    |   |    | 5.6667 | 2 | 0.7321 |
+------+----+---+----+--------+---+--------+
```

SRT

```
$ python3 main.py

srt
5
A B C D E
2 7 3 5 1
1 4 5 3 8

SRT
+------+----+---+----+--------+----+--------+
| name | ti | t | tf |   T    | E  |   I    |
+======+====+===+====+========+====+========+
| A    | 2  | 1 | 3  | 1      | 0  | 1      |
+------+----+---+----+--------+----+--------+
| B    | 7  | 4 | 15 | 8      | 4  | 0.5000 |
+------+----+---+----+--------+----+--------+
| C    | 3  | 5 | 8  | 5      | 0  | 1      |
+------+----+---+----+--------+----+--------+
| D    | 5  | 3 | 11 | 6      | 3  | 0.5000 |
+------+----+---+----+--------+----+--------+
| E    | 1  | 8 | 22 | 21     | 13 | 0.3810 |
+------+----+---+----+--------+----+--------+
| Avg. |    |   |    | 8.2000 | 4  | 0.6762 |
+------+----+---+----+--------+----+--------+
```
