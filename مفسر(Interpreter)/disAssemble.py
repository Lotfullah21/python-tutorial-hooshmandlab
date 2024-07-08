import dis
def total():
    a = 4
    b = 2
    c = a+b
    return c

# Print bytecode as a sequence of integers
byte_code = list(total.__code__.co_code)
print("Byte code =", byte_code)

# Print Bytecode
print("Byte code =",total.__code__.co_code)

# Disassemble the total function to show its bytecode
dis.dis(total)

# Access the code object of the function
code_obj = total.__code__

# Access the constants array
constants = code_obj.co_consts

# Access the variable names array
varnames = code_obj.co_varnames

# Print the results
print("Constants (co_consts):", constants)
print("Variable Names (co_varnames):", varnames)

