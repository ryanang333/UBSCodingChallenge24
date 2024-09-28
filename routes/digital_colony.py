from flask import Flask, request, jsonify

app = Flask(__name__)

# Calculate signature of a pair of digits
def calculate_signature(x, y):
    if x == y:
        return 0
    elif x > y:
        return x - y
    else:
        return 10 - (y - x)

# Generate the next generation of the colony
def generate_new_colony(colony):
    weight = sum(int(digit) for digit in colony)
    new_colony = []
    
    # Add the first digit
    new_colony.append(colony[0])
    
    # For each pair of digits, calculate the new digit and grow the colony
    for i in range(len(colony) - 1):
        x = int(colony[i])
        y = int(colony[i + 1])
        signature = calculate_signature(x, y)
        
        # New digit is the last digit of (weight + signature)
        new_digit = (weight + signature) % 10
        
        # Append the new digit between the current pair
        new_colony.append(str(new_digit))
        new_colony.append(colony[i + 1])
    
    return ''.join(new_colony)

# Get the total weight of the colony after the specified number of generations
def get_weight_after_generations(colony, generations):
    current_colony = colony
    
    # Simulate colony growth for the given number of generations
    for _ in range(generations):
        current_colony = generate_new_colony(current_colony)
    
    # Calculate and return the total weight of the final colony
    return sum(int(digit) for digit in current_colony)

# POST endpoint to receive the request and process colony growth
@app.route('/digital-colony', methods=['POST'])
def digital_colony():
    data = request.json
    result = []
    
    # Process each colony in the request
    for item in data:
        generations = item['generations']
        colony = item['colony']
        
        # Get the weight after specified generations
        weight = get_weight_after_generations(colony, generations)
        result.append(str(weight))
    
    # Return the result as a JSON array
    return jsonify(result)

# Entry point to start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
