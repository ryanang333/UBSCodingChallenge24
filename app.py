from flask import Flask
from flask import Flask, request, jsonify
import requests, re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/klotski', methods=['POST'])
def klotski_route():
    if request.is_json:
        data = request.get_json()
        klotski(data.board, data.moves)

def klotski(board, moves):
    #given a 5x4 box => can only slide vertically or horizontally
    positionMap = board_to_map(board, 5, 4)
    print('before positions: ', positionMap)
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
    print('after positions: ', positionMap)
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


# meaningpedia_resp = requests.get(
#     "https://meaningpedia.com/5-letter-words?show=all")

# # get list of words by grabbing regex captures of response
# # there's probably a far better way to do this by actually parsing the HTML
# # response, but I don't know how to do that, and this gets the job done

# # compile regex
# pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
# # find all matches
# word_list = pattern.findall(meaningpedia_resp.text)
word_list =['aalii', 'aaron', 'abaca', 'abaft', 'abamp', 'abase', 'abash', 'abate', 'abbot', 'abele', 'abets', 'abhor', 'abide', 'abies', 'ables', 'abode', 'abohm', 'abort', 'about',
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
 'april', 'apron', 'apses', 'apsis', 'aptly', 'aquas', 'arabs', 'arbor', 'arced', 'arcos', 'arcus', 'ardea', 'ardeb', 'ardor', 'areal', 'areas', 'areca', 'arena', 'arere', 'arete', 'argal', 'argil',
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
    input_dict = data.get('input_dict')
    starting_point = data.get('starting_point')
    time_limit = data.get('time_limit')

    # Constants (subway lines, travel times)
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
    
    # All possible stations in the starting line
    stations_list = subway_stations[starting_line]
    
    # Step 2: Pathfinding (maximize satisfaction within time constraints)
    def find_max_satisfaction_path():
        best_path = []
        max_satisfaction = 0

        for i in range(len(stations_list)):
            current_path = [starting_point]
            current_satisfaction = input_dict[starting_point][0]  # Initial satisfaction
            time_spent = input_dict[starting_point][1]  # Time spent at starting point
            
            for j in range(i+1, len(stations_list)):
                next_station = stations_list[j]
                travel_time = travelling_time_betw_stations[starting_line]
                required_time = input_dict[next_station][1]
                
                # Check if adding the next station exceeds the time limit
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
    
    best_path, max_satisfaction = find_max_satisfaction_path()

    return jsonify({
        "best_path": best_path,
        "max_satisfaction": max_satisfaction
    })


if __name__ == '__main__':
    app.run(debug=True)
