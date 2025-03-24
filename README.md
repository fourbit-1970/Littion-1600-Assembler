# Littion 1601 Assembler

## Project Description

This is a personal project to create an assembler for the Littion 1601 computer. The Litton 1600 is a drum-base 40-bit serial computer from the 1960s. This assembler will be used in the process of creating testing programs for the gate-accurate recreation of the Littion 1600 logic.

The assembler takes assembly code as input and generates an object file (`.obj`) that can be loaded into a Littion 1601 simulator. It also generates a listing file (`.lst`) for debugging purposes.

## Features

*   Parses Littion 1600 series assembly code.
*   Handles labels (hexadecimal and decimal).
*   Handles opcodes, operands, and comments.
*   Handles 8-bit and 16-bit opcodes.
*   Calculates the correct hex output.
*   Places opcodes in the correct order.
*   Calculates the next address (either provided or sequential).
*   Pads with `NN` (NOP) instructions.
*   Generates the correct 40-bit hex output.
*   Formats the output nicely and in a printer-friendly way.
*   Reports warnings and errors.
*   Generates object files (`.obj`).
*   Generates listing files (`.lst`).
*   Accepts command-line arguments.
*   Suppresses console output (optional).

## `.asm` File Format

The assembly file format is as follows:

*   **Labels:** Labels are used to specify the address of an instruction word. They can be either hexadecimal (starting with `$`, e.g., `$0A:`) or decimal (e.g., `10:`).
*   **Opcodes:** Opcodes are the instructions (e.g., `AC`, `RK`, `JC`).
*   **Operands:** Operands are the data used by the opcodes (e.g., `14A`, `fff`).
*   **Comments:** Comments start with a semicolon (`;`).
*   **Next Address:** The next address is optional and is specified at the end of the line, starting with `$` (e.g., `$01`). If not specified, the assembler will calculate the next sequential address.

**Example: assembly**

__Location        Symbolic Code   Partial Address__
$000:         RK TP CIE             $01             ; Test case from manual
$001:         AC+14A  JC+fff        $02             ; Add with Cary and Jump conditional
$020:         LA+7  NN  RK  SK      $03             ; Test case with 4 opcodes

## Command-Line Options

    python Assembler.py <filename.asm> [-s]

*   <filename.asm>: The name of the assembly file to assemble. This is a required argument.
*   -s or --suppress: An optional flag to suppress the formatted output to the console.

## output Files

*   obj: An object file containing the assembled code in the format address:instruction (e.g., $00:01584000140013). This file can be loaded into the Littion 1601 simulator.
*   lst: A listing file containing the formatted output that is normally displayed on the console. This file is useful for debugging.

## Error Handling

The assembler reports errors and warnings to the console. Errors will prevent the generation of the object and listing files. Warnings will not prevent the generation of the files.

## Future Enhancements

* Command timing-based next address optimization (calculate sum of command execution time to optomize next address).
* Add Assembler directives. 
* Improve listing output (add command timming information, modify format for readability, etc)

## License

This project is licensed under the MIT License.

## Additional Information

* [Original Litton 1600 Technical Reference Manual](https://bitsavers.org/pdf/litton/Litton1600_TechnicalRefMan.pdf)

## Acknowledgments

* Special thanks to David Lovett (Usagi Electric) for discovering this virtually unknown minicomputer.
