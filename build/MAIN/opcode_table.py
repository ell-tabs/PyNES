from . import instr_set as op
from . import addressing_modes as am

opcodes = {
        # LDA
        0xA9: (op.LDA, am.IMM, 2, 2),
        0xAD: (op.LDA, am.ABS, 4, 3),

        # LDX
        0xA2: (op.LDX, am.IMM, 2, 3),
        0xAE: (op.LDX, am.ABS, 2, 3),


        # LDY
        0xA0: (op.LDX, am.IMM, 2, 3),
        0xAC: (op.LDX, am.ABS, 2, 3),

        # STA
        # STX
        # STY

        # BRK
        0x00: (op.BRK, am.IMP, 1, 7)

    }