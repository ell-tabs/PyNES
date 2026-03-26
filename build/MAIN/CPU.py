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

        self.program = [
    0xA9, 0x10,       # LDA #$10
    0xA9, 0x20,       # LDA #$20
    0xAD, 0x0A, 0x00, # LDA $000A
    0xAD, 0x0B, 0x00, # LDA $000B
    0xA2, 0x05,       # LDX #$05      ; Load 5 into X
    0xAE, 0x0C, 0x00, # LDX $000C     ; Load value at memory[0x000C] into X
    0xA0, 0x03,       # LDY #$03      ; Load 3 into Y
    0xAC, 0x0D, 0x00, # LDY $000D     ; Load value at memory[0x000D] into Y
    0x55,             # memory[0x000A] = 0x55
    0xAA,             # memory[0x000B] = 0xAA
    0x00              # BRK
]

    def execute(self):

        opcode = self.memory[self.PC]

        try:

            func, addm, cycles, bytes = opcodes.opcodes[opcode]
            operand = addm(self)
            print("operand",operand)
            func(self, operand, cycles, bytes)
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

    def LOAD_ROM(self): # testing binary stuff  
        for i in range(len(self.program)):
            self.memory[i] = self.program[i] 