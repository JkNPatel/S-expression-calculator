# S-expression calculator

This is a simple calculator program that takes a single argument as an expression and prints out the integer result of evaluating it. The expression is passed in as a command-line argument and it is a string. The syntax resembles S-expressions but the rules are simplified.

## Usage

    $ python calc.py 123
    

> 123

    $ python calc.py "(add 12 12)"
    

> 24

    $ python calc.py "(add 12 12 12 12)"
    

> 48

    $ python calc.py "(multiply 2 2 1 3)"
    

> 12

    $ python calc.py "(add 2 (add (multiply 3 1) (add 3 3)))"
    

> 11

    $ python calc.py "(add 1 1 (add (multiply 2 5 6) 2) 33)"
    

> 97

## Installation

This code is written in Python, so you will need to have Python installed on your machine to run it. You can download the latest version of Python from the official website [here](https://www.python.org/downloads/).

## Note
The current version of the code only supports the `add`  and `multiply` functions with  2  or more operands. If you enter an expression with less than 2 operands or an invalid function, the program will return an error message. 