def arithmetic_arranger(problems, show_answers=False):
    # Check if too many problems are supplied
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Create (string) variables for all output lines
    first = ""
    second = ""
    lines = ""
    solutions = ""
    string = ""

    for problem in problems:
        # Create variables for operands and operator
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        # Check if correct operators are supplied
        if "/" in problem or "*" in problem:
            return "Error: Operator must be '+' or '-'."
        # Check if each operand only contains digits
        if first_number.isdigit() == False or second_number.isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        # Check if each operand has a max of four digits width
        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate sum for individual problems and convert into string
        solution = ""
        if operator == "+":
            solution = str(int(first_number) + int(second_number))
        elif operator == "-":
            solution = str(int(first_number) - int(second_number))

        # Find length of longest number and calculate required length
        length = (max(len(first_number), len(second_number))) + 2
        # Right align using space as fill character
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        for i in range(length):
            line += "-"
        sol = str(solution).rjust(length)

        # Add trailing spaces except for last problem
        if problem != problems[-1]:
            first += top + " " * 4
            second += bottom + " " * 4
            lines += line + " " * 4
            solutions += sol + " " * 4
        else:
            first += top
            second += bottom
            lines += line
            solutions += sol

    # Final string returned to user
    if show_answers:
        string = f"{first}\n{second}\n{lines}\n{solutions}"
    else:
        string = f"{first}\n{second}\n{lines}"
    return string


print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')

# arithmetic_arranger(["5 - 1111", "2222 + 6", "321 + 23", "22 - 123"])