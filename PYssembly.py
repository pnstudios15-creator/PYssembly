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
            
        elif command == "CPU":
            print(cpu)
            
        elif command == "RES":
            print(cpu['RES'])
           
           
def terminal():
    while True:
        code = input('>>> ').upper().replace(",","")
        
        if code == 'END':     
            return
            
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
            
        else:
            program.append(code)
            scr_show_code()
        
   
def scr_show_code():
    cls()
    for i, linha in enumerate(program):
        print(f"{i}: {linha}")
                  
terminal()