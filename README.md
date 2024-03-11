Contributors Names and Roll No.

1. Om Kumar Gupta(2023362)
2. Priyanshu Rana(2023407)
3. Nitin Kumar(2023358)

About the assembler-

Instruction Sets: The script defines several dictionaries (opcodes, resistor, func7, func3) and lists (r_types, i_types, s_types, b_types, u_types, j_types) to store instruction opcodes, register names, and other necessary information for different types of instructions.

Format Functions: There are several format functions (format_r, format_i, format_s, format_b, format_j, format_u) defined in the script, each responsible for formatting a specific type of instruction into its corresponding machine code representation. These functions take a string representing an assembly instruction as input and return the corresponding machine code string.

Main Execution: The script reads input assembly instructions from a file specified as the second-to-last command-line argument (sys.argv[-2]). It then iterates over each line, splits it into individual components, determines the type of instruction, and calls the appropriate format function to convert it to machine code. The formatted machine code is then written to an output file specified as the last command-line argument (sys.argv[-1]).

Command-Line Arguments: The script uses the sys.argv list to access command-line arguments. The second-to-last argument is assumed to be the input file containing assembly instructions, and the last argument is assumed to be the output file where the formatted machine code will be written.
