def arithmetic_arranger(problems, show_answers=False):
    result_string_output = ""
    a_list = []
    b_list = []
    operator_list = []
    results_list = []
    if len(problems) > 5:
        return "Error: Too many problems."
    is_illegal_operator = False
    is_number_more_4_digits = False
    parse_exception = False
    for i in problems:
        a = 0
        b = 0
        result = 0
        trimed_problem = i.replace(" ", "")
        if trimed_problem.find("+") != -1:
            try:
                a = int(trimed_problem.split("+")[0])
                b = int(trimed_problem.split("+")[1])
            except:
                parse_exception = True
                break
            
            if len(str(a)) > 4 or len(str(b)) > 4:
                is_number_more_4_digits = True
                break
            result = a + b
            a_list.append(a)
            b_list.append(b)
            operator_list.append('+')
            results_list.append(result)
        elif trimed_problem.find("-") != -1:
            try:
                a = int(trimed_problem.split("-")[0])
                b = int(trimed_problem.split("-")[1])
            except:
                parse_exception = True
                break
            if len(str(a)) > 4 or len(str(b)) > 4:
                is_number_more_4_digits = True
                break
            result = a - b
            a_list.append(a)
            b_list.append(b)
            operator_list.append('-')
            results_list.append(result)
        else:
            is_illegal_operator = True
            break

    if is_illegal_operator:
        return "Error: Operator must be '+' or '-'."
    if is_number_more_4_digits:
        return "Error: Numbers cannot be more than four digits."
    if parse_exception:
        return "Error: Numbers must only contain digits."
    result_a_string = ""
    result_b_string = ""
    dashes_string = ""
    results_string = ""

    for i in range(len(a_list)):
        string_align = max(len(str(a_list[i])) + 2, len(str(b_list[i])) + 2)
        end_space = ("    " if i != len(a_list) - 1 else "")
        result_a_string += str(a_list[i]).rjust(string_align) + end_space
        result_b_string += operator_list[i] + " " + str(b_list[i]).rjust(string_align - 2) + end_space
        dashes_string += ''.rjust(string_align, "-") + end_space
        results_string += str(results_list[i]).rjust(string_align) + end_space
    
    result_string_output += result_a_string + "\n"
    result_string_output += result_b_string + "\n"
    result_string_output += dashes_string
    if show_answers:
        result_string_output += "\n" + results_string
    return result_string_output

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')