# addressing modes
from . import CPU

def ACC(self):
        pass
def IMM(self):
    return self.memory[self.PC + 1]
def IMP(self):
        pass
def REL(self):
        pass
def ABS(self):
    low = self.memory[self.PC + 1]
    high = self.memory[self.PC + 2]
    a = (high << 8) | low
    return self.memory[a]

def ABX(self):
    low = self.memory[self.PC + 1]
    high = self.memory[self.PC + 2]
    a = (high << 8) | low
    return self.memory[a] +  CPU.cpu.X

def ABY(self):
    low = self.memory[self.PC + 1]
    high = self.memory[self.PC + 2]
    a = (high << 8) | low
    return self.memory[a] +  CPU.cpu.Y

def IND(self):
        pass
def INX(self):
        pass
def INY(self):
        pass
def ZPG(self):
       return self.memory[[self.PC + 1] & 0xFF]
def ZPX(self):
        pass
def ZPY(self):
        pass
