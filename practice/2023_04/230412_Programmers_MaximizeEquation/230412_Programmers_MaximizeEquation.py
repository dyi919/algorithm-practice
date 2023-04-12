import re
def solution(expression):
    answer = []
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    for combination in combinations:
        operand = re.split('[*+-]',expression)
        operator = re.split('[0-9]+',expression)[1:-1]
        for comb in combination:
            while comb in operator:
                idx = operator.index(comb)
                operand[idx] = str(eval(operand[idx] + comb + operand[idx+1]))
                del operand[idx+1]
                del operator[idx]
        answer.append(abs(int(operand[0])))
    return max(answer)
