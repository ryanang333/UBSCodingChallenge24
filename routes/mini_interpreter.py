from flask import Flask, request, jsonify

app = Flask(__name__)

# Store variables in a dictionary
variables = {}

def evaluate(expression):
    """Evaluate a single expression."""
    if isinstance(expression, str):
        # If it's a string, it could be a variable
        return variables.get(expression, expression)

    if not isinstance(expression, list):
        return expression

    # The first element is the function name
    func_name = expression[0]
    args = expression[1:]

    # Evaluate arguments
    evaluated_args = [evaluate(arg) for arg in args]

    # Call the corresponding function
    if func_name == 'puts':
        return puts(*evaluated_args)
    elif func_name == 'set':
        return set_variable(*evaluated_args)
    elif func_name == 'concat':
        return concat(*evaluated_args)
    elif func_name == 'lowercase':
        return lowercase(*evaluated_args)
    elif func_name == 'uppercase':
        return uppercase(*evaluated_args)
    elif func_name == 'replace':
        return replace(*evaluated_args)
    elif func_name == 'substring':
        return substring(*evaluated_args)
    elif func_name == 'add':
        return add(*evaluated_args)
    elif func_name == 'subtract':
        return subtract(*evaluated_args)
    elif func_name == 'multiply':
        return multiply(*evaluated_args)
    elif func_name == 'divide':
        return divide(*evaluated_args)
    elif func_name == 'abs':
        return abs_func(*evaluated_args)
    elif func_name == 'max':
        return max_func(*evaluated_args)
    elif func_name == 'min':
        return min_func(*evaluated_args)
    elif func_name == 'gt':
        return gt(*evaluated_args)
    elif func_name == 'lt':
        return lt(*evaluated_args)
    elif func_name == 'equal':
        return equal(*evaluated_args)
    elif func_name == 'not_equal':
        return not_equal(*evaluated_args)
    elif func_name == 'str':
        return str_func(*evaluated_args)

    raise ValueError(f"Unknown function: {func_name}")

def puts(*args):
    """Prints the string representation of the argument."""
    return ' '.join(str(arg) for arg in args)

def set_variable(var_name, value):
    """Sets a variable to a given value."""
    if var_name in variables:
        raise ValueError("Variable already exists.")
    variables[var_name] = value

def concat(arg1, arg2):
    """Concatenates two strings."""
    return arg1 + arg2

def lowercase(arg):
    """Converts a string to lowercase."""
    return arg.lower()

def uppercase(arg):
    """Converts a string to uppercase."""
    return arg.upper()

def replace(source, target, replacement):
    """Replaces occurrences of target in source with replacement."""
    return source.replace(target, replacement)

def substring(source, start, end):
    """Returns a substring from source from start to end indices."""
    return source[start:end]

def add(*args):
    """Adds numerical arguments."""
    return sum(args)

def subtract(arg1, arg2):
    """Subtracts arg2 from arg1."""
    return arg1 - arg2

def multiply(*args):
    """Multiplies numerical arguments."""
    result = 1
    for arg in args:
        result *= arg
    return result

def divide(arg1, arg2):
    """Divides arg1 by arg2."""
    if arg2 == 0:
        raise ValueError("Division by zero.")
    return arg1 / arg2

def abs_func(arg):
    """Returns the absolute value of arg."""
    return abs(arg)

def max_func(*args):
    """Returns the maximum of the arguments."""
    return max(args)

def min_func(*args):
    """Returns the minimum of the arguments."""
    return min(args)

def gt(arg1, arg2):
    """Checks if arg1 is greater than arg2."""
    return arg1 > arg2

def lt(arg1, arg2):
    """Checks if arg1 is less than arg2."""
    return arg1 < arg2

def equal(arg1, arg2):
    """Checks if two arguments are equal."""
    return arg1 == arg2

def not_equal(arg1, arg2):
    """Checks if two arguments are not equal."""
    return arg1 != arg2

def str_func(arg):
    """Converts arg to a string."""
    return str(arg)

@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    """API endpoint for parsing Lisp-like expressions."""
    expressions = request.json.get('expressions', [])
    output = []

    for line_number, expression in enumerate(expressions, start=1):
        try:
            result = evaluate(expression)
            output.append(result)
        except Exception as e:
            output.append(f"ERROR at line {line_number}: {str(e)}")

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
