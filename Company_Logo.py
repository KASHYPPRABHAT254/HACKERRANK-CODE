import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    from collections import Counter
    input_str = s
    char_count = Counter(input_str)
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_chars[:3]:
        print(char, count)
