from flask import Flask, request, jsonify

app = Flask(__name__)

variables = {}

def raise_error(line):
    return f"ERROR at line {line}"

def validate_numeric_args(args, line):
    """Validates that all arguments are numeric."""
    try:
        return [float(arg) for arg in args], None
    except ValueError:
        return None, raise_error(line)

def validate_string_args(args, line):
    """Validates that all arguments are strings."""
    if all(isinstance(arg, str) for arg in args):
        return args, None
    else:
        return None, raise_error(line)
    
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_boolean(value):
    return value in ["true", "false"]

def is_string(value):
    return value.startswith('"') and value.endswith('"')

def parse_value(value):
    """Converts a string representation into the correct data type."""
    if is_numeric(value):
        return float(value)
    elif is_boolean(value):
        return value == "true"  # Convert string "true" to Python True
    elif value == "null":
        return None
    elif is_string(value):
        return value[1:-1]  # Strip quotes for strings
    elif value in variables:
        return variables[value]  # Return variable value if defined
    else:
        return None  # Invalid or undefined variable
  
def concat(args, line_number):
    if len(args) != 2 or not all(is_string(arg) for arg in args):
        return None, raise_error(line_number, "concat expects two string arguments")
    return args[0][1:-1] + args[1][1:-1], None  # Concatenate after stripping quotes

def substring(args, line_number):
    if len(args) != 3 or not is_string(args[0]) or not all(is_numeric(arg) for arg in args[1:]):
        return None, raise_error(line_number, "substring expects a string and two numbers")
    string, start, end = args[0][1:-1], int(float(args[1])), int(float(args[2]))
    if start < 0 or end > len(string) or start > end:
        return None, raise_error(line_number, "substring index out of range")
    return string[start:end], None

def add(args, line_number):
    numbers, error = validate_numeric_args(args, line_number)
    if error:
        return None, error
    return str(round(sum(numbers), 4)), None

def divide(args, line_number):
    if len(args) != 2:
        return None, raise_error(line_number, "divide expects two arguments")
    numbers, error = validate_numeric_args(args, line_number)
    if error:
        return None, error
    if numbers[1] == 0:
        return None, raise_error(line_number, "division by zero")
    if numbers[0].is_integer() and numbers[1].is_integer():
        return str(int(numbers[0] // numbers[1])), None  # Integer division
    return str(round(numbers[0] / numbers[1], 4)), None  # Floating point division

def equal(args, line_number):
    if len(args) != 2:
        return None, raise_error(line_number, "equal expects two arguments")
    val1, val2 = parse_value(args[0]), parse_value(args[1])
    if type(val1) != type(val2):
        return "false", None
    return "true" if val1 == val2 else "false", None

def set_variable(args, line_number):
    if len(args) != 2:
        return None, raise_error(line_number, "set expects a variable name and a value")
    var_name, value = args[0], args[1]
    if var_name in variables:
        return None, raise_error(line_number, "variable already exists")
    variables[var_name] = parse_value(value)
    return None, None

def replace(args, line_number):
    if len(args) != 3 or not all(is_string(arg) for arg in args):
        return None, raise_error(line_number, "replace expects three string arguments")
    source, target, replacement = args[0][1:-1], args[1][1:-1], args[2][1:-1]
    return source.replace(target, replacement), None

def subtract(args, line_number):
    if len(args) != 2 or not all(is_numeric(arg) for arg in args):
        return None, raise_error(line_number, "subtract expects two numeric arguments")
    result = float(args[0]) - float(args[1])
    return str(round(result, 4)), None

def multiply(args, line_number):
    numbers, error = validate_numeric_args(args, line_number)
    if error:
        return None, error
    result = 1
    for num in numbers:
        result *= num
    return str(round(result, 4)), None

def gt(args, line_number):
    if len(args) != 2 or not all(is_numeric(arg) for arg in args):
        return None, raise_error(line_number, "gt expects two numeric arguments")
    return "true" if float(args[0]) > float(args[1]) else "false", None

def lt(args, line_number):
    if len(args) != 2 or not all(is_numeric(arg) for arg in args):
        return None, raise_error(line_number, "lt expects two numeric arguments")
    return "true" if float(args[0]) < float(args[1]) else "false", None

def eval_lisp_expression(expression, line_number):
    tokens = expression.replace('(', '').replace(')', '').split()

    if not tokens:
        return None, None

    function = tokens[0]

    # Handle functions
    if function == "puts":
        if len(tokens) != 2 or not tokens[1].startswith('"') or not tokens[1].endswith('"'):
            return None, raise_error(line_number)
        return tokens[1][1:-1], None 
    elif function == "set":
        return set_variable(tokens[1:], line_number)
    elif function == "concat":
        return concat(tokens[1:], line_number)
    elif function == "substring":
        return substring(tokens[1:], line_number)
    elif function == "add":
        return add(tokens[1:], line_number)
    elif function == "subtract":
        return subtract(tokens[1:], line_number)
    elif function == "multiply":
        return multiply(tokens[1:], line_number)
    elif function == "divide":
        return divide(tokens[1:], line_number)
    elif function == "replace":
        return replace(tokens[1:], line_number)
    elif function == "lowercase":
        if len(tokens) != 2:
            return None, raise_error(line_number)
        args, error = validate_string_args([tokens[1]], line_number)
        if error:
            return None, error
        return args[0].lower(), None
    
    elif function == "uppercase":
        if len(tokens) != 2:
            return None, raise_error(line_number)
        args, error = validate_string_args([tokens[1]], line_number)
        if error:
            return None, error
        return args[0].upper(), None
    
    elif function == "gt":
        return gt(tokens[1:], line_number)
    elif function == "lt":
        return lt(tokens[1:], line_number)
    elif function == "equal":
        return equal(tokens[1:], line_number)
    elif function == "not_equal":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        if tokens[1] != tokens[2]:
            return "true", None
        return "false", None
    elif function == "str":
        if len(tokens) != 2:
            return None, raise_error(line_number)
        var = tokens[1]
        if var in variables:
            return str(variables[var]), None
        return str(var), None
    
    # If the function is unknown
    return None, raise_error(line_number, f"unknown function '{function}'")
@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    data = request.json.get('expressions', [])
    output = []
    
    for i, line in enumerate(data):
        result, error = eval_lisp_expression(line, i + 1)
        if error:
            output.append(error)
            break
        if result:
            output.append(result)
    
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
