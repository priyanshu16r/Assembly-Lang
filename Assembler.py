import sys

opcodes = {
  "add": "0110011",
  "sub": "0110011",
  "sll": "0110011",
  "slt": "0110011",
  "sltu": "0110011",
  "xor": "0110011",
  "srl": "0110011",
  "or": "0110011",
  "and": "0110011",
  "lw": "0000011",
  "addi": "0010011",
  "sltiu": "0010011",
  "jalr": "1100111",
  "sw": "0100011",
  "beq": "1100011",
  "bne": "1100011",
  "blt": "1100011",
  "bge": "1100011",
  "bltu": "1100011",
  "bgeu": "1100011",
  "lui": "0110111",
  "auipc": "0010111",
  "jal": "1101111",
}

resistor = {
  "zero": "00000",
  "ra": "00001",
  "sp": "00010",
  "gp": "00011",
  "tp": "00100",
  "t0": "00101",
  "t1": "00110",
  "t2": "00111",
  "s0": "01000",
  "fp": "01000",
  "s1": "01001",
  "a0": "01010",
  "a1": "01011",
  "a2": "01100",
  "a3": "01101",
  "a4": "01110",
  "a5": "01111",
  "a6": "10000",
  "a7": "10001",
  "s2": "10010",
  "s3": "10011",
  "s4": "10100",
  "s5": "10101",
  "s6": "10110",
  "s7": "10111",
  "s8": "11000",
  "s9": "11001",
  "s10": "11010",
  "s11": "11011",
  "t3": "11100",
  "t4": "11101",
  "t5": "11110",
  "t6": "11111"
}

func7={
    "add": "0000000",
    "sub": "0100000",
    "sll": "0000000",
    "slt": "0000000",
    "sltu": "0000000",
    "xor": "0000000",
    "srl": "0000000",
    "or": "0000000",
    "and": "0000000",
}

func3={
    "add": "000",
  "sub": "000",
  "sll": "001",
  "slt": "010",
  "sltu": "011",
  "xor": "100",
  "srl": "101",
  "or": "110",
  "and": "111",
  "lw": "010",
  "addi": "000",
  "sltiu": "011",
  "jalr": "000",
  "sw": "010",
  "beq": "000",
  "bne": "001",
  "blt": "100",
  "bge": "101",
  "bltu": "110",
  "bgeu": "111",
}

r_types=["add","sub","sll","slt","sltu","xor","srl","or","and"]
i_types=["lw","addi","sltiu","jalr"]
s_types=["sw"]
b_types=["beq","bne","blt","bge","bltu","bgeu"]
u_types=["lui","auipc"]
j_types=["jal"]


def format_r(str):
    l1=[i for i in str.split()]
    l2=[j for j in l1[1].split(",")]
    return func7[l1[0]]+resistor[l2[2]]+resistor[l2[1]]+func3[l1[0]]+resistor[l2[0]]+opcodes[l1[0]]+'\n'
  

def format_i(str):
        l1=[i for i in str.split()]
        if l1[0]=="lw":
            l2=[j for j in l1[1].split(",")]
            l3=[k for k in l2[1].split("(")]
            return bin(int(l3[0]))[2:].zfill(12)+resistor[l3[1][:-1]]+func3[l1[0]]+resistor[l2[0]]+opcodes[l1[0]]+'\n'
          
        else:
            l2=[j for j in l1[1].split(",")]
            if int(l2[2]) >= 0:
                binary = bin(int(l2[2]))[2:].zfill(12)
                
            else:
                positive_binary = bin(-int(l2[2]))[2:].zfill(12)
                inverted_binary = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
                inverted_decimal = int(inverted_binary, 2) + 1
                binary = bin(inverted_decimal)[2:].zfill(12)
                
            return binary+resistor[l2[1]]+func3[l1[0]]+resistor[l2[0]]+opcodes[l1[0]]+'\n'
            

def format_s(str):
    l1=[i for i in str.split()]
    l2=[j for j in l1[1].split(",")]
    l3=[k for k in l2[1].split("(")]
    if int(l3[0]) >= 0:
            c = bin(int(l3[0]))[2:].zfill(12)
           
    else:
        positive_binary = bin(-int(l3[0]))[2:].zfill(12)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        c = bin(inverted_decimal)[2:].zfill(12)
    return c[:7]+resistor[l2[0]]+resistor[l3[1][:-1]]+func3[l1[0]]+c[7:]+opcodes[l1[0]]+'\n'
    

def format_b(str):
    l1=[i for i in str.split()]
    l2=[j for j in l1[1].split(",")]
    c=bin(int(l2[2]))[2:].zfill(12)
    return c[:7]+resistor[l2[1]]+resistor[l2[0]]+func3[l1[0]]+c[7:]+opcodes[l1[0]]+'\n'
    


def format_j(str):
    l1=[i for i in str.split()]
    l2=[j for j in l1[1].split(",")]
    if int(l2[1]) >= 0:
        c = bin(int(l2[1]))[2:].zfill(20)
        
    else:
        positive_binary = bin(-int(l2[1]))[2:].zfill(20)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
        inverted_decimal = int(inverted_binary, 2) + 1
        c = bin(inverted_decimal)[2:].zfill(20)
    return c[8:19]+c[:9]+resistor[l2[0]]+opcodes[l1[0]]+'\n'
    

def format_u(str):
    l1=[i for i in str.split()]
    l2=[j for j in l1[1].split(",")]
    if int(l2[1])>=0:
        d='0'*20
    else:
        d='1'*20
    return d+resistor[l2[0]]+opcodes[l1[0]]+'\n'
    

with open(sys.argv[-2],'r') as file:
    with open(sys.argv[-1],'w') as file2:
        for line in file:
            line=line.strip()
            lst=[i for i in line.split()]
            if lst[0] in r_types:
                file2.write(format_r(line))
            elif lst[0] in i_types:
                file2.write(format_i(line))
            elif lst[0] in s_types:
                file2.write(format_s(line))
            elif lst[0] in u_types:
                file2.write(format_u(line))
            elif lst[0] in b_types:
                file2.write(format_b(line))
            elif lst[0] in j_types:
                file2.write(format_j(line))

 