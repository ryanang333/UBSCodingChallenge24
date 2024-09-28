from flask import Flask, request, jsonify

app = Flask(__name__)

# Store variables
variables = {}

# Function to print outputs
def puts(string):
    if not isinstance(string, str):
        raise ValueError("ERROR: invalid argument type for puts")
    return string

# Function to set variables
def set_var(var_name, value):
    if var_name in variables:
        raise ValueError(f"ERROR: variable '{var_name}' already defined")
    variables[var_name] = value
    return None

# String operations
def concat(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("ERROR: invalid argument type for concat")
    return str1 + str2

def lowercase(string):
    if not isinstance(string, str):
        raise ValueError("ERROR: invalid argument type for lowercase")
    return string.lower()

def uppercase(string):
    if not isinstance(string, str):
        raise ValueError("ERROR: invalid argument type for uppercase")
    return string.upper()

def replace(source, target, replacement):
    if not isinstance(source, str) or not isinstance(target, str) or not isinstance(replacement, str):
        raise ValueError("ERROR: invalid argument type for replace")
    return source.replace(target, replacement)

def substring(source, start, end):
    if not isinstance(source, str) or not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("ERROR: invalid argument type for substring")
    return source[start:end]

# Number operations
def add(*args):
    if any(not isinstance(arg, (int, float)) for arg in args):
        raise ValueError("ERROR: invalid argument type for add")
    return round(sum(args), 4)

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("ERROR: invalid argument type for subtract")
    return round(a - b, 4)

def multiply(*args):
    if any(not isinstance(arg, (int, float)) for arg in args):
        raise ValueError("ERROR: invalid argument type for multiply")
    product = 1
    for arg in args:
        product *= arg
    return round(product, 4)

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("ERROR: invalid argument type for divide")
    if b == 0:
        raise ValueError("ERROR: division by zero")
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    return round(a / b, 4)

def abs_value(a):
    if not isinstance(a, (int, float)):
        raise ValueError("ERROR: invalid argument type for abs")
    return abs(a)

def max_value(*args):
    if len(args) < 2 or any(not isinstance(arg, (int, float)) for arg in args):
        raise ValueError("ERROR: invalid argument type for max")
    return max(args)

def min_value(*args):
    if len(args) < 2 or any(not isinstance(arg, (int, float)) for arg in args):
        raise ValueError("ERROR: invalid argument type for min")
    return min(args)

def gt(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("ERROR: invalid argument type for gt")
    return a > b

def lt(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("ERROR: invalid argument type for lt")
    return a < b

def equal(first, second):
    return first == second

def not_equal(first, second):
    return first != second

def str_value(arg):
    return str(arg)

# Function to evaluate an expression
def eval_expression(expression):
    tokens = expression.strip()[1:-1].split()
    function_name = tokens[0]
    args = []
    
    for token in tokens[1:]:
        if token in variables:
            args.append(variables[token])
        elif token.startswith('"') and token.endswith('"'):
            args.append(token[1:-1])  # Remove quotes
        elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            args.append(int(token))
        elif '.' in token and (token.replace('.', '').isdigit() or (token[0] == '-' and token[1:].replace('.', '').isdigit())):
            args.append(float(token))
        elif token.lower() == "true":
            args.append(True)
        elif token.lower() == "false":
            args.append(False)
        elif token == "null":
            args.append(None)
        else:
            raise ValueError(f"ERROR: unrecognized token '{token}'")

    if function_name == "puts":
        return puts(*args)
    elif function_name == "set":
        return set_var(*args)
    elif function_name == "concat":
        return concat(*args)
    elif function_name == "lowercase":
        return lowercase(*args)
    elif function_name == "uppercase":
        return uppercase(*args)
    elif function_name == "replace":
        return replace(*args)
    elif function_name == "substring":
        return substring(*args)
    elif function_name == "add":
        return add(*args)
    elif function_name == "subtract":
        return subtract(*args)
    elif function_name == "multiply":
        return multiply(*args)
    elif function_name == "divide":
        return divide(*args)
    elif function_name == "abs":
        return abs_value(*args)
    elif function_name == "max":
        return max_value(*args)
    elif function_name == "min":
        return min_value(*args)
    elif function_name == "gt":
        return gt(*args)
    elif function_name == "lt":
        return lt(*args)
    elif function_name == "equal":
        return equal(*args)
    elif function_name == "not_equal":
        return not_equal(*args)
    elif function_name == "str":
        return str_value(*args)

    raise ValueError(f"ERROR: unrecognized function '{function_name}'")

@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    data = request.json
    expressions = data.get('expressions', [])
    output = []
    try:
        for line_number, expression in enumerate(expressions, start=1):
            result = eval_expression(expression)
            if result is not None:
                output.append(result)
    except ValueError as e:
        error_message = f"ERROR at line {line_number}"
        return jsonify({"output": output + [error_message]}), 400

    return jsonify({"output": output}), 200

if __name__ == '__main__':
    app.run(debug=True)
