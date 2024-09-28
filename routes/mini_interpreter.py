from flask import Flask, request, jsonify

app = Flask(__name__)

# Store variables in a dictionary
variables = {}

def evaluate_expression(expr):
    tokens = expr.strip('()').split()
    function = tokens[0]
    
    # Handle different functions based on the provided definition
    if function == "puts":
        if len(tokens) != 2:
            raise ValueError("Incorrect number of arguments for puts")
        arg = evaluate_argument(tokens[1])
        if not isinstance(arg, str):
            raise ValueError("Argument for puts must be a string")
        return arg
    
    elif function == "set":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for set")
        var_name = tokens[1]
        value = evaluate_argument(tokens[2])
        if var_name in variables:
            raise ValueError(f"Variable '{var_name}' already exists")
        variables[var_name] = value
        return None
    
    elif function == "concat":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for concat")
        str1 = evaluate_argument(tokens[1])
        str2 = evaluate_argument(tokens[2])
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Arguments for concat must be strings")
        return str1 + str2

    elif function == "lowercase":
        if len(tokens) != 2:
            raise ValueError("Incorrect number of arguments for lowercase")
        str_input = evaluate_argument(tokens[1])
        if not isinstance(str_input, str):
            raise ValueError("Argument for lowercase must be a string")
        return str_input.lower()
    
    elif function == "uppercase":
        if len(tokens) != 2:
            raise ValueError("Incorrect number of arguments for uppercase")
        str_input = evaluate_argument(tokens[1])
        if not isinstance(str_input, str):
            raise ValueError("Argument for uppercase must be a string")
        return str_input.upper()
    
    elif function == "replace":
        if len(tokens) != 4:
            raise ValueError("Incorrect number of arguments for replace")
        source = evaluate_argument(tokens[1])
        target = evaluate_argument(tokens[2])
        replacement = evaluate_argument(tokens[3])
        if not all(isinstance(arg, str) for arg in [source, target, replacement]):
            raise ValueError("Arguments for replace must be strings")
        return source.replace(target, replacement)

    elif function == "substring":
        if len(tokens) != 4:
            raise ValueError("Incorrect number of arguments for substring")
        source = evaluate_argument(tokens[1])
        start = evaluate_argument(tokens[2])
        end = evaluate_argument(tokens[3])
        if not isinstance(source, str) or not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Invalid argument types for substring")
        if start < 0 or end > len(source) or start >= end:
            raise ValueError("Substring indices are out of bounds")
        return source[start:end]
    
    elif function == "add":
        if len(tokens) < 3:
            raise ValueError("Incorrect number of arguments for add")
        return sum(evaluate_argument(token) for token in tokens[1:])
    
    elif function == "subtract":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for subtract")
        a = evaluate_argument(tokens[1])
        b = evaluate_argument(tokens[2])
        return a - b
    
    elif function == "multiply":
        if len(tokens) < 3:
            raise ValueError("Incorrect number of arguments for multiply")
        product = 1
        for token in tokens[1:]:
            product *= evaluate_argument(token)
        return product
    
    elif function == "divide":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for divide")
        a = evaluate_argument(tokens[1])
        b = evaluate_argument(tokens[2])
        if b == 0:
            raise ValueError("Division by zero")
        return a // b if isinstance(a, int) and isinstance(b, int) else a / b
    
    elif function == "abs":
        if len(tokens) != 2:
            raise ValueError("Incorrect number of arguments for abs")
        num = evaluate_argument(tokens[1])
        return abs(num)
    
    elif function == "max":
        if len(tokens) < 3:
            raise ValueError("Incorrect number of arguments for max")
        return max(evaluate_argument(token) for token in tokens[1:])
    
    elif function == "min":
        if len(tokens) < 3:
            raise ValueError("Incorrect number of arguments for min")
        return min(evaluate_argument(token) for token in tokens[1:])

    elif function == "gt":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for gt")
        a = evaluate_argument(tokens[1])
        b = evaluate_argument(tokens[2])
        return a > b
    
    elif function == "lt":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for lt")
        a = evaluate_argument(tokens[1])
        b = evaluate_argument(tokens[2])
        return a < b
    
    elif function == "equal":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for equal")
        a = evaluate_argument(tokens[1])
        b = evaluate_argument(tokens[2])
        return a == b
    
    elif function == "not_equal":
        if len(tokens) != 3:
            raise ValueError("Incorrect number of arguments for not_equal")
        a = evaluate_argument(tokens[1])
        b = evaluate_argument(tokens[2])
        return a != b
    
    elif function == "str":
        if len(tokens) != 2:
            raise ValueError("Incorrect number of arguments for str")
        value = evaluate_argument(tokens[1])
        return str(value)

    else:
        raise ValueError(f"Unknown function: {function}")

def evaluate_argument(arg):
    if arg.startswith('"') and arg.endswith('"'):
        return arg[1:-1]  # Remove quotes for strings
    elif arg.isdigit():
        return int(arg)
    try:
        float_arg = float(arg)
        return float_arg if '.' in arg else int(float_arg)
    except ValueError:
        if arg in variables:
            return variables[arg]
        else:
            raise ValueError(f"Unknown variable: {arg}")

@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    data = request.get_json()
    expressions = data.get("expressions", [])
    
    output = []
    for i, expr in enumerate(expressions):
        try:
            result = evaluate_expression(expr)
            if result is not None:  # Only print if there is a result
                output.append(result)
        except ValueError as e:
            output.append(f"ERROR at line {i + 1}")
            break  # Stop on the first error

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
