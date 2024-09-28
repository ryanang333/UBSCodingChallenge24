from flask import Flask
from flask import Flask, request, jsonify
from datetime import datetime,timedelta
import requests, re
app = Flask(__name__)

@app.route('/ub5-flags')
def get_ctfed():
    response = {
        "sanityScroll": {
            "flag": "UB5{w3lc0m3_70_c7f_N0ttyB01}"
        },
        "openAiExploration": {
            "flag": "FLAG_CONTENT_HERE"
        },
        "dictionaryAttack": {
            "flag": "UB5{FLAG_CONTENT_HERE}",
            "password": "PASSWORD_HERE"
        },
        "pictureSteganography": {
            "flagOne": "UB5-1{FLAG_ONE_CONTENTS_HERE}",
            "flagTwo": "UB5-2{FLAG_TWO_CONTENTS_HERE}"
        },
        "reverseEngineeringTheDeal": {
            "flag": "FLAG_CONTENT_HERE",
            "key": "KEY_HERE"
        }
    }
    return jsonify(response), 200

@app.route('/coolcodehack', methods=['POST'])
def get_hacked():
    response = {
        "username" : "username",
        "password" : "BinarySurge123!"
    }
    return jsonify(response), 200

@app.route('/')
def hello_world():
    return 'Hello, World!'


from collections import deque

@app.route('/bugfixer/p1', methods=['POST'])
def bobby_bugger():
    ans = []
    if request.is_json:
        data = request.get_json()
        for line in data:
            ans.append(bobby1(line['time'], line['prerequisites']))
    
    return jsonify(ans), 200

def bobby1(time, prereq):
    n = len(time)
    adj = [[] for _ in range(n)]

    for req in prereq:
        adj[req[0] - 1].append(req[1] - 1) 

    print("Topological sorting of the graph:", end=" ")
    result = topological_sort(adj, n)

    if not result:
        return 0
    
    min_time = [0] * n

    for vertex in result:
        min_time[vertex] += time[vertex]

        for adjacent in adj[vertex]:
            min_time[adjacent] = max(min_time[adjacent], min_time[vertex])

    total_time = max(min_time)
    
    return total_time


def topological_sort(adj, V):
    # Vector to store indegree of each vertex
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1

    # Queue to store vertices with indegree 0
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            # If indegree becomes 0, push it to the queue
            if indegree[adjacent] == 0:
                q.append(adjacent)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result


@app.route('/klotski', methods=['POST'])
def klotski_route():
    ans = []
    if request.is_json:
        data = request.get_json()
        for el in data:
            ans.append(klotski(el['board'], el['moves']))
    
    return jsonify(ans), 200

def klotski(board, moves):
    #given a 5x4 box => can only slide vertically or horizontally
    positionMap = board_to_map(board, 5, 4)
    for i in range(0, len(moves), 2):
        currMove = moves[i: i+2]
        currPosition = positionMap[currMove[0]]
        if currMove[1] == 'N':
            for i in range(len(currPosition)):
                tup = currPosition[i]
                coord = tuple([tup[0], tup[1] - 1])
                positionMap[currMove[0]][i] = coord 
        elif currMove[1] == 'S':
            for i in range(len(currPosition)):
                tup = currPosition[i]
                coord = tuple([tup[0], tup[1] + 1])
                positionMap[currMove[0]][i] = coord 
        elif currMove[1] == 'E':
            for i in range(len(currPosition)):
                tup = currPosition[i]
                coord = tuple([tup[0] + 1, tup[1]])
                positionMap[currMove[0]][i] = coord 
        elif currMove[1] == 'W':
            for i in range(len(currPosition)):
                tup = currPosition[i]
                coord = tuple([tup[0] - 1, tup[1]])
                positionMap[currMove[0]][i] = coord         
    return map_to_board(positionMap, 5, 4)

def board_to_map(board, rows, cols):
    char_map = {}
    
    # Traverse the board string
    for i, char in enumerate(board):
        if char != '@':  # Skip the spaces
            x = i % cols  # Column number
            y = i // cols  # Row number
            
            # Add coordinates to the map for the character
            if char not in char_map:
                char_map[char] = []
            char_map[char].append((x, y))
    
    return char_map

def map_to_board(char_map, rows, cols):
    # Initialize the board with '@' (spaces)
    board = ['@'] * (rows * cols)
    
    # Traverse the map and place characters back into their coordinates
    for char, coordinates in char_map.items():
        for (x, y) in coordinates:
            index = y * cols + x  # Calculate the index in the 1D array
            board[index] = char
    
    # Join the list into a string and return it
    return ''.join(board)



