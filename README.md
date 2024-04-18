Contributors Names and Roll No.

1. Om Kumar Gupta(2023362)
2. Priyanshu Rana(2023407)
3. Nitin Kumar(2023358)

About the assembler-

Instruction Sets: The script defines several dictionaries (opcodes, resistor, func7, func3) and lists (r_types, i_types, s_types, b_types, u_types, j_types) to store instruction opcodes, register names, and other necessary information for different types of instructions.

Format Functions: There are several format functions (format_r, format_i, format_s, format_b, format_j, format_u) defined in the script, each responsible for formatting a specific type of instruction into its corresponding machine code representation. These functions take a string representing an assembly instruction as input and return the corresponding machine code string.

Main Execution: The script reads input assembly instructions from a file specified as the second-to-last command-line argument (sys.argv[-2]). It then iterates over each line, splits it into individual components, determines the type of instruction, and calls the appropriate format function to convert it to machine code. The formatted machine code is then written to an output file specified as the last command-line argument (sys.argv[-1]).

Command-Line Arguments: The script uses the sys.argv list to access command-line arguments. The second-to-last argument is assumed to be the input file containing assembly instructions, and the last argument is assumed to be the output file where the formatted machine code will be written.

About the simulator-

Memory Class: This class represents the memory of the simulated RISC-V processor. It has methods to read from and write to memory locations.

Registers Class: This class represents the registers of the simulated RISC-V processor. It has methods to read from and write to individual registers.

RISCV_Simulator Class: This is the main class representing the RISC-V simulator. It has the following attributes:
      registers: An instance of the Registers class to manage the processor's registers.
      memory: An instance of the Memory class to manage the processor's memory.
      pc: Program Counter, which keeps track of the address of the currently executing instruction.
It also has the following methods:
      execute_instruction: This method is responsible for executing individual RISC-V instructions.
      simulate: This method reads instructions from a file, executes them one by one, and then prints out the final state of the registers and memory.
      print_registers and print_memory: These methods print out the current values of registers and the contents of memory, respectively.
      
Main Block: This block checks if the script is being run directly (if __name__ == "__main__":). If so, it checks whether the correct number of command-line arguments are provided. Then it creates an instance of the RISCV_Simulator class and calls the simulate method with the input file provided as a command-line argument
