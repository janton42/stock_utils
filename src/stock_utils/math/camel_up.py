"""Probability utilities for the Camel Up style game logic."""


def calculate_prob(x, r):
    """Calculate the probability of a successful outcome in the game.

    Args:
        x: Number of positive outcomes to consider.
        r: Current round number.

    Returns:
        The calculated probability of the event occurring.
    """
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
    """Convert a probability into odds.

    Args:
        p: Probability value between 0 and 1.

    Returns:
        The odds ratio as ``p / (1 - p)``.
    """
    return p/(1-p)


if __name__ == '__main__':
    x = int(input('Enter the total number of positive outcomes:  '))
    r = int(input('Which round of the game is it?  '))
    prob = calculate_prob(x, r)
    odds = calculate_odds(prob)
    output = f'Probability: {prob:.4f}\nOdds:         {odds:.4f}:1'
    print(output)

