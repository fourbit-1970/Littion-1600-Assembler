import re
import argparse
from instructions import ebs_1601_instructions
from assembler_utils import calculate_hex_output, calculate_binary_output, format_parsed_output
from object_file_generator import generate_object_file, generate_listing_file

def parse_assembly_line(line, line_number, label_dict):
    """Parses a single line of assembly code.

    Args:
        line: A line of assembly code.
        line_number: The line number of the assembly code.
        label_dict: A dictionary to store labels and their values.

    Returns:
        A list containing the label, opcodes, operands, comment, hex outputs, timings, binary output, and next address.
    """
    line = line.strip()
    if not line:
        return [line_number, None, [], [], None, [], None, None, None]  # Return for empty line

    comment = None
    parts = line.split(';', 1)
    code_part = parts[0].strip()

    if len(parts) > 1:
        comment = parts[1].strip()
    if not code_part:
        return [line_number, None, [], [], comment, [], None, None, None]

    label = None
    opcodes = []
    operands = []
    hex_outputs = []
    timings = []
    total_opcode_bits = 0
    binary_output = None
    next_address = None

    # Check for a label.
    label_match = re.match(r'^(\$?[0-9a-fA-F]+):\s*(.*)$', code_part)
    if label_match:
        # Extract the label from the first capturing group.
        label_str = label_match.group(1)
        # Remove the label and colon from the code part.
        code_part = label_match.group(2).strip()
        # Convert decimal labels to hex.
        if label_str.startswith('$'):
            label = label_str
        else:
            label_int = int(label_str)
            label = f"${label_int:02X}"
        # Store the label and its value in the dictionary.
        label_dict[label] = label
    else:
        print(f"error: line {line_number}: missing or invalid label address")

    # Check for a next address.
    instruction_parts = re.split(r'\s+', code_part)
    if instruction_parts and instruction_parts[-1].startswith('$'):
        # Extract the next address from the end of the instruction parts.
        next_address = instruction_parts.pop()

    i = 0
    # Parse the opcodes and operands.
    while i < len(instruction_parts):
        part = instruction_parts[i].upper()
        operand = None
        # Check for an operand.
        if '+' in part:
            # Split the opcode and operand.
            opcode, operand = part.split('+', 1)
        else:
            opcode = part
        
        if opcode in ebs_1601_instructions:
            opcodes.append(opcode)
            hex_value_str = ebs_1601_instructions[opcode]['hex']
            opcode_size = ebs_1601_instructions[opcode]['size']
            total_opcode_bits += opcode_size
            
            if '+' in hex_value_str:
                if operand is None:
                    if i + 1 < len(instruction_parts):
                        operand = instruction_parts[i + 1]
                        i += 1
            operands.append(operand)
            hex_output, timing = calculate_hex_output(opcode, hex_value_str, operand, line_number)
            hex_outputs.append(hex_output)
            timings.append(timing)
        else:
            print(f"warning: line {line_number}: '{opcode}' is not a valid opcode")
            opcodes.append("INVALID")
            operands.append(None)
            hex_outputs.append(None)
            timings.append(None)
        i += 1
    if total_opcode_bits > 32:
        print(f"warning: line {line_number}: too many opcodes on line, total opcode bits: {total_opcode_bits}")
    if label is not None:
        binary_output = calculate_binary_output(hex_outputs, next_address, opcodes, line_number)

    return [line_number, label, opcodes, operands, comment, hex_outputs, timings, binary_output, next_address]

def read_and_parse_assembly(filename):
    """Reads an assembly file and parses each line."""
    parsed_lines = []
    label_dict = {}
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    parsed_lines.append(parse_assembly_line(line, line_num, label_dict))
                except Exception as e:
                    print(f"Error parsing line {line_num}: {line.strip()}")
                    print(f"Error details: {e}")
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None, None  # Return None for both if file not found
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

    # Calculate sequential next addresses if not provided.
    last_label = None
    for line in reversed(parsed_lines):
        line_number, label, opcodes, operands, comment, hex_outputs, timings, binary_output, next_address = line
        if label is not None:
            if next_address is None:
                if last_label is not None:
                    next_address_int = int(last_label[1:], 16) +1
                    next_address = f"${next_address_int:02X}"
                    line[8] = next_address
                else:
                    next_address = "$01"
                    line[8] = next_address
            last_label = label

    return parsed_lines, label_dict

# Assembler for the Littion 1600 computer.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Assemble Littion assembly code.")
    parser.add_argument("filename", help="The assembly filename (.asm)")
    parser.add_argument("-s", "--suppress", action="store_true", help="Suppress console output")
    args = parser.parse_args()

    filename = args.filename
    suppress_output = args.suppress

    parsed_output, label_dict = read_and_parse_assembly(filename)
    if parsed_output:  # Check if parsing was successful
        if not suppress_output:
            format_parsed_output(parsed_output, label_dict)
        generate_object_file(parsed_output, filename)
        generate_listing_file(parsed_output, filename)
