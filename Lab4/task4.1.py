# TODO решите задачу
import json
FILENAME = 'input.json'
def task(fname) -> float:
    with open(fname, 'r') as f:
        data = json.load(f)
    return sum(map(lambda d: d['score'] * d['weight'], data))

print('%.3f' % task(FILENAME))
