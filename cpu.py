import numpy as np
import random

'''
This is the cpu for this emulator(the mos6502) its an alternate version made specially for the nes.
currently everything inclusing loading roms will be done within this file, including the ROM until the project is expanded.
'''

class CPU:
    def __init__(self):

        # 6502 registers
        self.A = 0
        self.X = 0
        self.Y = 0
        self.PC = 0
        self.ROM = [0] * 1024 * 64

    '''
    Dictionary of opcodes to operations goes here
    '''

    def RAN(self): # testing binary stuff
        for i in range(0xFFFF):
            self.ROM[i] = random.randint(0x00, 0xFF)
            
        print((self.ROM))

    OP_TABLE = []

    '''
    Fetch Decode Execute here
    '''

    def fetch():
        pass

    def decode():
        pass

    def execute():
        pass

    

cpu = CPU()
cpu.RAN()
