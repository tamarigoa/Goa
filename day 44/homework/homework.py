#1)
def reverse_seq(n):
    return list(range(n, 0, -1))

# 2)
def rps(player1, player2):
    valid_choices = {"rock", "paper", "scissors"}


    if player1 not in valid_choices or player2 not in valid_choices:
        return "Invalid input!"

    if player1 == player2:
        return "Draw!"

    winning_cases = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if winning_cases[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

# 3)
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


# 4)
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3 
    
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

