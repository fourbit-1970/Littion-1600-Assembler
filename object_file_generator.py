def generate_object_file(parsed_lines, filename):
    """Generates an object file from the parsed assembly lines.

    Args:
        parsed_lines: A list of parsed assembly lines.
        filename: The original assembly filename.
    """
    obj_filename = filename.replace(".asm", ".obj")
    try:
        with open(obj_filename, 'w') as obj_file:
            for line in parsed_lines:
                line_number, label, opcodes, operands, comment, hex_outputs, timings, binary_output, next_address = line
                if label is not None and binary_output is not None:
                    obj_file.write(f"{label.upper()}:{binary_output.upper()}\n")
    except Exception as e:
        print(f"Error generating object file: {e}")
    print(f"Object file '{obj_filename}' generated successfully.")

def generate_listing_file(parsed_lines, filename):
    """Generates a listing file from the parsed assembly lines.

    Args:
        parsed_lines: A list of parsed assembly lines.
        filename: The original assembly filename.
    """
    lst_filename = filename.replace(".asm", ".lst")
    try:
        with open(lst_filename, 'w') as lst_file:
            lst_file.write("{:<5} {:<10} {:<20} {:<18} {:<15} {:<15} {:<10}\n".format(
                "Line", "Label", "Opcodes", "Operands", "Next Addr", "Hex Output", "Timing"
            ))
            for line in parsed_lines:
                line_number, label, opcodes, operands, comment, hex_outputs, timings, binary_output, next_address = line
                opcodes_str = ", ".join(opcodes) if opcodes else ""
                operands_str = ", ".join([str(op) if op is not None else "" for op in operands]) if operands else ""
                hex_outputs_str = ", ".join([str(hex_op) if hex_op is not None else "" for hex_op in hex_outputs]) if hex_outputs else ""
                timings_str = ", ".join([str(time) if time is not None else "" for time in timings]) if timings else ""
                lst_file.write(
                    "{:<5} {:<10} {:<20} {:<18} {:<15} {:<15} {:<10}\n".format(
                        line_number,
                        label if label is not None else "",
                        opcodes_str,
                        operands_str,
                        next_address if next_address is not None else "",
                        binary_output if binary_output is not None else "",
                        timings_str,
                    )
                )
    except Exception as e:
        print(f"Error generating listing file: {e}")
    print(f"Listing file '{lst_filename}' generated successfully.")
