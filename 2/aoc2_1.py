MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

'''
PARSING
'''
def parse_game_text(line: str) -> str:
    return line.split(':')[1]

def parse_selection_texts(line: str) -> list[str]:
    return line.split(';')

def parse_draw_texts(line: str) -> list[str]:
    return list(map(str.strip, line.split(',')))

def parse_draw_text(line: str) -> (int, str):
    elems = line.split(' ')
    return ( int(elems[0]), elems[1] )


'''
GAME LOGIC
'''
def build_selections(draw_texts: list[list[str]]) -> list[list[(int, str)]]:
    return [ 
        [ parse_draw_text(dt) for dt in sts ] 
        for sts in draw_texts 
    ]

def is_draw_impossible(count: int, colour: str) -> bool:
    if colour == 'red' and count > MAX_RED: return True
    if colour == 'blue' and count > MAX_BLUE: return True
    if colour == 'green' and count > MAX_GREEN: return True

    return False

def is_game_impossible(game: list[list[(int, str)]]) -> bool:
    for selection in game:
        for draw in selection:
            if is_draw_impossible(draw[0], draw[1]):
                return True

    return False


def go():
    input = open('input.txt', 'r')
    n = 0
    score = 0

    for gt in input.readlines():
        n += 1

        draw_texts = [
            parse_draw_texts(d) 
            for d in parse_selection_texts(parse_game_text(gt)) 
        ]
        game = build_selections(draw_texts)
        
        if not is_game_impossible(game):
            score += n
   
    print(f'Score: {score}')

if __name__ == '__main__':
    go()