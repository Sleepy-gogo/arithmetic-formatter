import re


def format_number(number, width):
  return " " * (width - len(number)) + number


def format_problem(upper, lower, operand, solution = ""):
  width = len(upper) if len(upper) > len(lower) else len(lower)

  length_solution = len(solution)
  diff = 1

  if width < length_solution:
    width = length_solution - 1 if length_solution > 3 else length_solution
    diff = 0 if length_solution > 3 else diff

  upper = format_number(upper, width)
  lower = format_number(lower, width)
  solution = format_number(solution, width) if solution else ""

  return [f'  {upper}', f'{operand} {lower}', '-' * (width + 2), ' ' * (diff if diff else 0) + f' {solution}']


def split_operations(problem):
  return problem.split()


def get_result(upper, lower, opperand):
  upper = int(upper)
  lower = int(lower)
  return str(upper + lower) if opperand == "+" else str(upper - lower)


def unite_problems(problems):
  arranged_problems = ''

  for section in problems:
    for i, part in enumerate(section):
      arranged_problems += part

      if i + 1 != len(section):
        arranged_problems += '    '

    arranged_problems += '\n'

  return arranged_problems


def arithmetic_arranger(problems, solutions=False):

  if len(problems) > 5:
    return 'Error: Too many problems.'

  for problem in problems:
    if ('+' not in problem) and ('-' not in problem):
      return "Error: Operator must be '+' or '-'."

    if re.findall("[a-zA-Z]", problem):
      return "Error: Numbers must only contain digits."

    if re.findall("[0-9]{5,}", problem):
      return "Error: Numbers cannot be more than four digits."

  splited = [split_operations(problem) for problem in problems]

  if solutions:
    formated_problems = [
      format_problem(problem[0], problem[2], problem[1], get_result(problem[0], problem[2], problem[1])) for problem in splited
    ]
  else:
    formated_problems = [
      format_problem(problem[0], problem[2], problem[1]) for problem in splited
    ]
  
  uppers = [problem[0] for problem in formated_problems]
  lowers = [problem[1] for problem in formated_problems]
  separation = [problem[2] for problem in formated_problems]
  results = [] if not solutions else [problem[3] for problem in formated_problems]

  return unite_problems([uppers, lowers, separation, results])[:(-1 if solutions else -2)]