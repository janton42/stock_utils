def calculate_prob(x, r):
    n = 7 - r
    p_die_chosen = 1/n
    p_dice_face = 0.333
    p_event = p_die_chosen * p_dice_face
    prob = 0
    while x > 0:
        prob += p_event
        x -= 1
    return prob

def calculate_odds(p):
    return p/(1-p)

if __name__ == '__main__':
    x = int(input('Enter the total number of positive outcomes:  '))
    r = int(input('Which round of the game is it?  '))
    prob = calculate_prob(x, r)
    odds = calculate_odds(prob)
    output = f'Probability: {prob:.4f}\nOdds:         {odds:.4f}:1'
    print(output)

