import re

def arithmetic_arranger(problems, flag = False):
  if len(problems) > 5: return 'Error: Too many problems.'
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''

  for problem in problems:
    operator: str = ''
    if '+' in problem:
      problem = [number.strip() for number in problem.split('+')]
      operator = '+'
    elif '-' in problem:
      problem = [number.strip() for number in problem.split('-')]
      operator = '-'
    else:
      return "Error: Operator must be '+' or '-'."
    maxLenNumber = max([len(p) for p in problem])+2
    if maxLenNumber - 2 >= 5: return 'Error: Numbers cannot be more than four digits.'
    lenPro2 = len(problem[1])
    if re.search(r'\D', ''.join(problem)): return 'Error: Numbers must only contain digits.'
    result = str(eval(f'{problem[0]}{operator}{problem[1]}'))
    line1 += f'{" "*(maxLenNumber-len(problem[0]))}{problem[0]}    '
    line2 += f'{operator}{" "*(maxLenNumber-len(problem[1])-1)}{problem[1]}    '
    line3 += f'{"-"*maxLenNumber}    '
    line4 += f'{" "*(maxLenNumber-len(result))}{result}    '

  return f'{line1[0:-4]}\n{line2[0:-4]}\n{line3[0:-4]}\n{line4[0:-4]}' if flag else f'{line1[0:-4]}\n{line2[0:-4]}\n{line3[0:-4]}'
