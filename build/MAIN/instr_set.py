import time

def LDA(self, operand, cycles, bytes): # Load A with a value
        self.A = operand
        self.PC += bytes

def LDX(self, operand, cycles, bytes): # Load X with a value
        self.X = operand
        self.PC += bytes

def LDY(self, operand, cycles, bytes): # Load Y with a value
        self.Y = operand
        self.PC += bytes

def BRK(self, operand, cycles, bytes): # End Program
        exit()