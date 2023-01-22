import sys
import re


class Calculator:
    def __init__(self):
        self.pattern = re.compile(r"\((add|multiply) (\d+) (\d+)(?: (\d+))*\)")

    def evaluate(self, expr):
            while (not expr.isdigit()):
                for match in self.pattern.finditer(expr):
                    func, *args = match.group().strip('()').split(' ')
                    if (func == 'add'):
                        value = sum([int(num) for num in args])
                    elif (func == 'multiply'):
                        value = 1
                        for num in args:
                            value *= int(num)
                    expr = expr.replace(match.group(), str(value))

                match = re.search(self.pattern, expr)
                if match is None and not expr.isdigit():
                    return "Invalid Input, Please check your input"

            return int(expr)


if __name__ == '__main__':
    expr = sys.argv[1]
    calculator = Calculator()
    print(calculator.evaluate(expr))
