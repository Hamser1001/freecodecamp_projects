def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for item in problems:
        # split the list
        operation_list = item.split()

        # determine items by names
        first = operation_list[0]
        second = operation_list[2]
        operator = operation_list[1]

        # determine the max length
        length = max(len(first), len(second)) + 2

        # check the operator if not + or -
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        # if the operands are mote then 4 digits
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        # add specified item to the lines list
        line1.append(first.rjust(length))
        line2.append(operator + " " + second.rjust(length - 2))
        line3.append("-" * length)

        # Display total
        if show_answers == True:
            total = 0
            if operator == "+":
                total += int(first) + int(second)
            elif operator == "-":
                total += int(first) - int(second)
            else:
                return "Error: Operator must be '+' or '-'."
            line4.append(str(total).rjust(length))

    space_between = "    "
    # print(space_between.join(line1))
    # print(space_between.join(line2))
    # print(space_between.join(line3))
    # print(space_between.join(line4))

    result = (
        space_between.join(line1)
        + "\n"
        + space_between.join(line2)
        + "\n"
        + space_between.join(line3)
    )

    if show_answers:  # print(space_between.join(line1))
    # print(space_between.join(line2))
    # print(space_between.join(line3))
    # print(space_between.join(line4))
        result += "\n" + space_between.join(line4)
    # print(result)
    problems = result
    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
