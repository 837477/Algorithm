import re
expression = '+' + input()

regex = re.compile("\+|\-")
operator = regex.findall(expression)
regex = re.compile("\-\d+|\+\d+")
operand = list(map(int, regex.findall(expression)))

prev_operator = operator[0]
for i in range(1, len(operand)):
    if operator[i] == '+' and prev_operator == '-':
        operand[i] *= -1
        operator[i] = '-'
    prev_operator = operator[i]

print(sum(operand))