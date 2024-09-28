from flask import Flask, request, jsonify

app = Flask(__name__)

# This will store variable assignments
variables = {}

def puts(arg):
    if isinstance(arg, str):
        return arg
    raise ValueError("Invalid argument for puts; expected a string.")

def str_func(arg):
    return str(arg) if arg is not None else "null"

def concat(arg1, arg2):
    if isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    raise ValueError("Invalid arguments for concat; both must be strings.")

def eval_expression(expression):
    expression = expression.strip()

    # Check if the expression is a direct string (no function call)
    if expression.startswith('"') and expression.endswith('"'):
        return expression[1:-1]  # Return the string without quotes

    # Check if the expression is a plain string without parentheses
    if not expression.startswith('(') or not expression.endswith(')'):
        return expression  # Return the plain string directly

    # Remove outer parentheses and split by whitespace
    parts = expression[1:-1].strip().split()
    
    if not parts:
        raise ValueError("Unrecognized expression")
    
    func_name = parts[0]  # The first part is the function name
    args = parts[1:]  # Remaining parts are arguments
    
    if func_name == "puts":
        if len(args) == 1:
            arg = eval_arg(args[0])
            return puts(arg)
        else:
            raise ValueError("puts function requires exactly 1 argument.")
    
    elif func_name == "str":
        if len(args) == 1:
            arg = eval_arg(args[0])
            return str_func(arg)
        else:
            raise ValueError("str function requires exactly 1 argument.")

    elif func_name == "concat":
        if len(args) == 2:
            arg1 = eval_arg(args[0])
            arg2 = eval_arg(args[1])
            return concat(arg1, arg2)
        else:
            raise ValueError("concat function requires exactly 2 arguments.")
    
    raise ValueError("Unrecognized function name or incorrect argument count.")

def eval_arg(arg):
    arg = arg.strip()
    if arg in variables:
        return variables[arg]  # Return the variable's value
    if arg.startswith('"') and arg.endswith('"'):
        return arg[1:-1]  # Return the string without quotes
    elif arg.isdigit() or (arg[1:].isdigit() and arg[0] == '-'):  # Handle integers
        return int(arg)
    raise ValueError(f"Invalid argument: {arg}")

@app.route('/lisp-parser', methods=['POST'])
def lisp_parser():
    data = request.get_json()
    expressions = data.get("expressions", [])
    
    output = []
    for i, expr in enumerate(expressions, 1):
        try:
            result = eval_expression(expr)
            if result is not None:
                output.append(result)
        except Exception as e:
            output.append(f"ERROR: {str(e)} at line {i}")

    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True)
