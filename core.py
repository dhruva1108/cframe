import numexpr as ne
import os

class Implement:
    def __init__(self):
        pass
    def implement():
        x = ne.detect_number_of_cores()
        os.environ['NUMEXPR_MAX_THREADS'] = str(x)
        print(f"Number of cores used = {x}")
