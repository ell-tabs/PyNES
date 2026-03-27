from . import instr_set as op
from . import addressing_modes as am

opcodes = {
        # INSTRUCTION, ADDR MODE, BYTES, CYCLES

        # JMP

        # JSR

        # LDA 
        0xA9: (op.LDA, am.IMM, 2, 2), 
        0xAD: (op.LDA, am.ABS, 3, 4),

        # LDX
        0xA2: (op.LDX, am.IMM, 2, 2),
        0xAE: (op.LDX, am.ABS, 3, 4),


        # LDY
        0xA0: (op.LDY, am.IMM, 2, 2),
        0xAC: (op.LDY, am.ABS, 3, 4),

        # STA

        # STX

        # STY

        #ADC
        0x69: (op.ADC, am.IMM, 2, 2),
        0x6D: (op.ADC, am.ABS, 3, 4),
        0x65: (op.ADC, am.ZPG, 2, 3),

        #AND

        # BRK
        0x00: (op.BRK, am.IMP, 1, 7),

        # NOP
        0xEA: (),

        # INC
        0xE6: (op.INC, am.ZPG, 2, 5),
        0xEE: (op.INC, am.ABS, 3, 6),

        # INX
        0xE8: (op.INX, am.IMP, 1, 2),

        # INY
        0xC8: (op.INY, am.IMP, 1, 2),

        # DEC
        0xC6: (op.DEC, am.ZPG, 2, 5),
        0xCE: (op.DEC, am.ABS, 3, 6),

        # DEX
        0xCA: (op.DEX, am.IMP, 1, 2),

        # DEY
        0x88: (op.DEY, am.IMP, 1, 2),

    }