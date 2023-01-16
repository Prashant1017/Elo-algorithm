""" Simple program using Elo algorithm """

def elo(old, exp, score, k=32):
    """
    Calculate the new Elo rating for a player.
    """
    new = old + k * (score - exp)
    return new

"""
    There are four arguments
    old: the player's current Elo rating.
    exp: the expected score, which is calculated using the ratings of player and their opponent
    score: the actual score (1 for a win, 0 for a loss, 0.5 for a draw)
    k: the k-factor which determines the maximum change in the rating [default is 32]
"""

player1_rating = 1500
player2_rating = 1600

# Calculate the expected scores
player1_exp = 1 / (1 + 10 ** ((player2_rating - player1_rating) / 400))
player2_exp = 1 / (1 + 10 ** ((player1_rating - player2_rating) / 400))

# Player 1 wins
player1_new_rating = elo(player1_rating, player1_exp, 1)
player2_new_rating = elo(player2_rating, player2_exp, 0)

print(f"Player 1 rating: {player1_new_rating:.2f}")
print(f"Player 2 rating: {player2_new_rating:.2f}")

"""
    This will print the new ratings for both players. The rating of player 1 should have increased, while the rating of player 2 should have decreased.
"""
