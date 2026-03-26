import numpy as np
import random
import os
import time

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
        self.SP = 0
        self.memory = [0] * 16

        # example program
        self.program = [0xA9, 100, 0xA9, 255, 0xA9, 233, 0xA9, 4]


    def LOAD_ROM(self): # testing binary stuff
        for i in range(len(self.program)):
            self.memory[i] = self.program[i]

    # addressing modes
    def ACC(self):
        pass
    def IMM(self):
        operand = self.memory[self.PC + 1]
        return operand
    def IMP(self):
        pass
    def REL(self):
        pass
    def ABS(self):
        pass
    def ABX(self):
        pass
    def ABY(self):
        pass
    def IND(self):
        pass
    def INX(self):
        pass
    def INY(self):
        pass
    def ZRO(self):
        pass
    def ZRX(self):
        pass
    def ZRY(self):
        pass



    def LDA(self, operand, cycles): # Load A with a value
        self.A = self.memory[self.PC + 1] & 0xFF
        self.PC += 2


    opcodes = {
        0xA9: (LDA, IMM, 2),
    }

    def execute(self):

        opcode = self.memory[self.PC]

        try:

            func, addm, cycles = self.opcodes[opcode]
            operand = addm(self)
            print("operand",operand)
            func(self, operand, cycles)
            time.sleep((cycles/10))

        except KeyError:

            print("invalid opcode in use:", hex(self.memory[self.PC]))
            exit()


    def PRINT_VALUES(self):
        print("A:",self.A)
        print("X:",self.X)
        print("Y:",self.Y)
        print("PC:",self.PC)
        print("SP:",self.SP)

    def print_memory(self):
        print(self.memory)

cpu = CPU()
cpu.LOAD_ROM()
cpu.print_memory()

while True:
    cpu.execute()
    cpu.PRINT_VALUES()
    time.sleep(2)
