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

def eval_lisp_expression(expression, line_number):
    tokens = expression.replace('(', '').replace(')', '').split()

    if not tokens:
        return None, None 

    function = tokens[0]
    
    if function == "puts":
        if len(tokens) != 2 or not tokens[1].startswith('"') or not tokens[1].endswith('"'):
            return None, raise_error(line_number)
        return tokens[1][1:-1], None  
    
    elif function == "set":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        var_name = tokens[1]
        var_value = tokens[2]
        if var_name in variables:
            return None, raise_error(line_number)
        variables[var_name] = var_value
        return None, None
    
    elif function == "concat":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        args, error = validate_string_args(tokens[1:], line_number)
        if error:
            return None, error
        return args[0] + args[1], None
    
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
    
    elif function == "replace":
        if len(tokens) != 4:
            return None, raise_error(line_number)
        args, error = validate_string_args(tokens[1:], line_number)
        if error:
            return None, error
        return args[0].replace(args[1], args[2]), None

    elif function == "substring":
        if len(tokens) != 4:
            return None, raise_error(line_number)
        source, start, end = tokens[1], tokens[2], tokens[3]
        if not source.startswith('"') or not source.endswith('"'):
            return None, raise_error(line_number)
        try:
            start = int(start)
            end = int(end)
        except ValueError:
            return None, raise_error(line_number)
        if start < 0 or end < 0 or start >= len(source) or end > len(source):
            return None, raise_error(line_number)
        return source[start:end], None

    elif function == "add":
        if len(tokens) < 3:
            return None, raise_error(line_number)
        numbers, error = validate_numeric_args(tokens[1:], line_number)
        if error:
            return None, error
        return str(round(sum(numbers), 4)), None

    elif function == "subtract":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        numbers, error = validate_numeric_args(tokens[1:], line_number)
        if error:
            return None, error
        return str(round(numbers[0] - numbers[1], 4)), None

    elif function == "multiply":
        if len(tokens) < 3:
            return None, raise_error(line_number)
        numbers, error = validate_numeric_args(tokens[1:], line_number)
        if error:
            return None, error
        result = 1
        for num in numbers:
            result *= num
        return str(round(result, 4)), None

    elif function == "divide":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        numbers, error = validate_numeric_args(tokens[1:], line_number)
        if error:
            return None, error
        if numbers[1] == 0:
            return None, raise_error(line_number)
        result = numbers[0] / numbers[1]
        if isinstance(numbers[0], int) and isinstance(numbers[1], int):
            return str(int(result)), None
        return str(round(result, 4)), None

    # Comparison and Boolean functions
    elif function == "equal":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        if tokens[1] == tokens[2]:
            return "true", None
        return "false", None
    
    elif function == "not_equal":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        if tokens[1] != tokens[2]:
            return "true", None
        return "false", None
    
    elif function == "gt":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        numbers, error = validate_numeric_args(tokens[1:], line_number)
        if error:
            return None, error
        return "true" if numbers[0] > numbers[1] else "false", None

    elif function == "lt":
        if len(tokens) != 3:
            return None, raise_error(line_number)
        numbers, error = validate_numeric_args(tokens[1:], line_number)
        if error:
            return None, error
        return "true" if numbers[0] < numbers[1] else "false", None

    # Variable access
    elif function == "str":
        if len(tokens) != 2:
            return None, raise_error(line_number)
        var = tokens[1]
        if var in variables:
            return str(variables[var]), None
        return str(var), None

    return None, raise_error(line_number)

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
