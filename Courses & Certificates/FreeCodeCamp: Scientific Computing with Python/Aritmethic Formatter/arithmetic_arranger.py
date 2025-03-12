def arithmetic_arranger(problems, show_answers=False) -> str:
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operands = []
    second_operands = []
    operators = []
    results = []

    for problem in problems:
        if "+" in problem:
            operator = "+"
        elif "-" in problem:
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        parts = problem.split(operator)
        first_part = parts[0].strip()
        second_part = parts[1].strip()

        if not first_part.isdigit() or not second_part.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_part) > 4 or len(second_part) > 4:
            return "Error: Numbers cannot be more than four digits."

        first_operands.append(first_part)
        second_operands.append(second_part)
        operators.append(operator)

        if operator == "+":
            result = str(int(first_part) + int(second_part))
        else:
            result = str(int(first_part) - int(second_part))

        results.append(result)

    # Print the result by lines and store them
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for i in range(len(problems)):
        length = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(length)
        second_line += operators[i] + " " + second_operands[i].rjust(length - 2)
        third_line += "-" * length
        fourth_line += results[i].rjust(length)

        if i < len(problems) - 1:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            fourth_line += "    "

    if show_answers:
        arranged_problems = (
            first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
        )
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line

    return arranged_problems