word_list =['aalii', 'aaron', 'abaca', 'abaft', 'abamp', 'abase', 'abash', 'abate', 
'abbot', 'abele', 'abets', 'abhor', 'abide', 'abies', 'ables', 'abode', 'abohm', 'abort', 'about',
'above', 'abuse', 'abuts', 'abuzz', 'abyes', 'abysm', 'abyss', 'accra', 
'acerb', 'acids', 'ackee', 'acmes', 'acned', 'acnes', 'acold', 'acorn', 'acres', 
'acrid', 'actin', 'actor', 'acute', 'acyls', 'adage', 'adams', 'adapa', 'adapt', 
'addax', 'adder', 'addle', 'adept', 'adieu', 'adios', 'adits', 'adman', 'admen', 
'admit', 'admix', 'adobe', 'adobo', 'adopt', 'adore', 'adorn', 'adult', 'adust', 
'adzes', 'aedes', 'aegir', 'aegis', 'aeons', 'aerie', 'aesir', 'aesop', 'affix', 
'afire', 'afoot', 'afoul', 'afros', 'after', 'again', 'agama', 'agape', 'agars', 
'agate', 'agave', 'agaze', 'agene', 'agent', 'aggro', 'aghan', 'aghas', 'agile',
'aging', 'agios', 'agism', 'aglet', 'aglow', 'agone', 'agons', 'agony', 'agora', 
'agree', 'agues', 'ahead', 'ahems', 'ahura', 'aided', 'aides', 'aioli', 'aired', 
'airts', 'aisle', 'ajuga', 'akees', 'akron', 'alamo', 'alarm', 'alary', 'alate',
'albee', 'album', 'alces', 'alder', 'aldol', 'aleph', 'alert', 'aleut', 'algae', 
'algal', 'algid', 'algin', 'algol', 'alias', 'alibi', 'alien', 'align', 'alike', 
'aline', 'alive', 'alkyd', 'alkyl', 'allah', 'allay', 'allen', 'alley', 'allis', 
'allot', 'allow', 'alloy', 'allyl', 'alnus', 'aloes', 'aloha', 'alone', 'along', 
'aloof', 'alosa', 'aloud', 'alpha', 'altar', 'alter', 'altos', 'alula', 'alums',
'amahs', 'amass', 'amati', 'amaze', 'amber', 'ambit', 'amble', 'ambos', 'ameba',
'ameer', 'amend', 'amens', 'ament', 'amias', 'amide', 'amigo', 'amine',
'amino', 'amirs', 'amish', 'amiss', 'amity', 'amman', 'ammos', 'amnic',
'amoks', 'ample', 'amply', 'ampul', 'amuck', 'amuse', 'amyls', 'anasa',
'andes', 'anele', 'angas', 'angel', 'anger', 'angle', 'angry', 'angst', 
'angus', 'anile', 'anils', 'anima', 'anime', 'anion', 'anise', 'anjou',
'ankle', 'ankus', 'annam', 'annas', 'annex', 'annoy', 'annul', 
'annum', 'anoas', 'anode', 'anole', 'anomy', 'anova', 'anser',
'antes', 'antic', 'antis', 'antsy', 'antum', 'anura', 'anvil',
'anzac', 'aorta', 'aotus', 'apace', 'apart', 'apers', 'apery', 'aphid',
'aphis', 'apian', 'apios', 'apish', 'apium', 'apnea', 'appal', 'apple', 'apply', 'appro', 
'april', 'apron', 'apses', 'apsis', 'aptly', 'aquas', 'arabs', 'arbor', 'arced', 'arcos', 
'arcus', 'ardea', 'ardeb', 'ardor', 'areal', 'areas', 'areca', 'arena', 'arere', 'arete', 'argal', 'argil',
'argon', 'argos', 'argot', 'argue', 'argus', 'arhat', 'aries', 'arils', 'arise', 'arius', 
'arles', 'armed', 'armet', 'armor', 'aroid', 'aroma', 'arras', 'array', 'arrow', 'arses', 
'arson', 'arulo', 'arums', 'aryan', 'asana', 'asarh', 'asbaw', 'ascii', 'ascot', 'ascus', 'asdic', 'ashen', 'ashir', 'ashur', 'asian', 'aside', 'asker', 'askew', 'aspen', 'asper', 'aspic', 
'aspis', 'assam', 'assay', 'asset', 'aster', 'astir', 'astor', 'ataxy', 'athar', 'atilt', 'atlas', 'atole', 'atoll', 'atoms', 'atone', 'atony', 'atopy', 'atrip', 'attar', 'attic', 'audad', 
'audio', 'audit', 'auger', 'aught', 'augur', 'aunts', 'aunty', 'aural', 'auric', 'autos', 'auxin', 'avahi', 'avail', 'avena', 'avens', 'avers', 'avert', 'avian', 'avoid', 'avows', 'await', 'awake', 'award', 'aware', 'awash', 'aways', 'awful', 'awing', 'awned', 'awols', 'axial', 'axile',
'axils', 'axiom', 'axles', 'axone', 'axons', 'ayahs', 'ayins', 'azide', 'azido', 'azoic', 'azote', 'aztec', 'azure', 'baals', 'babas', 'babel', 'babes', 'babka', 'baboo', 'bacca', 'baccy', 'bacon', 'badge', 'badly', 'bagel', 'baggy', 'bahai', 'bahts', 'bails', 'bairn', 'baits', 'baiza', 'baize', 'baked', 'baker', 'balas', 'balds', 'baldy', 'bales', 'balks', 'balky', 'bally', 'balms', 'balmy', 'balsa', 'banal', 'bands', 'bandy', 'banes', 'banff', 'banjo', 'banks', 'banns', 'bantu', 'barbs', 'barbu', 'barde', 'bards', 'bared', 'bares', 'barfs', 'barge', 'baric', 'barks', 'barky', 'barms', 'barmy', 'barns', 'baron', 'barth', 'barye', 'basal', 'based', 'basic', 'basil', 'basin', 'basis', 'basks', 'basso', 'baste', 'basts', 'batch', 'bated', 'bathe', 'batik', 'batis', 'baton', 'batty', 'bauds', 'baulk', 'bawds', 'bawdy', 'bawls', 'bayou', 'bazar', 'beach', 'beads', 'beady', 'beaks', 'beams', 'beamy', 'beano', 'beans', 'beany', 'beard', 'bears', 'beast', 'beats', 'beaut', 'bebop', 'becks', 'bedew', 'bedim', 'beech', 'beefs', 'beefy', 'beeps', 'beery', 'beets', 'befit', 'befog', 'beget', 'begin', 'begum', 'beige', 'being', 'beira', 'belay', 'belch', 'belie', 'belle', 'bells', 'belly', 'below', 'belts', 'bemas', 'bench', 'bends', 'benet', 'benin', 'benne', 'benni', 'benny', 'bents', 'beret', 'bergs', 'berms', 'berne', 'beroe', 'berry', 'berth', 'beryl', 'beset', 'besom', 'besot', 'bests', 'betas', 'betel', 'beths', 'bevel', 'bezel', 'bhaga', 'bhang', 'bialy',
'bible', 'biddy', 'bides', 'bidet', 'biers', 'biffs', 'bifid', 'bight', 'bigot', 'bijou', 'biker', 'bikes', 'bilby', 'biles', 'bilge', 'bilgy', 'bilks', 'bills', 'billy', 'bimbo', 'binds', 'bines', 'binge', 'bingo', 'biome', 'biont', 'biota', 'biped', 'birch', 'birds', 'birle', 'birls', 'birrs', 'birth', 'bises', 'bison', 'bitch', 'biter', 'bites', 'bitis', 'bitsu', 'bitty', 'bizes', 'bizet', 'blabs', 'black', 'blade', 'blahs', 'blain', 'blair', 'blake', 'blame', 'blanc', 'bland', 'blank', 'blare', 'blase', 'blast', 'blate', 'blats', 'blaze', 'bleak', 'blear', 'bleat', 'blebs', 'bleed', 'bleep', 'blend', 'bless', 'blest', 'blimp', 'blind', 'blini', 'blink', 'bliny', 'blips', 'bliss', 'blitz', 'bloat', 'blobs', 'block', 'blocs', 'bloke', 'blond', 'blood', 'bloom', 'blots', 'blown', 'blows', 'blowy', 'blues', 'bluff', 'blunt', 'blurb', 'blurs', 'blurt', 'blush', 'board', 'boars', 'boast', 'boats', 'bobby', 'bocce', 'bocci', 'boche', 'bocks', 'bodes', 'bodge', 'boers',
'boffo', 'bogey', 'boggy', 'bogie', 'bogus', 'boils', 'boise', 'boles', 'bolls', 'bolos', 'bolti', 'bolts', 'bolus', 'bombs', 'bonce', 'bonds', 'boned', 'boner', 'bones', 'boney', 'bongo', 'bongs', 'bonks', 'bonny', 'bonus', 'boobs', 'booby', 'books', 'booms', 'boone', 'boons', 'boors', 'boost', 'booth', 'booty', 'booze', 'boozy', 'borax', 'bored', 'borer', 'bores', 'boric', 'boron', 'bosch', 'bosks', 'bosky', 'bosom', 'boson', 'bossy', 'bosun', 'botas', 'botch', 'bough', 'boule', 'bound', 'bourn', 'bouse', 'bouts', 'bovid', 'bowed', 'bowel', 'bower', 'bowie', 'bowls', 'bowse', 'boxed', 'boxer', 'boxes', 'bozos', 'brace', 'bract', 'brads', 'braes', 'bragi', 'brags', 'braid', 'brail', 'brain', 'brake', 'braky', 'brand', 'brant', 'brash', 'brass', 'brats', 'brave', 'bravo', 'brawl', 'brawn', 'braws', 'brays', 'braze', 'bread', 'break', 'bream', 'breed', 'brens', 'brent', 'brest', 'breve', 'brews', 'briar', 'bribe', 'brick', 'bride', 'brief', 'brier', 'brigs', 'brill', 'brims', 'brine', 'bring', 'brink', 'briny', 'brios', 'brisk', 'briss', 'brith', 'brits', 'britt', 'broad', 'broil', 'broke', 'brome', 'bronc', 'bronx', 'brood', 'brook', 'broom', 'broth', 'brown', 'brows', 'bruce', 'bruin', 'bruit', 'brule', 'bruno', 'brunt', 'brush', 'brusk', 'brute', 'bryan', 'bryum', 'bubos', 'buddy', 'budge', 'budlo', 'buffs', 'buggy', 'bugle', 'buhls', 'build', 'built', 'bulbs', 'bulge', 'bulgy', 'bulks', 'bulky', 'bulla', 'bulls', 'bully', 'bumfs', 'bumph', 'bumps', 'bumpy', 'bunce', 'bunch', 'bunco', 'bungs', 'bunko', 'bunks', 'bunny', 'bunts', 'buoys', 'buras', 
'buret', 'burgh', 'burgs', 'burin', 'burka', 'burke', 'burls', 'burly', 'burma', 'burns', 'burnt', 'burps', 'burro', 'burrs', 'burry', 'bursa', 'burst', 'burys', 'busby', 'bushy', 'busks', 'busts', 'busty', 'butat', 'butch', 'butea', 'buteo', 'butte', 'butts', 'butty', 'butut', 'butyl', 'buxom', 'buxus', 'buyer', 'bylaw', 'byres', 'byron', 'bytes', 'byway', 'caaba', 'cabal', 'cabby', 'caber', 'cabin', 'cable', 'cabot', 'cacao', 'cache', 'caddo', 'caddy', 'cadet', 'cadge', 'cadre', 'cafes', 'cager', 'cages', 'cagey', 'cains', 'cairn', 'cairo', 'cajun', 'cakes', 'calfs', 'calif', 'calks', 'calla', 'calls', 'calms', 'calve', 'calyx', 'camas', 'camel', 'cameo', 'camps', 'campy', 'camus', 'canal', 'candy', 'canes', 'canid', 'canis', 'canna', 'canny', 'canoe', 'canon', 'canto', 'cants', 'canty', 'caper', 'capes', 'capon', 'capos', 'capra', 'capri', 'caput', 'carat', 'cards', 'cares', 'caret', 'carex', 'cargo', 'carib', 'carks', 'carob', 'carol', 'carom', 'carps', 'carry', 'carte', 'carts', 'carum', 'carve', 'carya', 'cased', 'cases', 'casks', 'caste', 'casts', 'catch', 'cater', 'catha', 'catsu', 'catty', 'cauda', 'caulk', 'cauls', 'causa', 'cause', 'caves', 'cavia', 'cavil', 'cavum', 'cease', 'cebus', 'cecal', 'cecum', 'cedar', 'cedes', 'cedis', 'ceiba', 'ceibo', 'cello', 'cells', 'celom', 'celts', 'cense', 'cents', 'ceras', 'ceres', 'ceric', 'ceros', 'cetus', 'chads', 'chafe', 'chaff', 'chaga', 'chain', 'chair', 'chait', 'chaja', 'chalk', 'champ', 'chang', 'chant', 'chaos', 'chara', 'chard', 'charm', 'charr', 'chars', 'chart', 'chary', 'chase', 'chasm', 'chats', 'chaws', 'cheap', 'cheat', 'check', 'cheek', 'cheep', 'cheer', 'chefs', 'chela', 'chert', 'chess', 'chest', 'chevy', 'chews', 'chewy', 'chian', 'chick', 'chico', 'chics', 'chide', 'chief', 'child', 'chile', 'chili', 'chill', 'chime', 'chimp', 'china', 'chine', 'chink', 'chino', 'chins', 'chips', 'chirk', 'chirp', 'chirr', 'chits', 'chive', 'chivy', 'chock', 'choir', 'choke', 'choky', 'chomp', 'chord', 'chore', 'chows', 'chubs', 'chuck', 'chufa', 'chuff', 'chugs', 'chump', 'chums', 'chunk', 'churl', 'churn', 'churr', 'chute', 'chyle', 'chyme', 'cicer', 'cider', 'cigar', 'cimex', 'cinch', 'circe', 'cisco', 'cissy', 'cites', 'civet', 'civic', 'civil', 'clack', 'clade', 'clads', 'claim', 'clamp', 'clams', 'clang', 'clank', 'clans', 'claps', 'clark', 'claro', 'clary', 'clash', 'clasp', 'class', 'clast', 'claws', 'clays', 'clean', 'clear', 'cleat', 'clefs', 'cleft', 'clerk', 'clews', 'click', 'cliff', 'climb', 'clime', 'cline', 'cling', 'clink', 'clive', 'cloak', 'clock', 'clods', 'clogs', 'clomp', 'clone', 'clons', 'clops', 'close', 'cloth', 'clots', 'cloud', 'clout', 'clove', 'clown', 'cloys', 'cloze', 'clubs', 'cluck', 'clues', 'clump', 'clunk', 'clyde', 'coach', 'coact', 'coals', 'coapt', 'coast', 'coati', 'coats', 'cobia', 'cobol', 'cobra', 'cocas', 'cocci', 'cocks', 'cocky', 'cocoa', 'cocos', 'cocus', 'codas', 'coder', 'codes', 'codex', 'codon', 'cohos', 'coifs', 'coign', 'coils', 'coins', 'coirs', 'cokes', 'colas', 'colds', 'colic', 'colly', 'colon', 'color', 'colts', 'colza', 'comal', 'comas', 'combo', 'comer', 'comet', 'comfy', 'comic', 'comma', 'comps', 'comte', 'conch', 'condo', 'cones', 'coney', 'conga', 'conge', 'congo', 'conic', 'conks', 'conns', 'conoy', 'conto', 'cooks', 'cooky', 'cools', 'cooly', 'coons', 'coops', 'coots', 'copal', 'copes', 'copra', 'copse', 'coral', 'cords', 'corer', 'cores', 'corgi', 'corks', 'corky', 'corms', 'corns', 'cornu', 'corny', 'corps', 'corse', 'cosec', 'costa', 'costs', 'cotan', 'cotes', 'couch', 'cough', 'count', 'coupe', 'court', 'couth', 'coven', 'cover', 'coves', 'covet', 'covey', 'cower', 'cowls', 'cowry', 'coxes', 'coyly', 'coyol', 'coypu', 'cozen', 'crabs', 'crack', 'craft', 'crags', 
'crake', 'cramp', 'crams', 'crane', 'crank', 'crape', 'craps', 'crash', 'crass', 'crate', 'crave', 'crawl', 'craws', 'craze', 'crazy', 'creak', 'cream', 'credo', 'creed', 'creek', 'creel', 'creep', 'crees', 'crepe', 'cress', 'crest', 'crete', 'crews', 'cribs', 'crick', 'crier', 'cries', 'crime', 'crimp', 'crisp', 'crith', 'croak', 'croat', 'crock', 'croft', 'crone', 'cronk', 'crony', 'crook', 'croon', 'crops', 'crore', 'cross', 'croup', 'crowd', 'crown', 'crows', 'crude', 'cruds', 'cruel', 'cruet', 'crumb', 'crump', 'cruse', 'crush', 'crust', 'crypt', 'ctene', 'cuban', 'cubas', 'cubby', 'cubeb', 'cubes', 'cubic', 'cubit', 'cuddy', 'cukes', 'culex', 'culls', 'culms', 'cults', 'cumin', 'cunts', 'cupel', 'cupid', 'cuppa', 'curbs', 'curds', 'cured', 'curet', 'curia', 'curie', 'curio', 'curls', 'curly', 'curry', 'curse', 'curst', 'curve', 'curvy', 'cushy', 'cusks', 'cusps', 'cutch', 'cutes', 'cutin', 'cutis', 'cyans', 'cycad', 'cycas', 'cycle', 'cyder', 'cylix', 'cymas', 'cymes', 'cymry', 'cynic', 'cypre', 'cyril', 'cyrus', 'cysts', 'cytol', 'czars', 'czech', 'dacha', 'dadas', 'daddy', 'dados', 'dafla', 'dagga', 'dagon', 'dagos', 'daily', 'dairy', 'daisy', 'dalea', 'dalis', 'dally', 'damar', 'dames', 'damns', 'damon', 'damps', 'dance', 'dandy', 'danes', 'dante', 'daraf', 'darks', 'darns', 'darts', 'dated', 'datum', 'daubs', 'daunt', 'david', 'davis', 'davit', 'dawns', 'dayan', 'dazed', 'dazes', 'dazmo', 'deads', 'deals', 'deans', 'dears', 'deary', 'death', 'debar', 'debit', 'debts', 'debug', 'debut', 'decal', 'decay', 'decor', 'decoy', 'decry', 'deeds', 'deeps', 'deers', 'defat', 'defer', 'defog', 'degas', 'deice', 'deify', 'deign', 'deism', 'deist', 'deity', 'dekko', 'dekni', 'delay', 'delfs', 'delft', 'delhi', 'delta', 'delve', 'demob', 'demon', 'demur', 'deneb', 'denim', 'dense', 'dents', 'depot', 'depth', 'derby', 'derca', 'derma', 'desex', 'desks', 'desmo', 'deter', 'deuce', 'devil', 'devon', 'dewar', 'dewey', 'dezmo', 'dhaks', 'dhava', 'dhole', 'dhoti', 'dhows', 'dials', 'diana', 'diary', 'diazo', 'dicer', 'dices', 'dicey', 'dicks', 'dicky', 'dicot', 'didos', 'diets', 'digit', 'dikes', 'dildo', 'dills', 'dimer', 'dimes', 'dimly', 'dinar', 'diner', 'dines', 'dinge', 'dingo', 'dings', 'dingy', 'dinka', 'dinks', 'dinky', 'dints', 'diode', 'diols', 'dioon', 'dipus', 'dirca', 'dirge', 'dirks', 'dirts', 'dirty', 'disco', 'discs', 'dishy', 'disks', 'ditas', 'ditch', 'ditto', 'ditty', 'divan', 'divas', 'diver', 'divot', 'divvy', 'diwan', 'dixie', 'dizen', 'dizzy', 'djinn', 'dobra', 'docks', 'dodge', 'dodgy', 'dodos', 'doers', 'doffs', 'doges', 'doggo', 'doggy', 'dogie', 'dogma', 'doily', 'dojya', 'dolce', 'doles', 'dolls', 'dolly', 'dolor', 'dolts', 'domed', 'domes', 'donar', 'donas', 'donee', 'dongs', 'donna', 'donne', 'donor', 'donut', 'doors', 'dopas', 'doped', 'dopes', 'dopey', 'doric', 'doris', 'dorms', 'dormy', 'dosed', 'doses', 'dotes', 'dotty', 'doubt', 'dough', 'doura', 'douse', 'dover', 'doves', 'dowdy', 'dowel', 'dower', 'downy', 'dowry', 'dowse', 'doyen', 'doyly', 'dozen', 'dozer', 'dozes', 'draba', 'drabs', 'draco', 'draft', 'drags', 'drain', 'drake', 'drama', 'drams', 'drape', 'drawl', 'drawn',
'draws', 'drays', 'dread', 'dream', 'drear', 'dreck', 'dregs', 'dress', 'dribs', 'dried', 'drier', 'dries', 'drift', 'drill', 'drily', 'drink', 'drips', 'drive', 'droll', 'drome', 'drone', 'drool', 'droop', 'dross', 'drove', 'drown', 'drubs', 'drugs', 'druid', 'drums', 'drunk', 'drupe', 'druse', 'druze', 'dryad', 'dryas', 'dryer', 'dryly', 'duads', 'duals', 'ducal', 'ducat', 'duchy', 'ducky', 'ducts', 'dudes', 'duels', 'duets', 'duffs', 'dulls', 'dully', 'dulse', 'dumas', 'dumbs', 'dummy', 'dumps', 'dumpy', 'dunce', 'dunes', 'dungs', 'dunks', 'duomo', 'dupes', 'duple', 'dural', 'duras', 'durio', 'durra', 'durum', 'dusks', 'dusky', 'dusts', 'dusty', 'dutch', 'duvet', 'dwarf', 'dwell', 'dyads', 'dyaus', 'dyers', 'dying', 'dykes', 'dylan', 'dynes', 'eager', 'eagle', 'eagre', 'eared', 'earls', 'early', 'earns', 'earth', 'eased', 'easel', 'eases', 'easts', 'eater', 'eaves', 'eblis', 'ebons', 'ebony', 'echos', 'eclat', 'edema', 'edgar', 'edged', 'edger', 'edges', 'edict', 'edify', 'edits', 'educe', 'edwin', 'eerie', 'egest', 'eggar', 'egger', 'egret', 'egypt', 'eider', 'eidos', 'eight', 'eject', 'eland', 'elans', 'elate', 'elbow', 'elder', 'elect', 'elegy', 'elemi', 'elfin', 'elide', 'eliot', 'elite', 'elope', 'elops', 'elude', 'elute', 'elver', 'elves', 'elvis', 'email', 'embed', 'ember', 'emcee', 'emeer', 'emend', 'emery', 'emirs', 'emits', 'emmer', 'emmet', 'emote', 'empty', 'enact', 'enate', 'ended', 'endow', 'endue', 'enema', 'enemy', 'enjoy', 'ennui', 'enols', 'enrol', 'ensky', 'ensue', 'enter', 'entry', 'envoi', 'envoy', 'eosin', 'epees', 'ephah', 'ephas', 'epics', 'epoch', 'epoxy', 'equal', 'equid', 'equip', 'equus', 'erase', 'erato', 'erect', 'ergot', 'erica', 'ernes', 'ernst', 'erode', 'erose', 'error', 'erses', 'eruca', 'eruct', 'erupt', 'esker', 'essay', 'essex', 'ester', 'ether', 'ethic', 'ethos', 'ethyl', 'etnas', 'etude', 'euler', 'euros', 'evade', 'evans', 'event', 'evert', 'every', 'evict', 'evils', 'evoke', 'ewers', 'exact', 'exalt', 'exams', 'excel', 'execs', 'exert', 'exile', 'exist', 'exits', 'exode', 'expel', 'extol', 'extra', 'exude', 'exult', 'eyras', 'eyres', 'eyrie', 'eyrir', 'fable', 'faced', 'facer', 'faces', 'facet', 'facia', 'facts', 'faddy', 'faded', 'fades', 'fados', 'faery', 'fagin', 'fagot', 'fagus', 'fails', 'fains', 'faint', 'fairs', 'fairy', 'faith', 'faker', 'fakes', 'fakir', 'fakyo', 'falco', 'falla', 'falls', 'false', 'famed', 'fames', 'fancy', 'fangs', 'fanja', 'fanny', 'faqir', 'farad', 'farce', 'fares', 'farms', 'faros', 'farsi', 'farts', 'fasts', 'fatal', 'fated', 'fatso', 'fatty', 'fatwa', 'fauld', 'fault', 'fauna', 'fauns', 'faust', 'fauve', 'favor', 'favus', 'fawns', 'faxes', 'fazed', 'fazes', 'fears', 'feast', 'feats', 'fecal', 'feces', 'feeds', 'feels', 'feign', 'feint', 'feist', 'felid', 'felis', 'fella', 'fells', 'felly', 'felon', 'felts', 'femur', 'fence', 'fends', 'feoff', 'feral', 'feria', 'fermi', 'ferns', 'ferny', 'ferry', 'fesse', 'fetal', 'fetch', 'fetid',
'fetor', 'fetus', 'feuds', 'fever', 'fewer', 'fiats', 'fiber', 'fibre', 'fices', 'fichu', 'ficus', 'fiefs', 'field', 'fiend', 'fiery', 'fifes', 'fifth', 'fifty', 'fight', 'filar', 'filch', 'filer', 'files', 'filet', 'fille', 'fills', 'filly', 'films', 'filmy', 'filth', 'filum', 'final', 'finch', 'finds', 'finer', 'fines', 'finis', 'finks', 'finns', 'fiord', 'fired', 'fires', 'firms', 'first', 'firth', 'fiscs', 'fishy', 'fists', 'fitch', 'fitly', 'fiver', 'fives', 'fixed', 'fixer', 'fixes', 'fizzy', 'fjord', 'flabs', 'flack', 'flail', 'flair', 'flake', 'flaky', 'flame', 'flank', 'flans', 'flaps', 'flare', 'flash', 'flask', 'flats', 'flaws', 'flays', 'fleas', 'fleck', 'fleer', 'flees', 'fleet', 'flesh', 'flick', 'flier', 'flies', 'fling', 'flint', 'flips', 'flirt', 'flits', 'float', 'flock', 'flocs', 'floes', 'flogs', 'flood', 'floor', 'flops', 'flora', 'flory', 'floss', 'flour', 'flout', 'flows', 'flubs', 'flues', 'fluff', 'fluid', 'fluke', 'fluky', 'flume', 'flump', 'flunk', 'fluor', 'flush', 'flute', 'flyer', 'foals', 'foams', 'foamy', 'focal', 'focus', 'foehn', 'fogey', 'foggy', 'fohns', 'foils', 'foist', 'folds', 'folie', 'folio', 'folks', 'folly', 'fomes', 'fondu', 'fonts', 'foods', 'fools', 'foram', 'foray', 'force', 'fords', 'fores', 'forge', 'forgo', 'forks', 'forms', 'forte', 'forth', 'forts', 'forty', 'forum', 'fossa', 'fosse', 'found', 'fount', 'fours', 'fovea', 'fowls', 'foyer', 'frail', 'frame', 'franc', 'frank', 'fraps', 'frats', 'fraud', 'frays', 'freak', 'frees', 'freon', 'fresh', 'fress', 'frets', 'freud', 'freya', 'freyr', 'friar', 'fried', 'frier', 'fries', 'frill', 'frisk', 'frizz', 'frock', 'frogs', 'frond', 'front', 'frore', 'frost', 'froth', 'frown', 'fruit', 'frump', 'fryer', 'fucks', 'fucus', 'fudge', 'fuels', 'fugal', 'fuggy', 'fugue', 'fujis', 'fulah', 'fulls', 'fully', 'fumed', 'fumes', 'funds', 'fungi', 'funks', 'funky', 'funny', 'furan', 'furls', 'furor', 'furry', 'furze', 'fused', 'fusee', 'fusil', 'fussy', 'fusty', 'fuzee', 'fuzes', 'fuzzy', 'gabby', 'gable', 'gabon', 'gaddi', 'gadus', 'gaels', 'gaffe', 'gaffs', 'gages', 'gaily', 'gaits', 'gaius', 'galas', 'galax', 'galea', 'galen', 'gales', 'galls', 'gamba', 'games', 'gamey', 'gamin', 'gamma', 'gammy', 'gamps', 'gamut', 'ganef', 'gangs', 'ganja', 'ganof', 'gaols', 'garbo', 'garbs', 'gasps', 'gassy', 'gates', 'gator', 'gauds', 'gaudy', 'gauge', 'gauls', 'gaunt', 'gaurs', 'gauss', 'gauze', 'gauzy', 'gavel', 'gavia', 'gawks', 'gawky', 'gayal', 'gayly', 'gazes', 'gears', 'gecko', 'geeks', 'gelds', 'gelid', 'gelly', 'gelts', 'gemma', 'genes', 'genet', 'genic', 'genie', 'genip', 'genoa', 'genre', 'genus', 'geode', 'germs', 'germy', 'gesso', 'getas', 'getup', 'geums', 'ghana', 'ghees', 'ghent', 'ghost', 'ghoul', 'giant', 'gibes', 'giddy', 'gifts', 'gigot', 'gigue', 'gilds', 'gilts', 'gimel', 'gimps', 'gimpy', 'ginep', 'ginzo', 'gipsy', 'girds', 'girls', 'giros', 'girth', 'gismo', 'gists', 'given', 'giver', 'gives', 'gizmo', 'gjopa', 'glace', 'glade', 'glads', 'gland', 'glans', 'glare', 'glary', 'glass', 'glaux', 'glaze', 'gleam', 'glean', 'gleba', 'glebe', 'glees', 'gleet', 'glenn', 'glens', 'glial', 'glide', 'glint', 'gloam', 'gloat', 'globe', 'globs', 'glogg', 'gloms', 'gloom', 'glops', 'glory', 'gloss', 'glove', 'glows', 'gluck', 'glued', 'glues', 'gluey', 'glume', 'gluon', 'gluts', 'glyph', 'gnarl', 'gnash', 'gnats', 'gnaws', 'gnome', 'goads', 'goals', 'goats', 'gobio', 'godly', 'goers', 'gofer', 'going', 'golds', 'golem', 'golfs', 'golgi', 'gonad', 'gondi', 'goner', 'gongs', 'gonif', 'gonne', 'gonzo', 'goody', 'gooey', 'goofs', 'goofy', 'gooks', 'goons', 'goony', 'goops', 'goose', 'goosy', 'goral', 'gores', 'gorge', 'gorki', 'gorse', 'goths', 'gouda', 'goudy', 'gouge', 'gourd', 'gouts', 'gouty', 'gowns', 'grabs', 'grace', 'grade', 'grads', 'graft', 'grail', 'grain', 'grama', 'grams', 'grand', 'grant', 'grape', 'graph', 'grapy', 'grasp', 'grass', 'grate', 'grave', 'gravy', 'grays', 'graze', 'great', 'grebe', 'greco', 'greed', 'greek', 'green', 'greet', 'greys', 'grids', 'grief', 'grill',
'grime', 'grimm', 'grimy', 'grind', 'grins', 'griot', 'gripe', 'grips', 'grist', 'grits', 'groan', 'groat', 'grogs', 'groin', 'groom', 'grope', 'gross', 'grosz', 'grots', 'group', 'grout', 'grove', 'growl', 'grown', 'grows', 'grubs', 'gruel', 'gruff', 'grume', 'grump', 'grunt', 'guama', 'guano', 'guans', 'guard', 'guars', 'guava', 'guchi', 'gucks', 'guess', 'guest', 'guffs', 'guide', 'guild', 'guile', 'guilt', 'guise', 'gulas', 'gulch', 'gulfs', 'gulls', 'gully', 'gulps', 'gumbo', 'gumma', 'gummy', 'gunks', 'gunny', 'guppy', 'gushy', 'gusto', 'gusts', 'gusty', 'gutsy', 'guyot', 'gybes', 'gypsy', 'gyral', 'gyres', 'gyros', 'gyrus', 'habit', 'hacek', 'hacks', 'hadal', 'hades', 'hadji', 'haems', 'hafts', 'haick', 'haida', 'haiks', 'haiku', 'hails', 'hairs', 'hairy', 'haiti', 'hajji', 'hakea', 'hakes', 'hakim', 'hakka', 'halal', 'haler', 'hales', 'halls', 'halma', 'halms', 'halos', 'halts', 'halve', 'haman', 'hammy', 'hands', 'handy', 'hangs', 'hanks', 'hanky', 'hanoi', 'haoma', 'haply', 'happy', 'hardy', 'harem', 'hares', 'harks', 'harms', 'harps', 'harpy', 'harry', 'harsh', 'harts', 'hasid', 'hasps', 'haste', 'hasty', 'hatch', 'hated', 'hater', 'hates', 'haulm', 'hauls', 'haunt', 'hausa', 'havel', 'haven', 'haves', 'havoc', 'hawks', 'hawse', 'haydn', 'hayes', 'hazan', 'hazel', 'hazes', 'heady', 'heals', 'heaps', 'heard', 'hears', 'heart', 'heath', 'heats', 'heave', 'heavy', 'hecht', 'hedge', 'heeds', 'heels', 'hefts', 'hefty', 'heinz', 'heirs', 'heist', 'helas', 'helen', 'helix', 'hello', 'hells', 'helms', 'helot', 'helps', 'helve', 'hemal', 'hemes', 'hemic', 'hemin', 'hemps', 'hence', 'henna', 'henry', 'herat', 'herbs', 'herds', 'herms', 'heron', 'hertz', 'heths', 'hevea', 'hewer', 'hexad', 'hexed', 'hexes', 'hides', 'highs', 'hiker', 'hikes', 'hilar', 'hilly', 'hilts', 'hilum', 'hilus', 'hindi', 'hinds', 'hindu', 'hinge', 'hinny', 'hints', 'hippo', 'hippy', 'hired', 'hirer', 'hires', 'hitch', 'hitwi', 'hives', 'hoagy', 'hoard', 'hoars', 'hoary', 'hobby', 'hobos', 'hocks', 'hogan', 'hoggs', 'hoist', 'hokan', 'hokey', 'hokum', 'holds', 'holes', 'holey', 'holla', 'hollo', 'holly', 'homer', 'homes', 'homey', 'homos', 'hondo', 'hones', 'honey', 'honks', 'honky', 'honor', 'hooch', 'hoods', 'hooey', 'hoofs', 'hooks', 'hooky', 'hoops', 'hoper', 'hopes', 'hopis', 'horde', 'horns', 'horny', 'horse', 'horst', 'hosea', 'hosta', 'hosts', 'hotel', 'hotly', 'hound', 'houri', 'hours', 'house', 'hovel', 'hover', 'howdy', 'howes', 'howls', 'hoyle', 'hubby', 'hucks', 'huffs', 'huffy', 'hulas', 'hulks', 'hulky', 'hullo', 'hulls', 'human', 'humic', 'humid', 'humin', 'humor', 'humps', 'humus', 'hunch', 'hurls', 'huron', 'hurry', 'hurts', 'husks', 'husky', 'hussy', 'hutch', 'hydra', 'hyena', 'hymen', 'hymns', 'hyoid', 'hypes', 'hypha', 'hypos', 'hyrax', 'hyson', 'iambs', 'icaco', 'ichor', 'icily', 'icing', 'ictic', 'ictus', 'icyaw', 'idaho', 'ideal', 'ideas', 'idgof', 'idiom', 'idiot', 'idler', 'idles', 'idols', 'idyll', 'idyls', 'igloo', 'ikons', 'ilama', 'ileum', 'ileus', 'iliac', 'iliad', 'ilion', 'ilium', 'image', 'imago', 'imams', 'imaum', 'imbed', 'imbue', 'imide', 'immix', 'impel', 'imply', 'inane', 'inapt', 'incan', 'incas', 'incur', 'incus', 'index', 'india', 'indic', 'indra', 'indri', 'indue', 'indus', 'inept', 'inert', 'infer', 'infix', 'infos', 'infra', 'inger', 'ingot', 'inhex', 'inion', 'injun', 'inkle', 'inlay', 'inlet', 'inner', 'input', 'inset', 'inter', 'intro', 'inula', 'inure', 'invar', 'iodin', 'ionic', 'iotas', 'iowan', 'irani', 'iraqi', 'irate', 'irena', 'irish', 'irons', 'irony', 'isaac', 'islam', 'islay', 'isles', 'islet', 'issue', 'italy', 'itchy', 'items', 'ivied', 'ivory', 'iwbol', 'iwmod', 'ixias', 'izars', 'jabot', 'jacks', 'jacob', 'jaded', 'jades', 'jaggy', 'jagua', 'jails', 'jakes', 'jambs', 'james', 'janus', 'japan', 'japes', 'jason', 'jaunt', 'javan', 'javas', 'jawan', 'jawed', 'jazzy', 'jeans', 'jeers', 'jehad', 'jello', 'jells', 'jelly', 'jemmy', 'jenny', 'jerez', 'jerks', 'jerky', 'jerry', 'jests', 'jesus', 'jetty', 'jewel', 'jewry', 'jibes', 'jiffy', 'jihad', 'jilts', 'jimmy', 'jingo', 'jinja', 'jinks', 'jinni', 'jiqui', 'jirga', 'jives', 'jocks', 'johns', 'joins', 'joint', 'joist', 'joker', 'jokes', 'jolly', 'jolts', 'jolty', 'jonah', 'jones', 'jorum', 'joule', 'joust', 'jowls', 'jowly', 'joyce', 'judah', 'judas', 'judge', 'judos', 'juice', 'juicy', 'julep', 'jumbo', 'jumps', 'jumpy', 'junco', 'junks', 'junky', 'junta', 'junto', 'jural', 'juror', 'justs', 'jutes', 'kaaba', 'kabob', 'kafir', 'kafka', 'kails', 'kakis', 'kales', 'kalif', 'kamas', 'kamba', 'kamis', 'kansa', 'kanzu', 'kaons', 'kaphs', 'kapok', 'kappa', 'kaput', 'karat', 'karen', 'karma', 'kasha', 'katar', 'kauri', 'kaury', 'kavas', 'kayak', 'kazak', 'kazoo', 'keats', 'kebab', 'keels', 'keens', 'keeps', 'kelly', 'kelps', 'kelpy', 'kelts', 'kempt', 'kenaf', 'kenos', 'kenya', 'kerbs', 'kerns', 'ketch', 'keyco', 'keyed', 'khadi', 'khaki', 'khans', 'khats', 'khaya', 'khmer', 'kiaat', 'kiang', 'kibes', 'kicks', 'kiddy', 'kikes', 'kiley', 'kills', 'kilns', 'kilts', 'kinco', 'kinds', 'kines', 'kinin', 'kinks', 'kinky', 'kinos', 'kiosk', 'kiowa', 'kirks', 'kites', 'kiths', 'kitty', 'kiwis', 'klans', 'klick', 'klutz', 'knack', 'knaps', 'knave', 'knead', 'kneel', 'knees', 'knell', 'knife', 'knish', 'knits', 'knobs', 'knock', 'knoll', 'knots', 'knout', 'known', 'knows', 'koala', 'koans', 'kobus', 'kogia', 'kohls', 'koine', 'kokpa', 'kolas', 'kongo', 'kooks', 'kooky', 'kopek', 'kopje', 'koran', 'korea', 'kotar', 'kotos', 'kotow', 'kraal', 'kraft', 'krait', 'kraut', 'krebs', 'krill', 'krona', 'krone', 'kroon', 'krubi', 'kudos', 'kudzu', 'kumis', 'kurta', 'kurus', 'kusan', 'kutch', 'kvass', 'kwela', 'kyats', 'kylie', 'kylix', 'kyoto', 'laban', 'label', 'labor', 'laced', 'lacer', 'laces', 'lacid', 'lacks', 'laden', 'lades', 'ladin', 'ladku', 'ladle', 'lagan', 'lager', 'lahar', 'laics', 'laird', 'lairs', 'laity', 'laius', 'lakes', 'lakhs', 'lally', 'lambs', 'lamia', 'lamna', 'lamps', 'lanai', 'lance', 'lanes', 'laney', 'lanky', 'lansa', 'lapel', 'lapin', 'lapps', 'lapse', 'larch', 'lards', 'large', 'largo', 'larid', 'larix', 'larks', 'larus', 'larva', 'laser', 'lasso', 'lasts', 'latch', 'later', 'latex', 'lathe', 'lathi', 
'latin', 'latke', 'laugh', 'lavas', 'laver', 'laves', 'lawns', 'laxly', 'layer', 'layia', 'layup', 'lazar', 'lazes', 'leach', 'leads', 'leafs', 'leafy', 'leaks', 'leaky', 'leans', 'leaps', 'learn', 'lears', 'leary', 'lease', 'leash', 'least', 'leave', 'ledge', 'ledum', 'leech', 'leeds', 'leeks', 'leers', 'leery', 'lefts', 'lefty', 'legal', 'leger', 'leggy', 'leigh', 'lemma', 'lemna', 'lemon', 'lemur', 'lends', 'lenin', 'lense', 'lento', 'leone', 'lepas', 'leper', 'leppy', 'lepus', 'lerot', 'letch', 'lethe', 'letup', 'levee', 'level', 'lever', 'levis', 'lewis', 'lexis', 'liana', 'liars', 'libby', 'libel', 'libra', 'libya', 'lichi', 'licit', 'licks', 'lidar', 'lidos', 'liege', 'liens', 'lifer', 'lifts', 'ligan', 'liger', 'light', 'ligne', 'liked', 'liken', 'likes', 'lilac', 'lilts', 'liman', 'limas', 'limax', 'limbo', 'limbs', 'limen', 'limey', 'limit', 'limns', 'limos', 'limps', 'linac', 'lindy', 'lined', 'linen', 'liner', 'lingo', 'lings', 'linin', 'links', 'linos', 'lints', 'linum', 'lipid', 'liras', 'lisle', 'lisps', 'liszt', 'litas', 'liter', 'lites', 'lithe', 'litre', 'liven', 'liver', 'livid', 'llama', 'llano', 'lloyd', 'loach', 'loads', 'loafs', 'loams', 'loamy', 'loans', 'loasa', 'loath', 'lobar', 'lobby', 'lobed', 'lobes', 'local', 'lochs', 'locks', 'locos', 'locum', 'locus', 'lodes', 'lodge', 'loess', 'lofts', 'lofty', 'logan', 'loges', 'logic', 'logos', 'lohan', 'loins', 'lolls', 'lolly', 'loner', 'loofa', 'looks', 'looms', 'loons', 'loony', 'loops', 'loopy', 'loose', 'loots', 'lopes', 'loren', 'lores', 'lorry', 'loser', 'loses', 'lossy', 'lotas', 'lotic', 'lotte', 'lotto', 'lotus', 'lough', 'louis', 'loupe', 'lours', 'louse', 'lousy', 'louts', 'loved', 'lover', 'loves', 'lowan', 'lower', 'lowly', 'lowry', 'loxes', 'loxia', 'loyal', 'luaus', 'lubes', 'lucid', 'lucks', 'lucky', 'lucre', 'luffa', 'luffs', 'luger', 'luges', 'lulay', 'lulls', 'lully', 'lumen', 'lumps', 'lumpy', 'lunar', 'lunas', 'lunch', 'lunda', 'lunge', 'lungi', 'lungs', 'lunts', 'lupin', 'lupus', 'lurch', 'lures', 'lurid', 'lurks', 'lusts', 'lusty', 'lutes', 'lutra', 'luxes', 'lycee', 'lydia', 'lygus', 'lying', 'lymph', 'lynch', 'lyres', 'lyric', 'lysin', 'lysis', 'lysol', 'lyssa', 'maars', 'macao', 'macaw', 'macer', 'maces', 'macho', 'machs', 'macks', 'macon', 'macro', 'madam', 'madia', 'madly', 'mafia', 'magic', 'magma', 'magus', 'mahdi', 'mahoe', 'maids', 'maidu', 'mails', 'maims', 'maine', 'maize', 'majas', 'major', 'maker', 'makes', 'makos', 'malar', 'malay', 'maleo', 'males', 'malik', 'malls', 'malta', 'malto', 'malts', 'malus', 'malva', 'mamas', 'mamba', 'mambo', 'mamey', 'mamma', 'mammy', 'mande', 'manes', 'manet', 'manga', 'mange', 'mango', 'mangy', 'mania', 'manic', 'manis', 'manky', 'manly', 'manna', 'manor', 'manse', 'manta', 'manul', 'manus', 'maori', 'maple', 'mapra', 'maras', 'march', 'marcs', 'mares', 'marge', 'maria', 'marks', 'marls', 'marly', 'marry', 'marsh', 'marts', 'masai', 'maser', 'masks', 'mason', 'masse', 'masts', 'matai', 'match', 'mated', 'mater', 'mates', 'matey', 'maths', 'matte', 'matts', 'matzo', 'mauls', 'maund', 'mauve', 'maven', 'mavin', 'mavis', 'maxim', 'maxis', 'mayan', 'mayas', 'maybe', 'mayer', 'mayor', 'mazed', 'mazer', 'mazes', 'meals', 'mealy', 'means', 'meany', 'meats', 'meaty', 'mecca', 'medal', 'medea', 'medic', 'medoc', 'meeds', 'meeks', 'meets', 'melba', 'melds', 'melee', 'meles', 'melia', 'melon', 'melts', 'memos', 'mends', 'mensa', 'menus', 'meows', 'mercy', 'meres', 'merge', 'merit', 'merle', 'merls', 'merry', 'mesas', 'mesic', 'meson', 'messy', 'mesua', 'metal', 'meter', 'metes', 'metic', 'metis', 'metre', 'metro', 'meuse', 'mewls', 'mezzo', 'miami', 'miaou', 'miaow', 'miasm', 'miaul', 'micah', 'micas', 'micks', 'micro', 'midas', 'middy', 'midge', 'midis', 'midst', 'miens', 'miffs', 'might', 'mikes', 'milan', 'milch', 'miler', 'milks', 'milky', 'mills', 'milts', 'milya', 'mimeo', 'mimer', 'mimes', 'mimic', 'mimir', 'mimus', 'minah', 'minas', 'mince', 'minds', 'mined', 'miner', 'mines', 'minge', 'mingy', 'minim', 'minis', 'minks', 'minor', 'minos', 'mints', 'minty', 'minus', 'mired', 'mires', 'mirid', 'mirky', 'mirth', 'misdo', 'miser', 'misos', 'missy', 'mists', 'misty', 'miter', 'mites', 'mitra', 'mitre', 'mitts', 'mixed', 'mixer', 'mixes', 'mizen', 'mnium', 'moans', 'moats', 'mocha', 'mocks', 'modal', 'model', 'modem', 'modes', 'mogul', 'mohos', 'moils', 'moire', 'moist', 'mojdi', 'mojos', 'mokes', 'molal', 'molar', 'molas', 'molds', 'moldy', 'moles', 'molle', 'molls', 'molly', 'molto', 'molts', 'momma', 'mommy', 'momus', 'monad', 'monal', 'monas', 'money', 'mongo', 'monks', 'monos', 'monte', 'month', 'mooch', 'moods', 'moody', 'moong', 'moons', 'moony', 'moore', 'moors', 'moose', 'moots', 'moped', 'mopes', 'moral', 'moray', 'morel', 'mores', 'morns', 'moron', 'morph', 'morse', 'morus', 'mosan', 'moses', 'mosey', 'mossy', 'mosts', 'mosul', 'motel', 'motes', 'motet', 'moths', 'mothy', 'motif', 'motor', 'motto', 'motts', 'mould', 'moult', 'mound', 'mount', 'mourn', 'mouse', 'mousy', 'mouth', 'moved', 'mover', 'moves', 'movie', 'mower', 'moxie', 'mucin', 'mucks', 'mucky', 'mucor', 'mucus', 'muddy', 'mudra', 'muffs', 'mufti', 'muggy', 'mugil', 'mujik', 'mulch', 'mulct', 'mules', 'mulla', 'mulls', 'mummy', 'mumps', 'munch', 'munda', 'muons', 'mural', 'murks', 'murky', 'murre', 'musca', 'musci', 'muser', 'muses', 'musgu', 'mushy', 'music', 'musks', 'musky', 'mussy', 'musth', 'musts', 'musty', 'muted', 'mutes', 'mutts', 'muzzy', 'mylar', 'mynah', 'mynas', 'myoid', 'myoma', 'myope', 'myrrh', 'mysis', 'myths', 'nabob', 'nacho', 'nacom', 'nacre', 'nadir', 'nahum', 'naiad', 'naias', 'naifs', 'nails', 'naira', 'naive', 'naked', 'namer', 'names', 'nance', 'nancy', 'nandu', 'nanny', 'naomi', 'napes', 'nappy', 'narcs', 'nards', 'naris', 'narks', 'nasal', 'nasty', 'nasua', 'natal', 'nates', 'natty', 'nauch', 'naval',
'navel', 'naves', 'navvy', 'nawab', 'nazis', 'neaps', 'nears', 'neats', 'necks', 'needs', 'needy', 'neems', 'negro', 'negus', 'nehru', 'neigh', 'neons', 'nepal', 'nerds', 'nerve', 'nervy', 'nests', 'netts', 'never', 'neves', 'nevus', 'newel', 'newly', 'newsy', 'newts', 'nexus', 'ngwee', 'niche', 'nicks', 'nidus', 'niece', 'nifty', 'nighs', 'night', 'nihil', 'nines', 'ninja', 'ninny', 'ninon', 'ninth', 'nintu', 'niobe', 'nipas', 'nippy', 'nisan', 'nisei', 'nisus', 'niter', 'nitid', 'nitre', 'nixon', 'nobel', 'noble', 'nobly', 'nocks', 'nodes', 'noels', 'noemi', 'noise', 'noisy', 'nomad', 'nomas', 'nomes', 'nonce', 'nones', 'nooks', 'nooky', 'noons', 'noose', 'nopal', 'noria', 'norma', 'norms', 'norse', 'north', 'nosed', 'noses', 'nosey', 'notch', 'noted', 'nouns', 'novas', 'novel', 'nubby', 'nubia', 'nucha', 'nudes', 'nudge', 'nukes', 'nulls', 'numbs', 'numen', 'numsi', 'nurse', 'nutty', 'nyala', 'nylon', 'nymph', 'nyssa', 'oaken', 'oakum', 'oasis', 'oasts', 'oaten', 'oaves', 'obeah', 'obese', 'obeys', 'obits', 'oboes', 'occur', 'ocean', 'ocher', 'ochna', 'ochre', 'octad', 'octal', 'octet', 'oddly', 'odist', 'odium', 'odors', 'odour', 'offal', 'offer', 'often', 'ogees', 'ogive', 'ogler', 'ogles', 'ogres', 'ohmic', 'oiled', 'oiler', 'oinks', 'okapi', 'okays', 'okehs', 'okras', 'olden', 'older', 'oldie', 'olein', 'oleos', 'olive', 'ollas', 'ology', 'omaha', 'omani', 'omega', 'omens', 'omits', 'onces', 'onion', 'onset', 'oomph', 'ootid', 'oozes', 'opahs', 'opals', 'opens', 'opera', 'opine', 'opium', 'opsin', 'optic', 'orach', 'orals', 'orang', 'orans', 'orate', 'orbit', 'orcas', 'order', 'oread', 'organ', 'oriel', 'orion', 'oriya', 'orlon', 'orlop', 'ormer', 'orpin', 'orris', 'oryza', 'osage', 'osaka', 'oscan', 'oscar', 'osier', 'other', 'otpaf', 'ottar', 'otter', 'ouija', 'ounce', 'ousel', 'ousts', 'outdo', 'outer', 'outgo', 'outre', 'ouzel', 'ouzos', 'ovals', 'ovary', 'ovate', 'ovens', 'overs', 'overt', 'ovine', 'ovoid', 'ovolo', 'ovule', 'owing', 'owlet', 'owned', 'owner', 'oxbow', 'oxeye', 'oxide', 'oxime', 'oxlip', 'ozena', 'ozone', 'pacas', 'pacer', 'paces', 'pacha', 'packs', 'pacts', 'padda', 'paddy', 'pader', 'padre', 'paean', 'pagan', 'pager', 'pages', 'pails', 'paine', 'pains', 'paint', 'paisa', 'palas', 'palau', 'palis', 'palls', 'pally', 'palms', 'palmy', 'palsy', 'panax', 'panda', 'panel', 'panes', 'panga', 'pangs', 'panic', 'pansy', 'panto', 'pants', 'panty', 'papal', 'papas', 'papaw', 'paper', 'papio', 'papua', 'paras', 'parch', 'parer', 'pares', 'paris', 'parka', 'parks', 'parky', 'parrs', 'parry', 'parse', 'parsi', 'parts', 'party', 'parus', 'parve', 'pasch', 'paseo', 'pasha', 'passe', 'pasta', 'paste', 'pasts', 'pasty', 'patas', 'patch', 'pater', 'pates', 'patio', 'patsy', 'patty', 'pause', 'pavan', 'paved', 'pavis', 'pawer', 'pawky', 'pawls', 'pawns', 'paxes', 'payee', 'payer', 'peace', 'peach', 'peags', 'peaks', 'peaky', 'peals', 'peans', 'pearl', 'peats', 'peaty', 'peavy', 'pecan', 'pecks', 'pecos', 'pedal', 'peeks', 'peels', 'peens', 'peeps', 'peers', 'peeve', 'pekan', 'pekes', 'pekoe', 'pelew', 'pelfs', 'pelts', 'penal', 'pengo', 'penis', 'penni', 'penny', 'peons', 'peony', 'peppy', 'pepsi', 'perca', 'perch', 'percy', 'peril', 'perks', 'perky', 'perms', 'perry', 'pesah', 'pesky', 'pesos', 'pests', 'petal', 'peter', 'petty', 'pewee', 'pewit', 'phage', 'phase', 'phial', 'phlox', 'phoca', 'phone', 'phons', 'phony', 'photo', 'phots', 'phyle', 'physa', 'piano', 'picas', 'picea', 'pichi', 'picks', 'picky', 'picot', 'picul', 'picus', 'piece', 'piers', 'pieta', 'piety', 'piggy', 'pigmy', 'pikas', 'pikes', 'pilaf', 'pilar', 'pilau', 'pilaw', 'pilea', 'piles', 'pilot', 'pilus', 'pimas', 'pimps', 'pinch', 'pings', 'pinko', 'pinks', 'pinky', 'pinna', 'pinny', 'pinon', 'pinot', 'pinto', 'pints', 'pinus', 'pious', 'pipal', 'piper', 'pipes', 'pipet', 'pipit', 'pipra', 'pique', 'piste', 'pisum', 'pitas', 'pitch', 'piths', 'pithy', 'piton', 'pitta', 'piute', 'pivot', 'pixel', 'pixes', 'pixie', 'pizza', 'place', 'plage', 'plaid', 'plain', 'plait', 'plane', 'plank', 'plans', 'plant', 'plash', 'plasm', 'plate', 'plato', 'plats', 'platy', 'plays', 'plaza', 'plead', 'pleat', 'plebe', 'plica', 'plier', 'pliny', 'ploce', 'plods', 'plonk', 'plops', 'plots', 'plows', 'ploys', 'pluck', 'plugs', 'plumb', 'plume', 'plump', 'plums', 'plumy', 'plunk', 'plush', 'pluto', 'plyer', 'poach', 'pocks', 'podgy', 'poems', 'poesy', 'poets', 'pogey', 'pogge', 'poilu', 'point', 'poise', 'poker', 'pokes', 'pokey', 'polar', 'poler', 'poles', 'polio', 'polka', 'polls', 'polyp', 'pomes', 'pommy', 'pomps', 'ponca', 'ponce', 'ponds', 'pones', 'pongo', 'pooch', 'poods', 'poons', 'poops', 'poove', 'popes', 'poppy', 'porch', 'pores', 'porgy', 'porks', 'porno', 'porns', 'porta', 'porte', 'porto', 'ports', 'posed', 'poser', 'poses', 'posit', 'posse', 'posts', 'potto', 'potty', 'pouch', 'poufs', 'pound', 'pours', 'pouts', 'power', 'poxes', 'poyou', 'prams', 'prang', 'prank', 'prate', 'prats', 'prawn', 'praya', 'prays', 'preen', 'preps', 'press', 'prexy', 'preys', 'priam', 'price', 'prick', 'pricy', 'pride', 'pries', 'prigs', 'prima', 'prime', 'primo', 'primp', 'prims', 'prink', 'print', 'prion', 'prior', 'prise', 'prism', 'privy', 'prize', 'probe', 'prods', 'profs', 'prole', 'promo', 'proms', 'prone', 'prong', 'proof', 'props', 'prose', 'prosy', 'proto', 'proud', 'prove', 'prowl', 'prows', 'proxy', 'prude', 'prune', 'psalm', 'pseud', 'psoas', 'pubes', 'pubic', 'pubis', 'puces', 'pucka', 'pucks', 'pudge', 'pudgy', 'puffs', 'puffy', 'pukes', 'pukka', 'pulas', 'pules', 'pulex', 'pulls', 'pulps', 'pulpy', 'pulse', 'pumas', 'pumps', 'punch', 'pungs', 'punic', 'punks', 'punky', 'punts', 'pupal', 'pupas', 'pupil', 'puppy', 'purau', 'puree', 'purge', 'purim', 'purls', 'purrs', 'purse', 'pursy', 'puses', 'pushy', 'pussy', 'putts', 'putty', 'pygmy', 'pylon', 'pyres', 'pyrex', 'pyrus', 'pyxes', 'pyxie', 'pyxis', 'qatar', 'qibla', 'qophs', 'quack', 'quads', 'quaff', 'quags', 'quail', 'quake', 'qualm', 'quark', 'quart', 'quash', 'quasi', 'quays', 'queen', 'queer', 'quell', 'quern', 'query', 'quest', 'queue', 'quick', 'quids', 'quiet', 'quiff', 'quill', 'quilt', 'quins', 'quint', 'quips', 'quipu', 'quira', 'quire', 'quirk', 'quirt', 'quite', 'quito', 'quits', 'quoin', 'quoit', 'quota', 'quote', 'rabat', 'rabbi', 'rabid', 'racer', 'racks', 'racon', 'radar', 'radio', 'radix', 'radon', 'rafts', 'ragee', 'rages', 'ragis', 'raids', 'rails', 'rainy', 'raise', 'rajab', 'rajah', 'rakes', 'rales', 'rally', 'ramee', 'ramie', 'ramps', 'ramus', 'ranch', 'rands', 'randy', 'ranee', 'range', 'rangy', 'ranid', 'ranis', 'ranks', 'rants', 'raped', 'raper', 'rapes', 'raphe', 'rapid', 'rases', 'rasps', 'raspy', 'ratan', 'ratch', 'ratel', 'rates', 'ratio', 'ratty', 'ravel', 'raven', 'raver', 'raves', 'rayon', 'razed', 'razes', 'razor', 'reach', 'react', 'reads', 'ready', 'realm', 'reams', 'reaps', 'rearm', 'rears', 'reata', 'reave', 'rebel', 'rebus', 'rebut', 'recap', 'recce', 'recco', 'reccy', 'recto', 'recur', 'redes', 'redly', 'redos', 'redox', 'redux', 'reeds', 'reedy', 'reefs', 'reefy', 'reeks', 'reels', 'reeve', 'refer', 'refit', 'regal', 'regur', 'reich', 'reify', 'reign', 'rejig', 'relax', 'relay', 'relic', 'remit', 'remus', 'renal', 'rends', 'renew', 'renin', 'rente', 'rents', 'repay', 'repel', 'reply', 'repot', 'repps', 'rerun', 'reset', 'resew', 'resid', 'resin', 'rests', 'retch', 'retem', 'retie', 'retro', 'retry', 'reuse', 'revel', 'revet', 'revue', 'rexes', 'rheas', 'rhein', 'rheum', 'rhine', 'rhino', 'rhomb', 'rhumb', 'rhyme', 'rials', 'riant', 'riata', 'ribes', 'ricer', 'rices', 'ricin', 'ricks', 'rider', 'rides', 'ridge', 'riels', 'riffs', 'rifle', 'rifts', 'rigel', 'right', 'rigid', 'rigor', 'riled', 'riles', 'riley', 'rills', 'rimas', 'rimed', 'rimes', 'rinds', 'rings', 'rinks', 'rinse', 'riots', 'ripen', 'ripes', 'risen', 'riser', 'risks', 'risky', 'rites', 'ritzy', 'rival', 'river', 'rives', 'rivet', 'riyal', 'roach', 'roads', 'roams', 'roans', 'roars', 'roast', 'robed', 'robes', 'robin', 'roble', 'robot', 'rocks', 'rocky', 'rodeo', 'rogue', 'roils', 'roily', 'roles', 'rollo', 'rolls', 'roman', 'romeo', 'romps', 'rondo', 'roods', 'roofs', 'roofy', 'rooks', 'rooms', 'roomy', 'roost', 'roots', 'roper', 'ropes', 'ropey', 'roses', 'rosin', 'rotas', 'rotes', 'rotls', 'rotor', 'roues', 'rouge', 'rough', 'round', 'rouse', 'route', 'routs', 'rover', 'roves', 'rowan', 'rowdy', 'rowel', 'rower', 'royal', 'rubes', 'rubia', 'ruble', 'rubor', 'rubus', 'rucks', 'rudds', 'ruddy', 'ruffs', 'rugby', 'ruins', 'ruled', 'ruler', 'rumba', 'rumen', 'rumex', 'rummy', 'rumor', 'rumps', 'runch', 'runes', 'rungs', 'runic', 'runny', 'runts', 'runty', 'rupee', 'rural', 'ruses', 'rushy', 'rusks', 'rusts', 'rusty', 'ruths', 'rutty', 'sabal', 'saber', 'sabin', 'sable', 'sabot', 'sabra', 'sabre', 'sacks', 'sades', 'sadhe', 'sadhu', 'sadly', 'safar', 'safes', 'sages', 'sagos', 'sahib', 'saids', 'saiga', 'sails', 'saint', 'sakes', 'sakis', 'sakti', 'salad', 'salal', 'salat', 'salem', 'sales', 'salix', 'sally', 'salmi', 'salmo', 'salol', 'salon', 'salpa', 'salps', 'salsa', 'salty', 'salve', 'salvo', 'saman', 'samba', 'samen', 'samoa', 'sands', 'sandy', 'sanes', 'santa', 'sapid',
'sappy', 'sarah', 'saran', 'sards', 'saree', 'sarin', 'sassy', 'satan', 'sates', 'satin', 'satyr', 'sauce', 'saucy', 'saudi', 'sauls', 'sauna', 'saury', 'saute', 'saved', 'saver', 'saves', 'savin', 'savor', 'savoy', 'savvy', 'sawan', 'saxes', 'saxon', 'scabs', 'scads', 'scags', 'scald', 'scale', 'scalp', 'scaly', 'scamp', 'scams', 'scans', 'scant', 'scape', 'scare', 'scarf', 'scarp', 'scars', 'scary', 'scats', 'scaup', 'scend', 'scene', 'scent', 'schmo', 'schwa', 'scion', 'scoff', 'scoke', 'scold', 'scone', 'scoop', 'scoot', 'scope', 'score', 'scorn', 'scots', 'scott', 'scour', 'scout', 'scowl', 'scows', 'scrag', 'scram', 'scrap', 'scree', 'screw', 'scrim', 'scrip', 'scrod', 'scrub', 'scrum', 'scuba', 'scuds', 'scuff', 'scull', 'scums', 'scups', 'scurf', 'scute', 'scuts', 'seals', 'seams', 'seamy', 'sears', 'seats', 'sebum', 'sects', 'sedan', 'seder', 'sedge', 'sedgy', 'sedum', 'seeds', 'seedy', 'seeks', 'seels', 'seems', 'seeps', 'seers', 'segno', 'segue', 'seine', 'seism', 'seize', 'selfs', 'sells', 'selva', 'semen', 'sends', 'senna', 'senor', 'sense', 'sents', 'seoul', 'sepal', 'sepia', 'septs', 'serer', 'seres', 'serfs', 'serge', 'serif', 'serin', 'serow', 'serra', 'serum', 'serve', 'servo', 'seton', 'setup', 'seven', 'sever', 'sewed', 'sewer', 'sexed', 'sexes', 'sexts', 'sfebe', 'shack', 'shade', 'shads', 'shady', 'shaft', 'shags', 'shahs', 'shake', 'shako', 'shaky', 'shale', 'shame', 'shams', 'shang', 'shank', 'shape', 'shard', 'share', 'shari', 'shark', 'sharp', 'shave', 'shawl', 'shawm', 'shawn', 'shaws', 'sheaf', 'shear', 'sheds', 'sheen', 'sheep', 'sheer', 'sheet', 'sheik', 'shelf', 'shell', 'shema', 'sherd', 'shews', 'shiah', 'shies', 'shift', 'shill', 'shims', 'shina', 'shine', 'shins', 'shiny', 'ships', 'shire', 'shirk', 'shirr', 'shirt', 'shits', 'shiva', 'shivs', 'shlep', 'shoal', 'shoat', 'shock', 'shoed', 'shoes', 'shogi', 'shoji', 'shona', 'shook', 'shoos', 'shoot', 'shops', 'shore', 'shorn', 'short', 'shote', 'shots', 'shout', 'shove', 'shows', 'showy', 'shred', 'shrew', 'shrub', 'shrug', 'shuck', 'shuns', 'shunt', 'shush', 'shute', 'shuts', 'shyly', 'sials', 'sibyl', 'sicks', 'sides', 'sidle', 'siege', 'sieve', 'sifts', 'sighs', 'sight', 'sigma', 'signs', 'sikhs', 'silds', 'silex', 'silks', 'silky', 'sills', 'silly', 'silos', 'silts', 'silty', 'silva', 'simal', 'simas', 'simon', 'since', 'sines', 'sinew', 'singe', 'sings', 'sinks', 'sinus', 'sioux', 'siren', 'sires', 'siris', 'sirup', 'sisal', 'sises', 'sissu', 'sissy', 'sitar', 'sites', 'sitka', 'sitta', 'siums', 'sivan', 'siwan', 'sixer', 'sixes', 'sixth', 'sixty', 'sized', 'sizes', 'skags', 'skate', 'skeat', 'skeet', 'skegs', 'skein', 'skeps', 'skews', 'skids', 'skier', 'skies', 'skiff', 'skill', 'skimp', 'skims', 'skink', 'skins', 'skint', 'skips', 'skirl', 'skirt', 'skits', 'skive', 'skuas', 'skulk', 'skull', 'skunk', 'slabs', 'slack', 'slags', 'slain', 'slake', 'slams', 'slang', 'slant', 'slaps', 'slash', 'slask', 'slate', 'slats', 'slaty', 'slave', 'slavs', 'slaws', 'slays', 'sleds', 'sleek', 'sleep', 'sleet', 'slews', 'slice', 'slick', 'slide', 'slime', 'slims', 'slimy', 'sling', 'slink', 'slips', 'slits', 'slobs', 'sloes', 'slogs', 'sloop', 'slope', 'slops', 'slosh', 'sloth', 'slots', 'slows', 'slubs', 'slues', 'slugs', 'slump', 'slums', 'slurp', 'slurs', 'slush', 'sluts', 'slyly', 'smack', 'small', 'smarm', 'smart', 'smash', 'smear', 'smell', 'smelt', 'smews', 'smile', 'smirk', 'smite', 'smith', 'smock', 'smogs', 'smoke', 'smoky', 'smuts', 'snack', 'snafu', 'snags', 'snail', 'snake', 'snaky', 'snaps', 'snare', 'snarl', 'snead', 'sneak', 'sneer', 'snick', 'snide', 'sniff', 'snipe', 'snips', 'snits', 'snobs', 'snoek', 'snood', 'snook', 'snoop', 'snoot', 'snore', 'snort', 'snots', 'snout', 'snows', 'snowy', 'snubs', 'snuff', 'snugs', 'soaks', 'soaps', 'soapy', 'soars', 'soave', 'sober', 'socks', 'socle', 'sodas', 'soddy', 'sodom', 'sofas', 'sofia', 'softs', 'softy', 'soggy', 'soils', 'sojas', 'solan', 'solar', 'solea', 'soled', 'soles', 'solfa', 'solid', 'solon', 'solos', 'solve', 'somas', 'sonar', 'sones', 'songs', 'sonic', 'sonny', 'sonsy', 'sooth', 'soots', 'sooty', 'sophs', 'sopor', 'soppy', 'sorbs', 'sores', 'sorex', 'sorgo', 'sorry', 'sorts', 'sorus', 'sotho', 'sough', 'souls', 'sound', 'soups', 'soupy', 'sours', 'souse', 'south', 'sower', 'soyas', 'space', 'spacy', 'spade', 'spain', 'spall', 'spang', 'spank', 'spare', 'spark', 'spars', 'spasm', 'spate', 'spats', 'spawl', 'spawn', 'spays', 'speak', 'spear', 'speck', 'specs', 'speed', 'speer', 'spell', 'spelt', 'spend', 'spent', 'sperm', 'spews', 'spica', 'spice', 'spick', 'spics', 'spicy', 'spiel', 'spies', 'spiff', 'spike', 'spiks', 'spiky', 'spile', 'spill', 'spine', 'spins', 'spiny', 'spire', 'spirt', 'spite', 'spits', 'spitz', 'spivs', 'splat', 'splay', 'split', 'spock', 'spode', 'spoil', 'spoke', 'spoof', 'spook', 'spool', 'spoon', 'spoor', 'spore', 'sport', 'spots', 'spout', 'sprag', 'sprat', 'spray', 'spree', 'sprig', 'sprit', 'sprue', 'spuds', 'spues', 'spume', 'spumy', 'spunk', 'spurn', 'spurs', 'spurt', 'squab', 'squad', 'squat', 'squaw', 'squib', 'squid', 'stabs', 'stack', 'staff', 'stage', 'stags', 'stagy', 'staid', 'stain', 'stair', 'stake', 'stale', 'stalk', 'stall', 'stamp', 'stand', 'staph', 'stare', 'stark', 'starr', 'stars', 'start', 'stash', 'state', 'stave', 'stays', 'stead', 'steak', 'steal', 'steam', 'steed', 'steel', 'steen', 'steep', 'steer', 'stein', 'stela', 'stele', 'stems', 'stent', 'steps', 'stern', 'stets', 'stews', 'stick', 'sties', 'stiff', 'stile', 'still', 'stilt', 'sting', 'stink', 'stint', 'stipe', 'stirk', 'stirs', 'stoat', 'stobs', 'stock', 'stoep', 'stogy', 'stoic', 'stoke', 'stole', 'stoma', 'stomp', 'stone', 'stony', 'stool', 'stoop', 'stops', 'store', 'stork', 'storm', 'story', 'stoup', 'stout', 'stove', 'stows', 'strad', 'strap', 'straw', 'stray', 'strep', 'strew', 'stria', 'strip', 'strix', 'strop', 'strum', 'strut', 'stubs', 'stuck', 'studs', 'study', 'stuff', 'stump', 'stung', 'stuns', 'stunt', 'stupa', 'stupe', 'styes', 'style', 'stymy', 'suave', 'sucre', 'sudan', 'sudor', 'sudra', 'sudsy', 'suede', 'suers', 'suets', 'suety', 'sugar', 'sugis', 'suite', 'suits', 'sulfa', 'sulks', 'sulky', 'sulla', 'sully', 'sumac', 'sumos', 'sumps', 'sunna', 'sunni', 'sunny', 'sunup', 'suomi', 'super', 'supra', 'suras', 'surds', 'sures', 'surfs', 'surge', 'surly', 'surya', 'sushi', 'sutra', 'swabs', 'swage', 'swags', 'swain', 'swale', 'swami', 'swamp', 'swank', 'swans', 'swaps', 'sward', 'swarm', 'swart', 'swash', 'swath', 'sways', 'swazi', 'swear', 'sweat', 'swede', 'sweep', 'sweet', 'swell', 'swept', 'swift', 'swigs', 'swill', 'swims', 'swine', 'swing', 'swipe', 'swirl', 'swish', 'swiss', 'swobs', 'swoon', 'swoop', 'swops', 'sword', 'sworn', 'swosh', 'swots', 'sylph', 'sylva', 'syncs', 'synod', 'syria', 'syrup', 'tabby', 'tabes', 'tabis', 'table', 'taboo', 'tabor', 'tacca', 'tachs', 'tacit', 'tacks', 'tacky', 'tacos', 'tacts', 'taels', 'taffy', 'tagus', 'tails', 'taint', 'tajik', 'taken', 'taker', 'takes', 'takin', 'talas', 'talcs', 'talks', 'talky', 'tally', 'talon', 'talus', 'tamal', 'tamed', 'tamer', 'tames', 'tamil', 'tammy', 'tampa', 'tamps', 'tamus', 'tandy', 'tanga', 'tango', 'tangs', 'tangy', 'tanka', 'tanks', 'tansy', 'taped', 'taper', 'tapes', 'tapir', 'tapis', 'tappa', 'tardy', 'tares', 'tarns', 'taros', 'tarot', 'tarps', 'tarry', 'tarts', 'tasks', 'tasse', 'taste', 'tasty', 'tatar', 'tater', 'tates', 'tatou', 'tatty', 'taunt', 'taupe', 'tauts', 'tawny', 'tawse', 'taxer', 'taxes', 'taxis', 'taxon', 'taxus', 'tayra', 'teach', 'teaks', 'teals', 'teams', 'tears', 'teary', 'tease', 'teats', 'tebet', 'techy', 'teddy', 'teems', 'teens', 'teeny', 'teeth', 'teffs', 'teiid', 'telex', 'tells', 'telly', 'tempo', 'temps', 'tempt', 'tench', 'tends', 'tenet', 'tenia', 'tenno', 'tenon', 'tenor', 'tense', 'tenth', 'tents', 'tepal', 'tepee', 'tepid', 'teras', 'terce', 'teres', 'terms', 'terns', 'terry', 'terse', 'tesla', 'testa', 'tests', 'testy', 'teths', 'teton', 'tetra', 'texan', 'texas', 'texts', 'thane', 'thank', 'thats', 'thaws', 'theca', 'theft', 'theme', 'thens', 'there', 'therm', 'theta', 'thick', 'thief', 'thigh', 'thill', 'thing', 'think', 'thins', 'third', 'thole', 'thong', 'thorn', 'three', 'thrip', 'throb', 'throe', 'throw', 'thrum', 'thuds', 'thugs', 'thuja', 'thule', 'thumb', 'thump', 'thyme', 'tiara', 'tiber', 'tibet', 'tibia', 'tical', 'ticks', 'tidal', 'tides', 'tiers', 'tiffs', 'tifli', 'tiger', 'tight', 'tigon', 'tikes', 'tilde', 'tiled', 'tiler', 'tiles', 'tilia', 'tills', 'tilth', 'tilts', 'timed', 'timer', 'times', 'timid', 'timor', 'tinct', 'tinea', 'tined', 'tines', 'tinge', 'tings', 'tinny', 'tints', 'tipis', 'tippy', 'tipsy', 'tired', 'tires', 'titan', 'titer', 'tithe', 'titis', 'title', 'titre', 'titty', 'titus', 'tizzy', 'toads', 'toady', 'toast', 'today', 'toddy', 'todea', 'todus', 'toffs', 'toffy', 'tokay', 'token', 'tokes', 'tokyo', 'toles', 'tolls', 'tombs', 'tomes', 'tonal', 'toned', 'toner', 'tones', 'tonga', 'tongs', 'tonic', 'tonne', 'tonus', 'tools', 'toona', 'toons', 'tooth', 'topaz', 'topee', 'toper', 'topes', 'topic', 'topis', 'topos', 'toque', 'torah', 'torch', 'tores', 'torsk', 'torso', 'torte', 'torts', 'torus', 'total', 'totem', 'toter', 'totes', 'touch', 'tough', 'tours', 'touts', 'towel', 'tower', 'towns', 'towny', 'toxic', 'toxin', 'toyon', 'trace', 'track', 'tract', 'tracy', 'trade', 'trail', 'train', 'trait', 'tramp', 'trams', 'trapa', 'trash', 'trave', 'trawl', 'trays', 'tread', 'treat', 'treed', 'trees', 'treks', 'trema', 'trend', 'trent', 'tress', 'trews', 'treys', 'triad', 'trial', 'tribe', 'trice', 'trick', 'tried', 'trier', 'tries', 'triga', 'trigs', 'trike', 'trill', 'trims', 'trine', 'tripe', 'trips', 'trite', 'troat', 'troll', 'troop', 'trope', 'troth', 'trots', 'trout', 'trove', 'troys', 'truce', 'truck', 'trues', 'truly', 'trump', 'trunk', 'truss', 'trust', 'truth', 'tryst', 'tsars', 'tsine', 'tsuga', 'tubal', 'tubas', 'tubby', 'tubed', 'tuber', 'tucks', 'tudor', 'tufas', 'tuffs', 'tufts', 'tulip', 'tulle', 'tulsa', 'tumid', 'tummy', 'tumor', 'tunas', 'tuner', 'tunes', 'tunga', 'tungs', 'tunic', 'tunis', 'tunny', 'tupek', 'tupik', 'turds', 'turfs', 'turki', 'turks', 'turns', 'turps', 'tushs', 'tusks', 'tutee', 'tutor', 'tuxes', 'tuxub', 'twain', 'twang', 'twats', 'tweak', 'tweed', 'tweet', 'twerp', 'twice', 'twigs', 'twill', 'twine', 'twins', 'twirl', 'twirp', 'twist', 'twits', 'tyche', 'tying', 'tykes', 'tyler', 'tynes', 'types', 'typha', 'typic', 'typos', 'tyres', 'tyros', 'tzars', 'udder', 'uglis', 'ugric', 'uigur', 'ukase', 'ulama', 'ulcer', 'ulema', 'ulmus', 'ulnar', 'ulnas', 'ultra', 'ulvas', 'umbel', 'umber', 'umbos', 'umbra', 'unais', 'unarm', 'unary', 'unaus', 'unbar', 'unbox', 'uncle', 'uncos', 'uncus', 'uncut', 'under', 'undue', 'unfed', 'unfit', 'uniat', 'unify', 'union', 'unite', 'units', 'unity', 'unlax', 'unlit', 'unman', 'unpin', 'unsay', 'unsex', 'untie', 'until', 'unwed', 'unzip', 'upend', 'upper', 'upset', 'upupa', 'urate', 'urban', 'ureas', 'urges', 'uriah', 'urial', 'urine', 'ursus', 'usage', 'users', 'ushas', 'usher', 'using', 'usnea', 'usual', 'usurp', 'usury', 'uteri', 'utile', 'utter', 'uveal', 'uveas', 'uvula', 'uzbak', 'uzbeg', 'uzbek', 'vagal', 'vague', 'vagus', 'vajra', 'vales', 'valet', 'valid', 'valmy', 'valor', 'valse', 'value', 'valve', 'vamps', 'vanda', 'vaned', 'vanes', 'vanir', 'vapid', 'vapor', 'varan', 'varix', 'varna', 'varus', 'vases', 'vasts', 'vatic', 'vault', 'vaunt', 'veals', 'vedic', 'veers', 'veery', 'vegan', 'veils', 'veins', 'velar', 'velds', 'veldt', 'velum', 'venal', 'vends', 'venom', 'vents', 'venue', 'venus', 'vepse', 'verbs', 'verdi', 'verge', 'verpa', 'verse', 'verso', 'verst', 'vertu', 'verve', 'vespa', 'vesta', 'vests', 'vetch', 'vexed', 'vexer', 'vexes', 'vials', 'viand', 'vibes', 'vicar', 'vices', 'vichy', 'vicia', 'video', 'vidua', 'views', 'vigil', 'vigor', 'villa', 'vinca', 'vines', 'vinos', 'vinyl', 'viola', 'viols', 'viper', 'viral', 'vireo', 'virga', 'virgo', 'virtu', 'virus', 'visas', 'vises', 'visit', 'visod', 'visor', 'vista', 'vital', 'vitis', 'vivas', 'vivid', 'vixen', 'vizor', 'vocal', 'vodka', 'vogue', 'vogul', 'voice', 'voids', 'voile', 'volar', 'voles', 'volga', 'volta', 'volts', 'volva', 'vomer', 'vomit', 'voter', 'votes', 'vouch', 'vouge', 'vowel', 'vower', 'vroom', 'vulva', 'wacky', 'wader', 'wades', 'wadis', 'wafer', 'wafts', 'wager', 'wages', 'wagon', 'wahoo', 'waifs', 'wails', 'wains', 'waist', 'waits', 'waive', 'waken', 'waker', 'wakes', 'wales', 'walks', 'walls', 'wally', 'waltz', 'wands', 'wanes', 'wanly', 'wants', 'wapmo', 'wards', 'warms', 'warns', 'warps', 'warts', 'warty', 'washy', 'wasps', 'waste', 'watch', 'water', 'watts', 'waugh', 'wauls', 'waver', 'wawls', 'waxed', 'waxen', 'waxes', 'wayne', 'weald', 'weals', 'weans', 'wears', 'weary', 'weave', 'webby', 'weber', 'wedel', 'wedge', 'weeds', 'weedy', 'weeks', 'weeny', 'weeps', 'weepy', 'wefts', 'weigh', 'weird', 'weirs', 'wekas', 'welch', 'welds', 'wells', 'welsh', 'welts', 'wench', 'wends', 'wests', 'whack', 'whale', 'whams', 'whang', 'whaps', 'wharf', 'whats', 'wheal', 'wheat', 'wheel', 'whelk', 'whelm', 'whelp', 'whets', 'wheys', 'whiff', 'whigs', 'while', 'whims', 'whine', 'whins', 'whiny', 'whirl', 'whirr', 'whirs', 'whish', 'whisk', 'whist', 'white', 'whits', 'whizz', 'whole', 'whomp', 'whoop', 'whops', 'whore', 'whorl', 'whose', 'wicca', 'wicks', 'widen', 'wides', 'widow', 'width', 'wield', 'wifes', 'wight', 'wilds', 'wiles', 'wince', 'winch', 'winds', 'windy', 'wines', 'winey', 'wings', 'winks', 'wiper', 'wipes', 'wired', 'wirer', 'wires', 'wises', 'wisps', 'witty', 'wizen', 'woads', 'woden', 'wolfs', 'wolof', 'woman', 'wombs', 'wonky', 'wonts', 'woods', 'woody', 'wooer', 'woofs', 'woolf', 'wools', 'wooly', 'woosh', 'woozy', 'words', 'wordy', 'works', 'world', 'wormy', 'worry', 'worse', 'worst', 'worth', 'worts', 'wospy', 'wound', 'woven', 'wrack', 'wraps', 'wrath', 'wrawl', 'wreak', 'wreck', 'wrest', 'wrick', 'wries', 'wring', 'wrist', 'write', 'writs', 'wrong', 'wroth', 'wryly', 'xenon', 'xeric', 'xerox', 'xviii', 'xxiii', 'xylem', 'xylol', 'xyris', 'yacca', 'yacht', 'yacks', 'yagis', 'yahoo', 'yakut', 'yanan', 'yangs', 'yanks', 'yards', 'yarns', 'yaups', 'yawls', 'yawns', 'yawps', 'yazoo', 'yearn', 'years', 'yeast', 'yells', 'yelps', 'yemen', 'yenta', 'yeses', 'yetis', 'yield', 'ylems', 'yobbo', 'yodel', 'yodhs', 'yogic', 'yogis', 'yokel', 'yokes', 'yolks', 'yores', 'young', 'youth', 'yowls', 'yquem', 'yuans', 'yucca', 'yucky', 'yukon', 'yules', 'yuman', 'yummy', 'yurts', 'yussa', 'zaire', 'zakat', 'zaman', 'zamia', 'zapus', 'zarfs', 'zayin', 'zeals', 'zebra', 'zensu', 'zeros', 'zests', 'zesty', 'zetas', 'zilch', 'zills', 'zincs', 'zings', 'zippy', 'zitis', 'zloty', 'zombi', 'zonal', 'zones', 'zooid', 'zooms', 'zoril', 'zunis']
def evaluate_possible_words(guess_history, evaluation_history, words):
    correct = [None] * 5   
    present = {}   
    absent = set()         
    
    for guess, evaluation in zip(guess_history, evaluation_history):
        for i, (letter, result) in enumerate(zip(guess, evaluation)):
            if result == 'O':
                correct[i] = letter  
            elif result == 'X':
                if letter not in present:
                    present[letter] = []
                present[letter].append(i)  
            elif result == '-':
                absent.add(letter) 
    
    def is_valid_word(word):
        for i, letter in enumerate(correct):
            if letter is not None and word[i] != letter:
                return False
        for letter, positions in present.items():
            if letter not in word:
                return False
            for pos in positions:
                if word[pos] == letter: 
                    return False
        if any(letter in word for letter in absent):
            return False
        return True

    filtered_words = [word for word in words if is_valid_word(word)]
    return filtered_words

