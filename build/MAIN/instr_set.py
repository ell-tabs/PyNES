import time

def JMP(self, operand, bytes, cycles):
        pass

def JSR(self, operand, bytes, cycles):
        pass

def LDA(self, operand, bytes, cycles): # Load A with a value
        self.A = operand
        self.PC += bytes

def LDX(self, operand, bytes, cycles): # Load X with a value
        self.X = operand
        self.PC += bytes

def LDY(self, operand, bytes, cycles): # Load Y with a value
        self.Y = operand
        self.PC += bytes

def STA(self, operand, bytes, cycles):
        pass

def STX(self, operand, bytes, cycles):
        pass

def STY(self, operand, bytes, cycles):
        pass

def ADC(self, operand, bytes, cycles): # Adds the carry flag and memory to the accumulator
        self.A = self.A + self.memory[operand] + self.C & 0xFF
        self.PC += bytes

def AND(self, operand, bytes, cycles): # Performs AND 
        self.Y = operand
        self.PC += bytes

def BRK(self, operand, bytes, cycles): # End Program
        exit()

def NOP(self, operand, bytes, cycles): # basically a wait
        time.sleep(0.1)
        self.PC += bytes
        pass

def INC(self, operand, bytes, cycles):
        self.memory[operand] += 1
        self.PC += bytes

def INX(self, operand, bytes, cycles):
        self.X += 1
        self.PC += bytes

def INY(self, operand, bytes, cycles):
        self.Y += 1
        self.PC += bytes

def DEC(self, operand, bytes, cycles):
        self.memory[operand] -= 1
        self.PC += bytes

def DEX(self, operand, bytes, cycles):
        self.X -= 1
        self.PC += bytes

def DEY(self, operand, bytes, cycles):
        self.Y -= 1
        self.PC += bytes