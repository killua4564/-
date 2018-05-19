perfect_rate = float(open('./perfect_rate', 'r').read())

def add_score_compute(condition, number, percent, score):
    if condition == 'note': return round(score * percent / number, 2)
    elif condition == 'perfect': return round(score * percent * perfect_rate / number, 2)
    elif condition == 'combo': return round(score * percent / number, 2)
    elif condition == 'second': return round(score * percent * 5 / number, 2)
    else: return .0