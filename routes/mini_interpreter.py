from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the functions for the interpreter
variables = {}

def puts(arg):
    if isinstance(arg, str):
        return arg
    raise ValueError("ERROR at line {line_number}")

def set_variable(var_name, value):
    if var_name in variables:
        raise ValueError("ERROR at line {line_number}")
    variables[var_name] = value

def concat(arg1, arg2):
    if isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    raise ValueError("ERROR at line {line_number}")

def lowercase(arg):
    if isinstance(arg, str):
        return arg.lower()
    raise ValueError("ERROR at line {line_number}")

def uppercase(arg):
    if isinstance(arg, str):
        return arg.upper()
    raise ValueError("ERROR at line {line_number}")

def replace(source, target, replacement):
    if isinstance(source, str) and isinstance(target, str) and isinstance(replacement, str):
        return source.replace(target, replacement)
    raise ValueError("ERROR at line {line_number}")

def substring(source, start, end):
    if isinstance(source, str) and isinstance(start, int) and isinstance(end, int):
        if start < 0 or end > len(source) or start >= end:
            raise ValueError("ERROR at line {line_number}")
        return source[start:end]
    raise ValueError("ERROR at line {line_number}")

def add(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        return round(sum(args), 4)
    raise ValueError("ERROR at line {line_number}")

def subtract(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return round(arg1 - arg2, 4)
    raise ValueError("ERROR at line {line_number}")

def multiply(*args):
    if all(isinstance(arg, (int, float)) for arg in args):
        product = 1
        for arg in args:
            product *= arg
        return round(product, 4)
    raise ValueError("ERROR at line {line_number}")

def divide(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        if arg2 == 0:
            raise ValueError("ERROR at line {line_number}")
        if isinstance(arg1, int) and isinstance(arg2, int):
            return arg1 // arg2
        return round(arg1 / arg2, 4)
    raise ValueError("ERROR at line {line_number}")

def abs_func(arg):
    if isinstance(arg, (int, float)):
        return abs(arg)
    raise ValueError("ERROR at line {line_number}")

def max_func(*args):
    if len(args) < 2 or not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("ERROR at line {line_number}")
    return max(args)

def min_func(*args):
    if len(args) < 2 or not all(isinstance(arg, (int, float)) for arg in args):
        raise ValueError("ERROR at line {line_number}")
    return min(args)

def gt(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 > arg2
    raise ValueError("ERROR at line {line_number}")

def lt(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 < arg2
    raise ValueError("ERROR at line {line_number}")

def equal(arg1, arg2):
    return arg1 == arg2

def not_equal(arg1, arg2):
    return arg1 != arg2

def str_func(arg):
    return str(arg)

# Map function names to their implementations
function_map = {
    'puts': puts,
    'set': set_variable,
    'concat': concat,
    'lowercase': lowercase,
    'uppercase': uppercase,
    'replace': replace,
    'substring': substring,
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'abs': abs_func,
    'max': max_func,
    'min': min_func,
    'gt': gt,
    'lt': lt,
    'equal': equal,
    'not_equal': not_equal,
    'str': str_func
}

def interpret_line(line):
    # Remove parentheses and split by spaces
    line = line.strip()[1:-1].split()
    func_name = line[0]
    args = line[1:]

    # Prepare arguments for the function
    prepared_args = []
    for arg in args:
        # Check if the argument is a variable
        if arg in variables:
            prepared_args.append(variables[arg])
        # Check if it's a number
        elif arg.replace('.', '', 1).isdigit() or (arg[0] == '-' and arg[1:].replace('.', '', 1).isdigit()):
            prepared_args.append(float(arg) if '.' in arg else int(arg))
        # Check if it's a boolean
        elif arg in ["true", "false"]:
            prepared_args.append(arg == "true")
        # Check if it's null
        elif arg == "null":
            prepared_args.append(None)
        # Otherwise, it's a string
        else:
            prepared_args.append(arg[1:-1])  # Remove quotes

    # Call the function and handle output
    try:
        result = function_map[func_name](*prepared_args)
        if func_name == 'puts':
            return result  # Only return for puts
    except Exception as e:
        return str(e)

@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    expressions = request.json.get('expressions', [])
    output = []

    for line_number, expression in enumerate(expressions, start=1):
        try:
            result = interpret_line(expression)
            if result is not None:
                output.append(result)
        except ValueError as e:
            output.append(f"ERROR at line {line_number}")

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
