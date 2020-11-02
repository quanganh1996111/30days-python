import os
import sys
def add_all_nums (*args):
    total=0
    for num in args:
        total += num
    return total
print(add_all_nums(123,245))