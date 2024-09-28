from flask import Flask, request, jsonify

app = Flask(__name__)

# Input: Given following text as map with every attempt:
# 1) . means empty area
# 2) u d r l represent bullets with its direction up, down, right, left
# 3) * is where you located
# Sample input: 
# .dd
# r*.
# ...
# Sample output (Expected JSON to be returned):
# {
#  "instructions": ["d", "l"]
# }

# Rule 1: Bullet will move to next cell each time as you moved: E.g:
# ...
# .dd         # Be aware r and middle d is overlapped, r is still there
# .*.

# Rule 2: Bullets can overlap with each other
# Rule 3: You can't dodge towards bullet

# E.g: Given input:
# .d
# d*             # Thus, you can move left to dodge the bullet, you can't move up to dodge the bullet

# If no way to dodge all bullets, pls provide null as instructions:
# {
#    "instructions": null
# }


@app.route('/dodge', methods=['POST'])
def dodge():
    # Ensure the request has the correct Content-Type
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415  # Unsupported Media Type
    
    # Get the map from the request
    data = request.json
    map_string = data.get('map')

    # Validate the input map
    if not map_string:
        return jsonify({"instructions": None}), 400  # Bad Request if map is missing

    # Process the map to find your location and bullets
    instructions = find_dodge_instructions(map_string)
    
    return jsonify({"instructions": instructions})

def find_dodge_instructions(map_string):
    # Parse the input map and find your location and bullets
    lines = map_string.splitlines()
    player_position = None
    bullets = []

    # Locate player position and bullets
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '*':
                player_position = (x, y)
            elif char in 'udrl':
                bullets.append((x, y, char))  # (x, y, direction)

    if player_position is None:
        return None

    # Check possible moves and dodge bullets
    possible_moves = {
        'u': (0, 1),
        'd': (0, -1),
        'l': (-1, 0),
        'r': (1, 0)
    }

    instructions = []
    for direction, (dx, dy) in possible_moves.items():
        new_x = player_position[0] + dx
        new_y = player_position[1] + dy

        # Check boundaries
        if 0 <= new_x < len(lines[0]) and 0 <= new_y < len(lines):
            # Check if moving to this position would result in being hit by bullets
            if not would_be_hit(new_x, new_y, bullets):
                instructions.append(direction)

    # Return null if no valid instructions
    return instructions if instructions else None

def would_be_hit(new_x, new_y, bullets):
    # Check if moving to (new_x, new_y) will get hit by any bullets
    for bullet_x, bullet_y, direction in bullets:
        # Calculate the new position of the bullet based on its movement
        if direction == 'u' and bullet_y == new_y + 1 and bullet_x == new_x:  # Bullet moves up
            return True
        if direction == 'd' and bullet_y == new_y - 1 and bullet_x == new_x:  # Bullet moves down
            return True
        if direction == 'l' and bullet_x == new_x + 1 and bullet_y == new_y:  # Bullet moves left
            return True
        if direction == 'r' and bullet_x == new_x - 1 and bullet_y == new_y:  # Bullet moves right
            return True

    return False



if __name__ == '__main__':
    app.run(debug=True)
