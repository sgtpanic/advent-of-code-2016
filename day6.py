from collections import defaultdict
from operator import itemgetter

with open('day6.txt', 'r') as f:
    lines = f.readlines()
    lines_dicts = [defaultdict(int) for _ in range(len(lines[0]) - 1)]
    for line in lines:
        line = line.strip()
        for i in range(len(line)):
            lines_dicts[i][line[i]] += 1
    for each in lines_dicts:
        sorted_dict = sorted(each.items(), key=itemgetter(1))
        print(sorted_dict[0][0], end='')


