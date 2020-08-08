import string
import collections


def print_single_number(a):
    variable = ''.join(a)
    if variable.isnumeric():
        print(variable)
    elif variable in store_dict:
        print(store_dict[variable])
    else:
        print('Unknown variable')


def check_input(list_):
    if list_:
        if list_[-1] in ['+', '-']:
            print('Invalid expression')
            return False
        else:
            for i in range(len(list_)):
                if list_[i] not in string.ascii_uppercase + string.ascii_lowercase + string.digits \
                        and list_[i] not in ['+', '-', '=', '(', ')', '*', '/'] and not list_[0] == '/':
                    print('Invalid expression')
                    return False
            return True

    return True


def check_assignment(assignment_list):
    assign_list = collections.deque(assignment_list)
    finall_assign = list()
    single_var = list()
    for i in range(len(assign_list)):
        if assign_list[i] in ['-', '+', '*', '/']:
            if single_var:
                variable = ''.join(single_var)
                if variable in store_dict:
                    finall_assign.append(store_dict[variable])
                    single_var.clear()
                else:
                    print('Unknown variable')
                    return False
            finall_assign.append(assign_list[i])
        elif assign_list[i].isnumeric():
            if single_var:
                print('Invalid assignment')
                return False
            elif assign_list[i] != assign_list[-1]:
                if assign_list[i + 1] in string.ascii_lowercase + string.ascii_uppercase:
                    finall_assign.append(assign_list[i] + '*')
                    continue

            finall_assign.append(assignment_list[i])
        else:
            single_var.append(assignment_list[i])
    if single_var:
        variable = ''.join(single_var)
        if variable in store_dict:
            finall_assign.append(store_dict[variable])
        else:
            print('Invalid assignment')
            return False
    d = ''.join(finall_assign)
    return int(eval(d))


def check_pow(var_list):
    if '***' in var_list or '//' in var_list:
        print('Invalid expression')
        return False
    return True


def check_paranthas(var_list):
    if '(' or ')' in var_list:
        check_list = collections.deque()
        for i in var_list:
            if i in ['(', ')']:
                check_list.append(i)
        if len(check_list) % 2 == 0:
            for _ in range(int(len(check_list) / 2)):
                if check_list.popleft() == check_list.pop():
                    print('Invalid expression')
                    return False
            return True
        print('Invalid expression')
        return False
    return True


def find_variable(var_list):
    current_command_list = collections.deque(var_list)
    single_var_list = []
    full_command_list = []
    for i in var_list:
        if i.isnumeric():
            full_command_list.append(current_command_list.popleft())
        elif i in ['(', ')']:
            full_command_list.append(current_command_list.popleft())
        elif i in ['+', '-', '*', '/']:
            if single_var_list:
                variable = ''.join(single_var_list)
                if variable in store_dict:
                    full_command_list.append(store_dict[variable])
                    single_var_list.clear()
                else:
                    print('Unknown variable')
                    return False
            full_command_list.append(current_command_list.popleft())
        else:
            single_var_list.append(current_command_list.popleft())
    if single_var_list:
        if single_var_list:
            variable = ''.join(single_var_list)
            if variable in store_dict:
                full_command_list.append(store_dict[variable])
                single_var_list.clear()
            else:
                print('Unknown variable')
                return False
    if check_paranthas(full_command_list) and check_pow(''.join(full_command_list)):
        d = ''.join(full_command_list)
        print(int(eval(d)))


quit = {'exit': True}
store_dict = {}
while quit['exit']:
    what_to_do = list(input().replace(' ', ''))
    if check_input(what_to_do):

        if ''.join(what_to_do).startswith('/') and ''.join(what_to_do) not in ['/exit', '/help']:
            print('Unknown command')
        elif '=' in what_to_do and len(what_to_do) >= 3:
            if what_to_do[0] != '=' and what_to_do[-1] != '=' and what_to_do.count('=') == 1:
                index = what_to_do.index('=')
                identifier = what_to_do[0:index]

                if any([i.isnumeric() for i in identifier]):
                    print('Invalid identifier')
                else:
                    identifier = ''.join(identifier)
                    assignment = what_to_do[index + 1:]
                    assignment = check_assignment(assignment)
                    store_dict[identifier] = str(assignment)
            else:
                print('Invalid assignment')


        elif ''.join(what_to_do) == '/exit':
            quit['exit'] = False
            print('Bye!')

        elif ''.join(what_to_do) == '/help':
            print('The program calculates the sum of numbers, you should write number and arithmetic operand')

        elif len(what_to_do) == 0:
            continue

        elif (not (
                '*' in what_to_do or '/' in what_to_do or '+' in what_to_do or '-' in what_to_do or '=' in what_to_do)) or ''.join(
            what_to_do) in ['/exit', '/help']:

            print_single_number(what_to_do)

        elif '+' or '-' in what_to_do:
            find_variable(what_to_do)
