import os
#ALU IN PYTHON

MAX_EXEC = 1000

cpu = {
    "FLAG": 0,
    "RES": 0,
    "PC": 0,
    "A": 0,
    "B": 0,
}

ram = [0] * 256

program = []

#------------------

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def err(code_split):
    if len(code_split) != 3:
        print("err")
        return True
    return False

def reg_err(reg1, reg2):
    if reg1 not in cpu or reg2 not in cpu:
        print ("err reg")
        return True
    return False

#------------------

def STORE(register, value):
    cpu[register] = value

def SUM(reg1, reg2):
    return reg1 + reg2
    
def SUB(reg1, reg2):
    return reg1 - reg2
    
def MUL(reg1, reg2):
    return reg1 * reg2
    
def DIV(reg1, reg2):
    return reg1 / reg2
    
def MOV(reg1, reg2):
    cpu[reg2] = cpu[reg1]
    
def CMP(reg1, reg2):
    if cpu[reg2] == cpu[reg1]:
        cpu["FLAG"] = 1
    else:
        cpu["FLAG"] = 0
        
def INPUT(reg):
    usr_in = int(input(f'>>{reg}> '))
    cpu[reg] = usr_in
    
def PRINT(reg):
    print(cpu[reg])
    
def SAVE(reg, addr):
    ram[addr] = cpu[reg]
    
def LOAD(reg, addr):
    cpu[reg] = ram[addr]

#------------------

def exec(code):
            
        if code == "":
            return
            
        code_split = code.split()
        command = code_split[0]
            
        if command == "STORE":
            if err(code_split): return
            register = code_split[1]
            value = int(code_split[2])
            STORE(register, value)
            
        elif command == "SUM":
            if err(code_split): return
            reg1 = cpu[code_split[1]]
            reg2 = cpu[code_split[2]]            
            cpu['RES'] = SUM(reg1, reg2)
            
        elif command == "SUB":
            if err(code_split): return
            reg1 = cpu[code_split[1]]
            reg2 = cpu[code_split[2]]
            cpu['RES'] = SUB(reg1, reg2)
            
            
        elif command == "MUL":
            if err(code_split): return
            reg1 = cpu[code_split[1]]
            reg2 = cpu[code_split[2]]         
            cpu['RES'] = MUL(reg1, reg2)
            
        elif command == "DIV":
            if err(code_split): return
            reg1 = cpu[code_split[1]]
            reg2 = cpu[code_split[2]]            
            cpu['RES'] = DIV(reg1, reg2)
            
        elif command == "MOV":
            if err(code_split): return
            reg1 = code_split[1]
            reg2 = code_split[2]
            MOV(reg1, reg2)
            
        elif command == "CMP":
            if err(code_split): return
            reg1 = code_split[1]
            reg2 = code_split[2]
            CMP(reg1, reg2)
            
        elif command == "JMP":
            if len(code_split) != 2:
                print("err")
                return
            cpu["PC"] = int(code_split[1])
            
        elif command == "JE":
            if len(code_split) != 2:
                print("err")
                return
            if cpu["FLAG"] == 1:
                cpu["PC"] = int(code_split[1])
                
        elif command == "JNE":
            if len(code_split) != 2:
                print("err")
                return
            if cpu["FLAG"] == 0:
                cpu["PC"] = int(code_split[1])
                
        elif command == "INPUT":
            if len(code_split) != 2:
                print("err")
                return
            reg = code_split[1]
            INPUT(reg)
            
        elif command == "PRINT":
            if len(code_split) != 2:
                print("err")
                return
            reg = code_split[1]
            PRINT(reg)
            
        
            
        elif command == "RES":
            print(cpu['RES'])
            
        elif command == "SAVE":
            if err(code_split): return
            reg = code_split[1]
            addr = code_split[2]
            SAVE(reg, addr)
            
        elif command == "LOAD":
            if err(code_split): return
            reg = code_split[1]
            addr = code_split[2]
            LOAD(reg, addr)
           
        elif command == "MEM":
            print(ram)
           
def terminal():
    while True:
        code = input('>>> ').upper().replace(",","")
        
        if code == 'END':     
            return
            
        elif code == 'HELP':
            print("""
=== PYssembly Commands ===

STORE REG VALOR   - Armazena um valor em um registrador
SUM REG REG       - Soma dois registradores
SUB REG REG       - Subtrai dois registradores
MUL REG REG       - Multiplica dois registradores
DIV REG REG       - Divide dois registradores

MOV REG REG       - Copia valor entre registradores
CMP REG REG       - Compara dois registradores

JMP LINHA         - Salta para uma linha
JE LINHA          - Salta se FLAG = 1
JNE LINHA         - Salta se FLAG = 0

INPUT REG         - Lê valor do usuário
PRINT REG         - Exibe valor do registrador

SAVE REG ADDR     - Salva registrador na RAM
LOAD REG ADDR     - Carrega da RAM para registrador

CPU               - Exibe estado da CPU
MEM               - Exibe conteúdo da RAM

RUN               - Executa o programa
CLEAR             - Limpa o programa
CLR LINE          - Remove a última linha

SAVE PGM          - Salva programa em arquivo
LOAD PGM          - Carrega programa de arquivo

END               - Fecha o PYssembly

==========================
""")
            
        elif code == "CPU":
            print(cpu)
            
        elif code == "MEM":
            print(ram)
            
        elif code == "RUN":
            cpu["PC"] = 0
            n_exec = 0
            
            while cpu["PC"] < len(program):
                n_exec += 1
                
                if n_exec > MAX_EXEC:
                    print("break: n exec exceed")
                    break
                    
                linha = program[cpu["PC"]]
                last_pc = cpu["PC"]    
                exec(linha)
                
                if cpu["PC"] == last_pc:
                    cpu["PC"] += 1
                    
        elif code == "CLEAR":
            program.clear()
            
        elif code == "CLR LINE":
            if program:
                program.pop()
                scr_show_code()
                
        elif code == "SAVE PGM":
            name = input("PGM name >>> ")
            with open(f"{name}.txt", "w", encoding = "utf-8") as file:
                for linha in program:
                    file.write(linha + "\n")
            print('PGM Saved!')
            
        elif code == "LOAD PGM":
            print(os.getcwd())
            print(os.listdir())
            name = input("PGM name >>> ")        
            with open(f"{name}.txt", "r", encoding="utf-8") as file:
                program.clear()        
                for linha in file:
                    program.append(linha.strip())        
            scr_show_code()
            print("PGM Loaded!")
                   
        else:
            program.append(code)
            scr_show_code()
   
def scr_show_code():
    cls()
    for i, linha in enumerate(program):
        print(f"{i}: {linha}")
                  
def startup():
      print("========== PYasm ==========")
      print("Type 'HELP' to see commands  ")
                  
startup()
terminal()