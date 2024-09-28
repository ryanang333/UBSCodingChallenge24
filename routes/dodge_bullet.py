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
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415
    
    data = request.json
    map_string = data.get('map')

    if not map_string:
        return jsonify({"instructions": None}), 400
    
    instructions = find_dodge_instructions(map_string)
    return jsonify({"instructions": instructions})

def find_dodge_instructions(map_string):
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

    # Possible moves from current player position
    possible_moves = {
        'u': (0, -1),
        'd': (0, 1),
        'l': (-1, 0),
        'r': (1, 0)
    }

    # Check each move and simulate bullet movement
    safe_moves = []
    for direction, (dx, dy) in possible_moves.items():
        new_x = player_position[0] + dx
        new_y = player_position[1] + dy

        # Check if the move is within map boundaries
        if 0 <= new_x < len(lines[0]) and 0 <= new_y < len(lines):
            # Simulate bullet movement and check if the new position is safe
            if not will_bullet_hit(new_x, new_y, bullets, len(lines), len(lines[0])):
                safe_moves.append(direction)

    return safe_moves if safe_moves else None

def will_bullet_hit(new_x, new_y, bullets, max_y, max_x):
    # Check if the new position will be hit by any bullet after movement
    for bullet_x, bullet_y, direction in bullets:
        # Simulate the next position of the bullet based on its direction
        if direction == 'u':
            bullet_y = (bullet_y - 1) % max_y
        elif direction == 'd':
            bullet_y = (bullet_y + 1) % max_y
        elif direction == 'l':
            bullet_x = (bullet_x - 1) % max_x
        elif direction == 'r':
            bullet_x = (bullet_x + 1) % max_x

        # Check if the bullet's new position overlaps with the player's new position
        if bullet_x == new_x and bullet_y == new_y:
            return True

    return False

if __name__ == '__main__':
    app.run(debug=True)
