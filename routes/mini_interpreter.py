from flask import Flask, request, jsonify

app = Flask(__name__)

variables = {}

# List to store output
outputs = []

def execute_expression(expr, line_number):
    global variables, outputs
    # Remove outer parentheses and split by space
    if not (expr.startswith("(") and expr.endswith(")")):
        raise ValueError(f"ERROR at line {line_number}")

    expr = expr[1:-1].strip()
    parts = expr.split(" ")
    
    func_name = parts[0]
    args = parts[1:]

    # Handle printing
    if func_name == "puts":
        if len(args) != 1:
            raise ValueError(f"ERROR at line {line_number}")
        arg_value = evaluate_argument(args[0], line_number)
        outputs.append(arg_value)  # Append to outputs
        return None

    # Handle variable setting
    elif func_name == "set":
        if len(args) != 2:
            raise ValueError(f"ERROR at line {line_number}")
        var_name, value = args
        if var_name in variables:
            raise ValueError(f"ERROR at line {line_number}")
        variables[var_name] = evaluate_argument(value, line_number)
        return None

    # Handle string functions
    elif func_name == "concat":
        if len(args) != 2:
            raise ValueError(f"ERROR at line {line_number}")
        return concat(args, line_number)

    elif func_name == "lowercase":
        if len(args) != 1:
            raise ValueError(f"ERROR at line {line_number}")
        return lowercase(args[0], line_number)

    elif func_name == "uppercase":
        if len(args) != 1:
            raise ValueError(f"ERROR at line {line_number}")
        return uppercase(args[0], line_number)

    elif func_name == "replace":
        if len(args) != 3:
            raise ValueError(f"ERROR at line {line_number}")
        return replace(args, line_number)

    elif func_name == "substring":
        if len(args) != 3:
            raise ValueError(f"ERROR at line {line_number}")
        return substring(args, line_number)

    # Handle number functions
    elif func_name == "add":
        return add(args, line_number)

    elif func_name == "subtract":
        return subtract(args, line_number)

    elif func_name == "multiply":
        return multiply(args, line_number)

    elif func_name == "divide":
        return divide(args, line_number)

    elif func_name == "abs":
        if len(args) != 1:
            raise ValueError(f"ERROR at line {line_number}")
        return abs_function(args[0], line_number)

    elif func_name == "max":
        return max_function(args, line_number)

    elif func_name == "min":
        return min_function(args, line_number)

    elif func_name == "gt":
        return gt(args, line_number)

    elif func_name == "lt":
        return lt(args, line_number)

    elif func_name == "equal":
        return equal(args, line_number)

    elif func_name == "not_equal":
        return not_equal(args, line_number)

    elif func_name == "str":
        if len(args) != 1:
            raise ValueError(f"ERROR at line {line_number}")
        return str_function(args[0], line_number)

    else:
        raise ValueError(f"ERROR at line {line_number}")


def evaluate_argument(arg, line_number):
    if arg in variables:
        return variables[arg]
    elif arg.isdigit() or (arg[0] == '-' and arg[1:].isdigit()):
        return int(arg)
    elif '.' in arg:
        try:
            return float(arg)
        except ValueError:
            raise ValueError(f"ERROR at line {line_number}")
    elif arg == "true":
        return True
    elif arg == "false":
        return False
    elif arg == "null":
        return None
    elif arg.startswith('"') and arg.endswith('"'):
        return arg[1:-1]  # Return string without quotes
    else:
        raise ValueError(f"ERROR at line {line_number}")


# Define each operation
def concat(args, line_number):
    str1 = evaluate_argument(args[0], line_number)
    str2 = evaluate_argument(args[1], line_number)
    return str1 + str2


def lowercase(arg, line_number):
    str_val = evaluate_argument(arg, line_number)
    return str_val.lower()


def uppercase(arg, line_number):
    str_val = evaluate_argument(arg, line_number)
    return str_val.upper()


def replace(args, line_number):
    src = evaluate_argument(args[0], line_number)
    target = evaluate_argument(args[1], line_number)
    replacement = evaluate_argument(args[2], line_number)
    return src.replace(target, replacement)


def substring(args, line_number):
    src = evaluate_argument(args[0], line_number)
    start = evaluate_argument(args[1], line_number)
    end = evaluate_argument(args[2], line_number)
    if not isinstance(src, str) or not isinstance(start, int) or not isinstance(end, int):
        raise ValueError(f"ERROR at line {line_number}")
    return src[start:end]


def add(args, line_number):
    return sum(evaluate_argument(arg, line_number) for arg in args)


def subtract(args, line_number):
    if len(args) != 2:
        raise ValueError(f"ERROR at line {line_number}")
    num1 = evaluate_argument(args[0], line_number)
    num2 = evaluate_argument(args[1], line_number)
    return num1 - num2


def multiply(args, line_number):
    result = 1
    for arg in args:
        result *= evaluate_argument(arg, line_number)
    return result


def divide(args, line_number):
    if len(args) != 2:
        raise ValueError(f"ERROR at line {line_number}")
    num1 = evaluate_argument(args[0], line_number)
    num2 = evaluate_argument(args[1], line_number)
    if num2 == 0:
        raise ValueError(f"ERROR at line {line_number}")
    return num1 // num2 if isinstance(num1, int) and isinstance(num2, int) else num1 / num2


def abs_function(arg, line_number):
    num = evaluate_argument(arg, line_number)
    return abs(num)


def max_function(args, line_number):
    if len(args) < 2:
        raise ValueError(f"ERROR at line {line_number}")
    return max(evaluate_argument(arg, line_number) for arg in args)


def min_function(args, line_number):
    if len(args) < 2:
        raise ValueError(f"ERROR at line {line_number}")
    return min(evaluate_argument(arg, line_number) for arg in args)


def gt(args, line_number):
    if len(args) != 2:
        raise ValueError(f"ERROR at line {line_number}")
    num1 = evaluate_argument(args[0], line_number)
    num2 = evaluate_argument(args[1], line_number)
    return num1 > num2


def lt(args, line_number):
    if len(args) != 2:
        raise ValueError(f"ERROR at line {line_number}")
    num1 = evaluate_argument(args[0], line_number)
    num2 = evaluate_argument(args[1], line_number)
    return num1 < num2


def equal(args, line_number):
    if len(args) != 2:
        raise ValueError(f"ERROR at line {line_number}")
    arg1 = evaluate_argument(args[0], line_number)
    arg2 = evaluate_argument(args[1], line_number)
    return arg1 == arg2


def not_equal(args, line_number):
    if len(args) != 2:
        raise ValueError(f"ERROR at line {line_number}")
    arg1 = evaluate_argument(args[0], line_number)
    arg2 = evaluate_argument(args[1], line_number)
    return arg1 != arg2


def str_function(arg, line_number):
    value = evaluate_argument(arg, line_number)
    return str(value)


@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    global outputs
    outputs = []  # Reset outputs for each request
    try:
        data = request.get_json()
        expressions = data.get('expressions', [])
        for i, expression in enumerate(expressions, start=1):
            execute_expression(expression, i)
        return jsonify({"output": outputs})

    except ValueError as e:
        return jsonify({"output": []}), 400
    except Exception as e:
        return jsonify({"output": []}), 500


if __name__ == '__main__':
    app.run(debug=True)
