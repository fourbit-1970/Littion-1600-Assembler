
# Timing Abbreviations:
# ma: Memory Access Time (drum track and sector, 12-bit number)
# n: Shift Count (0-39)
# sa: Scratchpad Access Time
# za: Scratchpad Address 000 (sector 0) Access Time
# alt: Alternate timing (usually a faster timing under certain conditions)
# M: storage Address 000 to FFF in hex
# S: scratchpad sector address 0 to 7
# N: shift count -1
# D: device select code (8bits maximum)
# C: character (8bits)
# A: accumulator register
# I: instruction register
# K: carry flip-flop (F14) bit

ebs_1601_instructions = {
    'AC': {'hex': 'D000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'AD': {'hex': '9000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'AK': {'hex': '08', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'AS': {'hex': '76C0', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'AST': {'hex': '74C0', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'BI': {'hex': '0F', 'type': '8-bit', 'timing': ['10', 'za'], 'size': 8},
    'BLD': {'hex': '4200+N', 'type': '16-bit', 'timing': ['8', 'n', 'za'], 'size': 16},
    'BLDK': {'hex': '4280+N', 'type': '16-bit', 'timing': ['8', 'n', 'za'], 'size': 16},
    'BLDS': {'hex': '4300', 'type': '16-bit', 'timing': ['5'], 'size': 16},
    'BLDSK': {'hex': '4380', 'type': '16-bit', 'timing': ['5'], 'size': 16},
    'BLS': {'hex': '4000+N', 'type': '16-bit', 'timing': ['3', 'n'], 'size': 16},
    'BLSK': {'hex': '4080+N', 'type': '16-bit', 'timing': ['3', 'n'], 'size': 16},
    'BLSS': {'hex': '4100', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'BLSSK': {'hex': '4180', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'BRD': {'hex': '4A00+N', 'type': '16-bit', 'timing': ['8', 'n', 'za'], 'size': 16},
    'BRDK': {'hex': '4A80+N', 'type': '16-bit', 'timing': ['8', 'n', 'za'], 'size': 16},
    'BRDS': {'hex': '4800', 'type': '16-bit', 'timing': ['5'], 'size': 16},
    'BRDSK': {'hex': '4B80', 'type': '16-bit', 'timing': ['5'], 'size': 16},
    'BRS': {'hex': '4800+N', 'type': '16-bit', 'timing': ['3', 'n'], 'size': 16},
    'BRSK': {'hex': '4880+N', 'type': '16-bit', 'timing': ['3', 'n'], 'size': 16},
    'BRSS': {'hex': '4900', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'BRSSK': {'hex': '4980', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'CA': {'hex': '8000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'CIE': {'hex': '5840', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'CIEP': {'hex': '5C40', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'CIO': {'hex': '5800', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'CIOP': {'hex': '5C00', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'CL': {'hex': '09', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'CM': {'hex': '0B', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'DLD': {'hex': '6200+N', 'type': '16-bit', 'timing': ['8', 'n', 'za'], 'size': 16},
    'DLDC': {'hex': '6280+N', 'type': '16-bit', 'timing': ['8', 'n', 'za'], 'size': 16},
    'DLDS': {'hex': '6300', 'type': '16-bit', 'timing': ['5'], 'size': 16},
    'DLDSC': {'hex': '6380', 'type': '16-bit', 'timing': ['5'], 'size': 16},
    'DLS': {'hex': '6000+N', 'type': '16-bit', 'timing': ['3', 'n'], 'size': 16},
    'DLSC': {'hex': '6080+N', 'type': '16-bit', 'timing': ['3', 'n'], 'size': 16},
    'DLSS': {'hex': '6100', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'DLSSC': {'hex': '6180', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'DRD': {'hex': '6A00+N', 'type': '16-bit', 'timing': ['16', 'n', 'za'], 'size': 16},
    'DRS': {'hex': '6800+N', 'type': '16-bit', 'timing': ['2', 'n'], 'size': 16},
    'HH': {'hex': '00+X', 'type': '8-bit', 'timing': ['–'], 'size': 8},
    'IS': {'hex': '7E00+D', 'type': '16-bit', 'timing': ['4'], 'size': 16},
    'IST': {'hex': '7C00+D', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'JA': {'hex': '0D', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'JC': {'hex': 'F000+M', 'type': '16-bit', 'timing': ['4', 'ma', 'alt'], 'size': 16},
    'JM': {'hex': 'C000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'JU': {'hex': 'E000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'LA': {'hex': '18+S', 'type': '8-bit', 'timing': ['3', 'sa'], 'size': 8},
    'LI': {'hex': '8000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'NN': {'hex': '0A', 'type': '8-bit', 'timing': ['1'], 'size': 8},
    'OA': {'hex': '70C0', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'OAE': {'hex': '7040', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'OAO': {'hex': '7000', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'OI': {'hex': '7800+C', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'RK': {'hex': '13', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'RS': {'hex': '5080', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'SI': {'hex': '5000', 'type': '16-bit', 'timing': ['4', 'alt'], 'size': 16},
    'SK': {'hex': '10', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'ST': {'hex': 'B000+M', 'type': '16-bit', 'timing': ['4', 'ma'], 'size': 16},
    'TE': {'hex': '30+S', 'type': '8-bit', 'timing': ['3', 'sa'], 'size': 8},
    'TG': {'hex': '38+S', 'type': '8-bit', 'timing': ['3', 'sa'], 'size': 8},
    'TH': {'hex': '12', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'TN': {'hex': '12', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'TP': {'hex': '14', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'TZ': {'hex': '11', 'type': '8-bit', 'timing': ['3'], 'size': 8},
    'XC': {'hex': '20+S', 'type': '8-bit', 'timing': ['3', 'sa'], 'size': 8},
    'XT': {'hex': '28+S', 'type': '8-bit', 'timing': ['3', 'sa'], 'size': 8}
}
