import sys
import os
from ruff.__main__ import find_ruff_bin

def check(args):
    ruff = find_ruff_bin()
    exit_code = os.spawnv(os.P_WAIT, ruff, ["ruff", *args])
    sys.exit(exit_code)

