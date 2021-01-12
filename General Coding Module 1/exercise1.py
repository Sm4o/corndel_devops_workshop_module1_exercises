
# PART 1
# operation = input("Select operation ('x', '+', '-', '/')")

# parameter_a = int(input("Give value of A (int)"))
# parameter_b = int(input("Give value of B (int)"))

# if operation == 'x':
#     print(parameter_a * parameter_b)
# elif operation == '+':
#     print(parameter_a + parameter_b)
# elif operation == '-':
#     print(parameter_a - parameter_b)
# elif operation == '/':
#     print(parameter_a / parameter_b)    


# PART 2
# with open('General Coding Module 1/instructions_part2.txt', 'r') as f:
#     calc_instructions = f.read().splitlines()
#     for instruction in calc_instructions:
#         _, operation, parameter_a, parameter_b = instruction.split()
#         parameter_a, parameter_b = int(parameter_a), int(parameter_b)
#         if operation == 'x':
#             print(parameter_a * parameter_b)
#         elif operation == '+':
#             print(parameter_a + parameter_b)
#         elif operation == '-':
#             print(parameter_a - parameter_b)
#         elif operation == '/':
#             print(parameter_a / parameter_b)    

# PART 3
# def calculate_goto_row(goto_row: str) -> int:
#     _, operation, parameter_a, parameter_b = goto_row.split()
#     parameter_a, parameter_b = int(parameter_a), int(parameter_b)
#     if operation == 'x':
#         return parameter_a * parameter_b
#     elif operation == '+':
#         return parameter_a + parameter_b
#     elif operation == '-':
#         return parameter_a - parameter_b
#     elif operation == '/':
#         return parameter_a / parameter_b

# with open('General Coding Module 1/instructions_part3.txt', 'r') as f:
#     instructions = f.read().splitlines()
#     instruction_start = instructions[0] 

#     next_instruction = instruction_start

#     instruction_log = []

#     while next_instruction:
#         if next_instruction in instruction_log:
#             line_number = instructions.index(next_instruction) + 1
#             print(f'Duplicate statement found, stopping at line {line_number} with statement: {next_instruction}')
#             break
#         instruction_log.append(next_instruction)
        
#         goto_row = next_instruction.split('goto')[1]
#         try:
#             goto_row = int(goto_row)
#         except:
#             goto_row = int(calculate_goto_row(goto_row))
                
#         next_instruction = instructions[goto_row-1]
#         print(next_instruction)

         
# PART 4
def calculate_goto_row(goto_row: str) -> int:
    _, operation, parameter_a, parameter_b = goto_row.split()
    parameter_a, parameter_b = int(parameter_a), int(parameter_b)
    if operation == 'x':
        return parameter_a * parameter_b
    elif operation == '+':
        return parameter_a + parameter_b
    elif operation == '-':
        return parameter_a - parameter_b
    elif operation == '/':
        return parameter_a / parameter_b
    elif operation == '^':
        return parameter_a ** parameter_b

with open('General Coding Module 1/instructions_part4.txt', 'r') as f:
    instructions = f.read().splitlines()
    # Keep original instructions for reference 
    instructions_copy = instructions.copy()

    instruction_start = instructions[0] 

    next_instruction = instruction_start

    instruction_log = []

    while next_instruction:
        if next_instruction in instruction_log:
            line_number = instructions.index(next_instruction) + 1
            print(f'Duplicate statement found, stopping at line {line_number} with statement: {next_instruction}')
            break
        instruction_log.append(next_instruction)
        print(instruction_log)

        command = next_instruction.split()[0]
        
        if command == 'goto': 
            print(next_instruction)
            goto_row = next_instruction.split('goto')[1]
            try:
                goto_row = int(goto_row)
            except:
                goto_row = int(calculate_goto_row(goto_row))
            next_instruction = instructions_copy[goto_row-1]

        elif command == 'remove':
            print('Remove', next_instruction)
            remove_row = int(next_instruction.split()[1])
            instruction_to_remove = instructions_copy[remove_row-1]
            instructions.remove(instruction_to_remove)
            next_instruction_row = instructions_copy.index(next_instruction)
            next_instruction = instructions_copy[next_instruction_row + 1]

        elif command == 'replace':
            print('Replace', next_instruction)
            to_replace_row, replace_by_row = next_instruction.split()[1:]
            to_replace_row, replace_by_row = int(to_replace_row), int(to_replace_row)
            next_instruction_row = instructions.index(next_instruction)
            instructions = [instructions_copy[replace_by_row] if instructions_copy[to_replace_row] == row else row for i, row in enumerate(instructions)]
            next_instruction = instructions[next_instruction_row] 