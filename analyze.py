import re
from collections import OrderedDict
import subprocess

OUT_PATH = 'out.txt'

def main():
    metric_values = OrderedDict()
    coeff = 1000.0
    with open(OUT_PATH, 'rp') as out:
        for line in out.readlines():
            m = re.match(r'(\d+) (\w+)\: (.+)', line.strip())
            metric = m.group(2)
            value = int(coeff * float(m.group(3)))
            metric_values.setdefault(metric, [])
            metric_values[metric].append(value)
    for metric, values in metric_values.items():
        print metric
        subprocess.call(['spark'] + map(str, values))

if __name__ == '__main__':
    main()
