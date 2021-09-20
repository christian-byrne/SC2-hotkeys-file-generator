"""Test cases for /grid.py

Usage:
    `import test-cases.py`
    `race, grid, prefix, name = case$N().values()`
    Where $N = case number.
    
Author:
    Christian P. Byrne

Since:
    Sep 21


"""


def case1():
    return {
        "race": "zerg",
        "grid": False,
        "prefix": "Control+",
        "name": "zerg-control-grid",
    }

def case2():
    return {
        "race": "zerg",
        "grid": False,
        "prefix": "Shift+",
        "name": "zerg-shift-grid",
    }

def case3():
    return {
        "race": "protoss",
        "grid": False,
        "prefix": "",
        "name": "protoss-grid",
    }