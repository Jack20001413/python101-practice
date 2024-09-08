# Every file in Python is modules

# Import self-written modules
from lib import human
human.walk()

from lib.human import walk
walk()

# Import Standard modules
import math
from math import sumprod