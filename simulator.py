import sys

class Memory:
    def _init_(self, size):
        self.size = size
        self.data = [0] * size

    def read(self, address):
        if 0 <= address < self.size:
            return self.data[address]
        else:
            raise ValueError("Memory address out of bounds")

    def write(self, address, value):
        if 0 <= address < self.size:
            self.data[address] = value
        else:
            raise ValueError("Memory address out of bounds")

class Registers:
    def _init_(self, size):
        self.size = size
        self.data = [0] * size

    def read(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise ValueError("Register index out of bounds")

    def write(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise ValueError("Register index out of bounds")

class RISCV_Simulator:
    def _init_(self):
        self.registers = Registers(32)
        self.memory = Memory(128)
        self.pc = 0  

    def execute_instruction(self, instruction):
        opcode = instruction[25:32]
        

    def simulate(self, file_path):
        with open(file_path, 'r') as file:
            instructions = file.readlines()

        for instruction in instructions:
            instruction = instruction.strip()
            if len(instruction) != 32:
                print("Invalid instruction length:", instruction)
                continue

            self.execute_instruction(instruction)

        self.print_registers()
        self.print_memory()

    def print_registers(self):
        print("Register Values:")
        for i in range(32):
            print(f"x{i}: {self.registers.read(i)}")

    def print_memory(self):
        print("Memory Contents:")
        for i in range(128):
            print(f"Address {i}: {self.memory.read(i)}")

if __name__ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python program.py input_file output_file")
        sys.exit(1)

    input_file, output_file = sys.argv[-2], sys.argv[-1]
    riscv = RISCV_Simulator()
    riscv.simulate(input_file)