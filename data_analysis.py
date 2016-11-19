import csv
from collections import namedtuple

Container = namedtuple(
    'Container',
    ['capacity', 'length']
)


def num_trucks_needed(avg_cap, total_cap):
    return total_cap / avg_cap


with open('data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=' ', quotechar='|')
    for row in reader:
        # vess, oper, cargo, quant, ship_line, cont, bill_lad, size, port, unload_port, local_ipi, inland_point, voy_no = split ''
        print(row)
