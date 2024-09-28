from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the dodging logic
def dodge_bullets(map_data):
    # Parse the map
    map_lines = map_data.splitlines()
    player_position = None
    bullets = []

    # Find player position and bullets
    for r, line in enumerate(map_lines):
        for c, char in enumerate(line):
            if char == '*':
                player_position = (r, c)
            elif char in 'udrl':
                bullets.append((r, c, char))

    instructions = []
    rows = len(map_lines)
    cols = len(map_lines[0])
    # Define possible moves
    moves = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }

    # Define a function to update bullet positions
    def update_bullets(bullets):
        new_bullets = []
        for r, c, direction in bullets:
            new_r = r + moves[direction][0]
            new_c = c + moves[direction][1]
            if 0 <= new_r < rows and 0 <= new_c < cols:
                new_bullets.append((new_r, new_c, direction))
        return new_bullets

    # Define a function to check if the next position is safe
    def is_safe(next_position, bullets):
        for r, c, direction in bullets:
            next_bullet_position = (r + moves[direction][0], c + moves[direction][1])
            if next_bullet_position == next_position:
                return False
        return True

    # Continue moving until no more moves are possible or player is safe
    while True:
        possible_moves = []
        for direction, (dr, dc) in moves.items():
            new_r = player_position[0] + dr
            new_c = player_position[1] + dc
            new_position = (new_r, new_c)

            # Check if the new position is within bounds and safe
            if 0 <= new_r < rows and 0 <= new_c < cols and is_safe(new_position, bullets):
                possible_moves.append((direction, new_position))

        if not possible_moves:
            break

        # Choose the first possible move (can be optimized further)
        direction, new_position = possible_moves[0]
        instructions.append(direction)
        player_position = new_position

        # Update bullet positions
        bullets = update_bullets(bullets)

    # Return null if no valid instructions
    if not instructions:
        return {"instructions": None}

    return {"instructions": instructions}

@app.route('/dodge', methods=['POST'])
def dodge():
    # Read raw text input
    map_data = request.data.decode('utf-8')
    # Process the map data
    instructions = dodge_bullets(map_data)
    return jsonify(instructions)

if __name__ == '__main__':
    app.run(debug=True)