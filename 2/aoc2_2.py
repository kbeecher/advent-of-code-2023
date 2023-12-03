import functools
import operator

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

def build_selections(draw_texts: list[list[str]]) -> list[list[(int, str)]]:
    return [ 
        [ parse_draw_text(dt) for dt in sts ] 
        for sts in draw_texts 
    ]


'''
GAME LOGIC
'''

def minset_power(minset: [int]) -> int:
    return functools.reduce(operator.mul, minset, 1)

def get_minset(selection: list[list[(int, str)]]) -> dict[str, int]:
    minset = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    flat_list = [ d for draws in selection for d in draws]
    
    for d in flat_list:
        if d[0] > minset[d[1]]: minset[d[1]] = d[0]

    return minset


def go():
    input = open('input.txt', 'r')
    score = 0

    for gt in input.readlines():
        draw_texts = [
            parse_draw_texts(d) 
            for d in parse_selection_texts(parse_game_text(gt)) 
        ]
        game = build_selections(draw_texts)
        score += minset_power(get_minset(game).values())
   
    print(f'Score: {score}')

if __name__ == '__main__':
    go()