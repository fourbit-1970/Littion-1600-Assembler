from instructions import ebs_1601_instructions

def calculate_hex_output(opcode, hex_value_str, operand_str, line_number):
    """Calculates the final hex output based on the opcode and operands."""
    base_hex_str = hex_value_str.split('+')[0]
    base_hex = int(base_hex_str, 16)
    suffix = hex_value_str.split('+')[1] if '+' in hex_value_str else None
    timing = ebs_1601_instructions[opcode]['timing']
    if suffix is None:
        return hex(base_hex), timing

    if operand_str is None:
        print(f"warning: line {line_number}: '{hex_value_str.split('+')[0]}' requires an operand")
        return hex(base_hex), timing

    if operand_str.startswith('$'):
        operand_value = int(operand_str[1:], 16)
    else:
        try:
            operand_value = int(operand_str, 16)
        except ValueError:
            print(f"warning: line {line_number}: '{operand_str}' is not a valid operand")
            return hex(base_hex), timing

    match suffix:
        case 'M':
            hex_output = base_hex + operand_value
        case 'N':
            hex_output = base_hex + operand_value
        case 'X':
            hex_output = base_hex + operand_value
        case 'D':
            hex_output = base_hex + operand_value
        case 'C':
            hex_output = base_hex + operand_value
        case 'S':
            hex_output = base_hex + operand_value
        case _:
            print(f"warning: line {line_number}: '{suffix}' is not a valid suffix")
            hex_output = base_hex
    return hex(hex_output), timing


def calculate_binary_output(hex_outputs, next_address, opcodes, line_number):
    """Calculates the 40-bit binary output.

    Args:
        hex_outputs: A list of hex outputs for the opcodes.
        next_address: The next address for the instruction word.
        opcodes: A list of opcodes.

    Returns:
        A 40-bit hex string.
    """
    if not hex_outputs:
        return None

    opcode_bits = ""
    # Iterate through the hex outputs in reverse order to place them correctly.
    for i, hex_output in enumerate(hex_outputs):
        if hex_output is None:
            # Pad with 16 zeros if there is no hex output.
            opcode_bits = "0000000000000000" + opcode_bits
        else:
            hex_value = int(hex_output, 16)
            opcode_size = ebs_1601_instructions[opcodes[i]]['size']
            if opcode_size == 16:
                # Pad 16-bit opcodes to 16 bits.
                opcode_bits = bin(hex_value)[2:].zfill(16) + opcode_bits
            elif opcode_size == 8:
                # Pad 8-bit opcodes to 8 bits.
                opcode_bits = bin(hex_value)[2:].zfill(8) + opcode_bits
            else:
                print(f"warning: line {line_number}: '{opcodes[i]}' is not a valid opcode size")
                opcode_bits = "0000000000000000" + opcode_bits

    # Pad the opcode bits to 32 bits.
    opcode_bits = opcode_bits.rjust(32, '0')
    opcode_bits = opcode_bits[:32]

    # Convert the next address to binary.
    if next_address.startswith('$'):
        next_address_value = int(next_address[1:], 16)
    else:
        try:
            next_address_value = int(next_address)
        except ValueError:
            print(f"warning: line {line_number}: '{next_address}' is not a valid address")
            next_address_value = 0

    address_bits = bin(next_address_value)[2:].zfill(8)
    # Combine the address bits and opcode bits.
    binary_output = address_bits + opcode_bits
    # Convert the binary output to hex.
    hex_output = hex(int(binary_output, 2))[2:].zfill(10).upper()
    return hex_output


def format_parsed_output(parsed_lines, label_dict):
    """Formats the parsed output for better readability."""
    print("{:<5} {:<10} {:<20} {:<18} {:<15} {:<15} {:<10}".format(
        "Line", "Label", "Opcodes", "Operands", "Next Addr", "Hex Output", "Timing"
    ))
    for line in parsed_lines:
        line_number, label, opcodes, operands, comment, hex_outputs, timings, binary_output, next_address = line
        opcodes_str = ", ".join(opcodes) if opcodes else ""
        operands_str = ", ".join([str(op) if op is not None else "" for op in operands]) if operands else ""
        hex_outputs_str = ", ".join([str(hex_op) if hex_op is not None else "" for hex_op in hex_outputs]) if hex_outputs else ""
        timings_str = ", ".join([str(time) if time is not None else "" for time in timings]) if timings else ""
        print(
            "{:<5} {:<10} {:<20} {:<18} {:<15} {:<15} {:<10}".format(
                line_number,
                label if label is not None else "",
                opcodes_str,
                operands_str,
                next_address if next_address is not None else "",
                binary_output if binary_output is not None else "",
                timings_str,
            )
        )
    print("\nLabels:")
    for label, value in label_dict.items():
        print(f"{label}: {value}")
