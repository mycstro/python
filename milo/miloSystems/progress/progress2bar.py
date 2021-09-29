# -*- coding: utf-8 -*-
import time
from time import sleep
import sys

# Print iterations progress
def progress(count, total, prefix='', suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('%s[%s] %s%s ...%s\r' % (prefix, bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben

def progress1(ti):
    for it in range(0, ti):
        time.sleep(1)
        sys.stdout.write("\r%d%%" % it)
    sys.stdout.flush()

def pfpbc(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
        sys.stdout.flush()

class ProgressBar:
    def __init__(self):
        # A List of Items
        items = list(range(0, 5))
        l = len(items)
        self.inicall(l, items)

    def inicall(self, le, item):
        # Initial call to print 0% progress
        pfpbc(0, le, prefix = 'Progress:', suffix = 'Complete')
        for i, item in enumerate(item):
            # Do stuff...
            sleep(0.1)
            # Update Progress Bar
            pfpbc(i + 1, le, prefix = 'Progress:', suffix = 'Complete')

class ProgressBar1():
    def __init__(self, end_va):
        end_v = end_va
        self.cli_progress_test(end_v)

    def cli_progress_test(self, end_val, bar_length=20):
        for i in range(0, end_val):
            percent = float(i) / end_val
            hashes = '#' * int(round(percent * bar_length))
            spaces = ' ' * (bar_length - len(hashes))
            sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100.0))))
            sys.stdout.flush()


if __name__ == "__main__":
    ProgressBar()
    print()
    progress1(10)
    print()
    ProgressBar1(10)
    print()
    progress(10, 10, 'Progress', 'Complete')