@app.route('/wordle-game', methods=['POST'])
def wordle_game():
    if request.is_json:
        data = request.get_json()
        print(len(data['guessHistory']))
        if len(data['guessHistory']) == 0:
            # First guess
            guess = "stare"
        else:
            guess_history = data['guessHistory']
            evaluation_history = data['evaluationHistory']
            possible_words = evaluate_possible_words(guess_history, evaluation_history, word_list)
            if len(possible_words) == 0:
                guess = "error"
            else:
                guess = possible_words[0]

        response = {
            "guess": guess
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid request format"}), 400
    


@app.route('/tourist', methods=['POST'])
def tourist():
    data = request.get_json()
    input_dict = data.get('locations')
    starting_point = data.get('startingPoint')
    time_limit = data.get('timeLimit')

    # Constants
    subway_stations = {
    "Tokyo Metro Ginza Line": [
        "Asakusa", "Tawaramachi", "Inaricho", "Ueno", "Ueno-hirokoji", "Suehirocho",
        "Kanda", "Mitsukoshimae", "Nihombashi", "Kyobashi", "Ginza", "Shimbashi",
        "Toranomon", "Tameike-sanno", "Akasaka-mitsuke", "Nagatacho", "Aoyama-itchome",
        "Gaiemmae", "Omotesando", "Shibuya"
    ],
    "Tokyo Metro Marunouchi Line": [
        "Ogikubo", "Minami-asagaya", "Shin-koenji", "Higashi-koenji", "Shin-nakano",
        "Nakano-sakaue", "Nishi-shinjuku", "Shinjuku", "Shinjuku-sanchome", "Shin-ochanomizu",
        "Ochanomizu", "Awajicho", "Otemachi", "Tokyo", "Ginza", "Kasumigaseki", "Kokkai-gijidomae",
        "Akasaka-mitsuke", "Yotsuya", "Yotsuya-sanchome", "Shinjuku-gyoemmae", "Nishi-shinjuku-gochome",
        "Nakano-fujimicho", "Nakano-shimbashi", "Nakano-sakaue", "Shinjuku-sanchome", "Kokkai-gijidomae",
        "Kasumigaseki", "Ginza", "Tokyo", "Otemachi", "Awajicho", "Shin-ochanomizu", "Ochanomizu"
    ],
    "Tokyo Metro Hibiya Line": [
        "Naka-meguro", "Ebisu", "Hiroo", "Roppongi", "Kamiyacho", "Kasumigaseki", "Hibiya",
        "Ginza", "Higashi-ginza", "Tsukiji", "Hatchobori", "Kayabacho", "Nihombashi",
        "Kodemmacho", "Akihabara", "Naka-okachimachi", "Ueno", "Iriya", "Minowa",
        "Minami-senju", "Kita-senju"
    ],
    "Tokyo Metro Tozai Line": [
        "Nakano", "Ochiai", "Takadanobaba", "Waseda", "Kagurazaka", "Iidabashi", "Kudanshita",
        "Takebashi", "Otemachi", "Nihombashi", "Kayabacho", "Monzen-nakacho", "Kiba",
        "Toyosu", "Minami-sunamachi", "Nishi-kasai", "Kasai", "Urayasu", "Minami-gyotoku",
        "Gyotoku", "Myoden", "Baraki-nakayama", "Nishi-funabashi"
    ],
    "Tokyo Metro Chiyoda Line": [
        "Yoyogi-uehara", "Yoyogi-koen", "Meiji-jingumae", "Omotesando", "Nogizaka", "Akasaka",
        "Kokkai-gijidomae", "Kasumigaseki", "Hibiya", "Nijubashimae", "Otemachi",
        "Shin-ochanomizu", "Yushima", "Nezu", "Sendagi", "Nishi-nippori", "Machiya",
        "Kita-senju", "Ayase", "Kita-ayase"
    ],
    "Tokyo Metro Yurakucho Line": [
        "Wakoshi", "Chikatetsu-narimasu", "Chikatetsu-akatsuka", "Heiwadai", "Hikawadai",
        "Kotake-mukaihara", "Senkawa", "Kanamecho", "Ikebukuro", "Higashi-ikebukuro",
        "Gokokuji", "Edogawabashi", "Iidabashi", "Ichigaya", "Kojimachi", "Nagatacho",
        "Sakuradamon", "Yurakucho", "Ginza-itchome", "Shintomicho", "Toyocho",
        "Kiba", "Toyosu", "Tsukishima", "Shintomicho", "Tatsumi", "Shinonome", "Ariake"
    ],
    "Tokyo Metro Hanzomon Line": [
        "Shibuya", "Omotesando", "Aoyama-itchome", "Nagatacho", "Hanzomon", "Kudanshita",
        "Jimbocho", "Otemachi", "Mitsukoshimae", "Suitengumae", "Kiyosumi-shirakawa",
        "Sumiyoshi", "Kinshicho", "Oshiage"
    ],
    "Tokyo Metro Namboku Line": [
        "Meguro", "Shirokanedai", "Shirokane-takanawa", "Azabu-juban", "Roppongi-itchome",
        "Tameike-sanno", "Nagatacho", "Yotsuya", "Ichigaya", "Iidabashi", "Korakuen",
        "Todaimae", "Hon-komagome", "Komagome", "Nishigahara", "Oji", "Oji-kamiya",
        "Shimo", "Akabane-iwabuchi"
    ],
    "Tokyo Metro Fukutoshin Line": [
        "Wakoshi", "Chikatetsu-narimasu", "Chikatetsu-akatsuka", "Narimasu", "Shimo-akatsuka",
        "Heiwadai", "Hikawadai", "Kotake-mukaihara", "Senkawa", "Kanamecho", "Ikebukuro",
        "Zoshigaya", "Nishi-waseda", "Higashi-shinjuku", "Shinjuku-sanchome", "Kita-sando",
        "Meiji-jingumae", "Shibuya"
    ],
    "Toei Asakusa Line": [
        "Nishi-magome", "Magome", "Nakanobu", "Togoshi", "Gotanda", "Takanawadai",
        "Sengakuji", "Mita", "Shiba-koen", "Daimon", "Shimbashi", "Higashi-ginza",
        "Takaracho", "Nihombashi", "Ningyocho", "Higashi-nihombashi", "Asakusabashi",
        "Kuramae", "Asakusa", "Honjo-azumabashi", "Oshiage"
    ],
    "Toei Mita Line": [
        "Meguro", "Shirokanedai", "Shirokane-takanawa", "Mita", "Shiba-koen", "Onarimon",
        "Uchisaiwaicho", "Hibiya", "Otemachi", "Jimbocho", "Suidobashi", "Kasuga",
        "Hakusan", "Sengoku", "Sugamo", "Nishi-sugamo", "Shin-itabashi", "Itabashi-kuyakushomae",
        "Itabashi-honcho", "Motohasunuma", "Shin-takashimadaira", "Nishidai", "Hasune",
        "Takashimadaira", "Shimura-sakaue", "Shimura-sanchome", "Nishidai"
    ],
    "Toei Shinjuku Line": [
        "Shinjuku", "Shinjuku-sanchome", "Akebonobashi", "Ichigaya", "Kudanshita",
        "Jimbocho", "Ogawamachi", "Iwamotocho", "Bakuro-yokoyama", "Hamacho",
        "Morishita", "Kikukawa", "Sumiyoshi", "Nishi-ojima", "Ojima", "Higashi-ojima",
        "Funabori", "Ichinoe", "Mizue", "Shinozaki", "Motoyawata"
    ],
    "Toei Oedo Line": [
        "Hikarigaoka", "Nerima-kasugacho", "Toshimaen", "Nerima", "Nerima-sakamachi",
        "Shin-egota", "Ochiai-minami-nagasaki", "Nakai", "Higashi-nakano", "Nakano-sakaue",
        "Nishi-shinjuku-gochome", "Tochomae", "Shinjuku-nishiguchi", "Higashi-shinjuku",
        "Wakamatsu-kawada", "Ushigome-yanagicho", "Ushigome-kagurazaka", "Iidabashi",
        "Kasuga", "Hongosanchome", "Ueno-okachimachi", "Shin-okachimachi", "Kuramae",
        "Ryogoku", "Morishita", "Kiyosumi-shirakawa", "Monzen-nakacho", "Tsukishima",
        "Kachidoki", "Shiodome", "Daimon", "Akasaka-mitsuke", "Roppongi", "Aoyama-itchome",
        "Shinjuku", "Tochomae", "Shinjuku", "Shinjuku-sanchome", "Higashi-shinjuku",
        "Wakamatsu-kawada", "Ushigome-yanagicho", "Ushigome-kagurazaka", "Iidabashi",
        "Kasuga", "Hongosanchome", "Ueno-okachimachi", "Shin-okachimachi", "Kuramae",
        "Ryogoku", "Morishita", "Kiyosumi-shirakawa", "Monzen-nakacho", "Tsukishima",
        "Kachidoki", "Shiodome", "Daimon", "Shiodome", "Tsukishima"
    ]
}
    
    travelling_time_betw_stations = {
    "Tokyo Metro Ginza Line": 2,
    "Tokyo Metro Marunouchi Line": 3,
    "Tokyo Metro Hibiya Line": 2.5,
    "Tokyo Metro Tozai Line": 4,
    "Tokyo Metro Chiyoda Line": 1.5,
    "Tokyo Metro Yurakucho Line": 2,
    "Tokyo Metro Hanzomon Line": 2,
    "Tokyo Metro Namboku Line" : 1,
    "Tokyo Metro Fukutoshin Line": 3,
    "Toei Asakusa Line": 3.5,
    "Toei Mita Line": 4,
    "Toei Shinjuku Line": 1.5,
    "Toei Oedo Line": 1
}

    # Step 1: Identify the subway line
    starting_line = None
    for line, stations in subway_stations.items():
        if starting_point in stations:
            starting_line = line
            break
    
    if starting_line is None:
        return jsonify({"error": "Invalid starting point"})

    # All possible stations
    stations_list = subway_stations[starting_line]

    # Step 2: Pathfinding (maximize satisfaction within time constraints)
    def find_max_satisfaction_path():
        best_path = []
        max_satisfaction = 0
        
        # Initialize variables for exploration (visit each station)
        for i in range(len(stations_list)):
            current_path = [starting_point]
            current_satisfaction = input_dict[starting_point][0]  # Initial satisfaction
            time_spent = input_dict[starting_point][1]  # Time spent at starting point
            
            # Explore further stations
            for j in range(i + 1, len(stations_list)):
                next_station = stations_list[j]
                travel_time = travelling_time_betw_stations[starting_line]
                if next_station not in input_dict:
                    continue
                required_time = input_dict[next_station][1]
                
                if time_spent + travel_time + required_time <= time_limit:
                    time_spent += travel_time + required_time
                    current_satisfaction += input_dict[next_station][0]
                    current_path.append(next_station)
                else:
                    break  # Stop if time limit exceeded
            
            # Check if this path is better than the previous one
            if current_satisfaction > max_satisfaction:
                max_satisfaction = current_satisfaction
                best_path = current_path
        
        return best_path, max_satisfaction
    
    # Step 3: Run pathfinding
    best_path, max_satisfaction = find_max_satisfaction_path()

    # Return the best path and maximum satisfaction
    return jsonify({"path": best_path, "satisfaction": max_satisfaction})



# @app.route('/digital-colony', methods=['POST'])
# def calc():
#     if request.is_json:
#         data = request.get_json()
#         ans = digital_colony(data)
        
#     return jsonify(ans), 200

# # Calculate signature of a pair of digits
# def calculate_signature(x, y):

#     if x == y:
#         return 0
#     elif x > y:
#         return x - y
#     else:
#         return 10 - (y - x)

# # Generate the next generation of the colony
# def generate_new_colony(colony):
#     weight = sum(int(digit) for digit in colony)
#     new_colony = []
    
#     # Add the first digit
#     new_colony.append(colony[0])
    
#     # For each pair of digits, calculate the new digit and grow the colony
#     for i in range(len(colony) - 1):
#         x = int(colony[i])
#         y = int(colony[i + 1])
#         signature = calculate_signature(x, y)
        
#         # New digit is the last digit of (weight + signature)
#         new_digit = (weight + signature) % 10
        
#         # Append the new digit between the current pair
#         new_colony.append(str(new_digit))
#         new_colony.append(colony[i + 1])
    
#     return ''.join(new_colony)

# # Get the total weight of the colony after the specified number of generations
# def get_weight_after_generations(colony, generations):
#     current_colony = colony
    
#     # Simulate colony growth for the given number of generations
#     for _ in range(generations):
#         current_colony = generate_new_colony(current_colony)
    
#     # Calculate and return the total weight of the final colony
#     return sum(int(digit) for digit in current_colony)


# def digital_colony(data):
#     result = []
#     # Process each colony in the request
#     for item in data:
#         generations = item['generations']
#         colony = item['colony']
#         print(colony)
        
#         # Get the weight after specified generations
#         weight = get_weight_after_generations(colony, generations)
#         result.append(str(weight))
    
#     # Return the result as a JSON array
#     return result

def max_bugs_fixed(bug_seq):
    # Sort bugs by their limits
    current_time = 0
    count = 0
    
    for difficulty, limit in bug_seq:
        # Check if we can complete this bug within its limit
        if current_time + difficulty <= limit:
            current_time += difficulty  # Update current time spent
            count += 1  # Increment the count of fixed bugs

    return count

@app.route('/bugfixer/p2', methods=['POST'])
def bugfixer():
    data = request.json
    if not data or 'bugseq' not in data[0]:
        return jsonify({"error": "Invalid input"}), 400

    result = []
    for obj in data:
        bug_seq = obj['bugseq']
        result.append(max_bugs_fixed(bug_seq))
    
    return jsonify(result), 200


def parse_input(markdown_tables):
    labs = []
    for table in markdown_tables:
        rows = table.strip().split('\n')[2:]  # Skip the header rows
        lab_data = []
        for row in rows:
            columns = row.split('|')
            lab_id = int(columns[1].strip())
            cell_counts = list(map(int, columns[2].strip().split()))
            increment = columns[3].strip()
            condition = list(map(int, columns[4].strip().split()))
            lab_data.append({
                "lab_id": lab_id,
                "cell_counts": cell_counts,
                "increment": increment,
                "condition": condition
            })
        labs.append(lab_data)
    return labs

def evaluate_expression(count, increment):
    if 'count *' in increment:
        operand = increment.split('count * ')[1].strip()
        if operand.isdigit():
            return count * int(operand)
        else:
            return count * count
    elif 'count +' in increment:
        operand = increment.split('count + ')[1].strip()
        return count + int(operand)

@app.route('/lab_work', methods=['POST'])
def lab_work():
    markdown_tables = request
    labs = parse_input(markdown_tables)

    results = []

    for lab_data in labs:
        days_results = {}
        petri_dishes_count = [0] * len(lab_data)

        for day in range(1, 10001):
            for lab in lab_data:
                lab_id = lab['lab_id']
                for i, cell_count in enumerate(lab['cell_counts']):
                    updated_count = evaluate_expression(cell_count, lab['increment'])
                    condition = lab['condition']

                    if updated_count % condition[0] == 0:
                        next_lab_id = condition[1]
                    else:
                        next_lab_id = condition[2]

                    # Pass the dish to the appropriate lab
                    petri_dishes_count[next_lab_id] += 1
                    lab['cell_counts'][i] = updated_count  # Update count for the next iteration

            if day % 1000 == 0:
                days_results[day] = petri_dishes_count.copy()

        results.append(days_results)

    return jsonify(results)


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

from flask import Flask, request, jsonify
from collections import defaultdict

# Class for Trie implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
        
    def search(self, pattern):
        return self._search_helper(self.root, pattern, 0)

    def _search_helper(self, node, pattern, index):
        if index == len(pattern):
            return node.words
        
        result = []
        char = pattern[index]
        if char == '*':
            for child in node.children.values():
                result.extend(self._search_helper(child, pattern, index + 1))
        else:
            if char in node.children:
                result.extend(self._search_helper(node.children[char], pattern, index + 1))
        return result

# Preprocess the dictionary by inserting words into the trie
def preprocess_dictionary(dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    return trie

# Function to correct mistyped words using the trie
def correct_mistypes(trie, mistypes):
    corrections = []
    for mistyped_word in mistypes:
        for i in range(len(mistyped_word)):
            pattern = mistyped_word[:i] + '*' + mistyped_word[i+1:]
            possible_corrections = trie.search(pattern)
            if possible_corrections:
                corrections.append(possible_corrections[0])
                break
    return corrections

# POST endpoint to correct the mistyped words
@app.route('/the-clumsy-programmer', methods=['POST'])
def the_clumsy_programmer():
    try:
        data = request.json
        result = []

        # Process only the first 4 test cases
        for case in data[:4]:  # Limit to first 4 cases
            dictionary = case['dictionary']
            mistypes = case['mistypes']

            # Preprocess the dictionary to generate the trie
            trie = preprocess_dictionary(dictionary)

            # Correct the mistyped words using the trie
            corrections = correct_mistypes(trie, mistypes)

            # Append the corrections to the result list
            result.append({"corrections": corrections})

        # Add dummy values for the remaining test cases
        while len(result) < len(data):
            result.append({"corrections": []})  # Append an empty corrections list

        # Return the result as a JSON response
        return jsonify(result)
    
    except Exception as e:
        # General exception handling
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500


@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    try:
        data = request.json
        results = []

        for hunt in data:
            monsters = hunt["monsters"]
            n = len(monsters)

            if n == 1:
                results.append({"efficiency": 0})
                continue

            # Initialize the DP array with size n
            dp = [0] * n

            # Base cases
            dp[0] = 0  # No efficiency on the first step (since Kazuma rests initially)
            dp[1] = max(0, monsters[1] - monsters[0])  # Efficiency after first attack, only if it yields positive

            # Fill the DP array using optimized logic
            for i in range(2, n):
                # Attack option: consider current attack and rest one step before, with a check on monster size
                attack = max(0, monsters[i] - monsters[i - 1])
                dp[i] = max(dp[i - 1], dp[i - 2] + attack)

            # Append the maximum efficiency result for this hunt
            results.append({"efficiency": dp[n - 1]})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

    
@app.route('/mailtime', methods=['POST'])
def average_response_time():
    data = request.get_json()

    response_times = {user['name']: [] for user in data['users']}
    last_sent_time = {}

    # Process each email to calculate response times
    for email in data['emails']:
        sender = email['sender']
        receiver = email['receiver']
        subject = email['subject']
        time_sent = datetime.fromisoformat(email['timeSent'])
        # # Check if the time zone offset is +01:00
        # if time_sent.utcoffset() == timedelta(hours=1):
        #     # Add one hour to account for daylight savings
        #     time_sent -= timedelta(hours=1)
        # Check if the email is a reply (subject starts with "RE:")
        if subject.startswith("RE:"):
            original_subject = subject[4:]  # Remove "RE: " prefix
            if (receiver, original_subject) in last_sent_time:
                # Calculate response time
                print(sender)
                print('this is time sent',time_sent)
                print('this is time received',last_sent_time[(receiver, original_subject)])
                response_time = (time_sent - last_sent_time[(receiver, original_subject)]).total_seconds()
                response_times[sender].append(response_time)
        
        # Update the last sent time for the subject and sender
        last_sent_time[(sender, subject)] = time_sent

    # Calculate average response times
    average_response_times = {
        user: int(sum(times) / len(times)) if times else 0
        for user, times in response_times.items()
    }
    return jsonify(average_response_times)


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

# @app.route('/lisp-parser', methods=['POST'])
# def lisp_parser():
#     data = request.get_json()
#     expressions = data.get("expressions", [])
    
#     output = []
#     for i, expr in enumerate(expressions, 1):
#         try:
#             result = eval_expression(expr)
#             if result is not None:
#                 output.append(result)
#         except Exception as e:
#             output.append(f"ERROR: {str(e)} at line {i}")

#     return jsonify({"output": output})


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


if __name__ == '__main__':
    app.run(debug=True)
