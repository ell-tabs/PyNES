import numpy as np
import random
import os
import time
from MAIN import opcode_table as op
from MAIN import CPU as CPU

'''
This is the cpu for this emulator(the mos6502) its an alternate version made specially for the nes.
currently everything inclusing loading roms will be done within this file, including the ROM until the project is expanded.
'''

cpu = CPU.CPU()
cpu.LOAD_ROM()
cpu.print_memory()

while True:
    cpu.execute()
    cpu.PRINT_VALUES()
    time.sleep(2)
