import time
from . import opcode_table as opcodes

class CPU:
    def __init__(self):

        # 6502 registers
        self.A = 0
        self.X = 0
        self.Y = 0
        self.PC = 0
        self.SP = 0

        self.C = 0
        self.Z = 0
        self.I = 0
        self.D = 0
        self.V = 0
        self.N = 0

        self.B = 0
        self.O = 1

        self.memory = [0] * 64 * 1024

    program = [
    0xA9, 0x10,       # LDA #$10
    0xA9, 0x20,       # LDA #$20
    0xAD, 0x01, 0x00, # LDA $0001
    0xAD, 0x0B, 0x00, # LDA $000B
    0xA2, 0x05,       # LDX #$05      ; Load 5 into X
    0xAE, 0x0C, 0x00, # LDX $000C     ; Load value at memory[0x000C] into X
    0xA0, 0x03,       # LDY #$03      ; Load 3 into Y
    0xAC, 0x0D, 0x00, # LDY $000D     ; Load value at memory[0x000D] into Y
    0x69, 100,         # ADC #$64      ; Add value to A and store in A 
    0x6D, 0x01, 0x00, #ADC ABS $01
    0x65, 0x08,
    0xE6, 3,
    0xCE, 0x0B, 0x00,
    0xC8, 0xCA,
    0x00,             # BRK
    0xAA,             # memory[0x000B] = 0xAA
    ]

    def execute(self):
        try:
            opcode = self.memory[self.PC]
            func, addm, bytes, cycles = opcodes.opcodes[opcode]
            operand = addm(self)
            print(func.__name__, addm.__name__, operand)
            func(self, operand, bytes, cycles)

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
        print(self.memory[:108])

    def LOAD_ROM(self): # testing binary stuff  
        for i in range(len(self.program)):
            self.memory[i] = self.program[i] 