import random
from typing import Union
import doctest


def getMoveName(move_id: int) -> str:
    """Returns string value of the move
    >>> getMoveName(1)
    "Rock"
    >>> getMoveName(2)
    "Paper"
    >>> getMoveName(3)
    "Scissors"
    >>> getMoveName(0)
    "INVALID_MOVE"
    """
    match move_id:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"
        case _:
            return "INVALID_MOVE"


def isFirstWinner(move1_id: int, move2_id: int) -> Union[bool, str]:
    """Return bool value of win of the first passed move, in case of tie returns string 'tie'"""
    if move1_id == 1 and move2_id == 3:
        return True
    elif move1_id == 2 and move2_id == 1:
        return True
    elif move1_id == 3 and move2_id == 2:
        return True
    elif move1_id == move2_id:
        return "tie"
    else:
        return False


def getAIMove() -> int:
    """Returns random integer between 1 and 3
    this single line action is wrapped into a function for better understanding of game's code
    """
    return random.randint(1, 3)


def getPlayerMove() -> int:
    """Asks player to make it's move input in console"""
    isInputCorrect: bool = False

    while not isInputCorrect:
        print("Choose your move:")  # asking player to choose their move
        print(f"1 - {getMoveName(1)}")
        print(f"2 - {getMoveName(2)}")
        print(f"3 - {getMoveName(3)}")
        user_input = input()  # reading input
        if (
            not user_input.isalnum() or len(user_input) > 1
        ):  # if input is not a number or too large
            print(
                "\n---\nInvalid input, please choose correct option\n---\n"
            )  # inform user aboiut it
            continue  # and start again

        user_input = int(user_input)  # type: ignore
        if user_input > 3 or user_input < 1:  # type: ignore                     # if user input is wrong integer value
            print(
                "\n---\nInvalid move id, please choose correct option\n---\n"
            )  # inform user about it
            continue  # and start again
        else:
            isInputCorrect = True  # if evetyrhing is correct, this flag gets marked and cycle ends, returning id of chosen move
    return user_input  # type: ignore


def playWithAI():
    """Starts rock paper scissors game with ai"""
    isGameOn: bool = True  # marks that game is still going

    player_pts: int = 0  # player wins
    ai_pts: int = 0  # ai wins
    tie_pts: int = 0  # amount of ties

    while isGameOn:
        player_move_id: int = getPlayerMove()  # get player move id
        ai_move_id: int = getAIMove()  # get ai move id
        print(
            f"Your move\t: {getMoveName(player_move_id)}"
        )  # display moves to the user
        print(f"Ai move\t\t: {getMoveName(ai_move_id)}")

        isWin: Union[bool, str] = isFirstWinner(
            player_move_id, ai_move_id
        )  # checking what are the results of this turn
        if isWin == "tie":
            print("===TIE===")
            tie_pts += 1
        elif isWin:  # if user wins add point to player_pts
            print("\\\\\\YOU WIN///")
            player_pts += 1
        else:  # if ai wins add point to ai_pts
            print("///YOU LOOSE\\\\\\")
            ai_pts += 1

        print("Points:")  # printing out current points
        print(f"Player\t: {player_pts}")
        print(f"Ai\t: {ai_pts}")
        print(f"\nTies\t: {tie_pts}")

        user_input: str = input(
            "\nDo you want to exit the game? [Y]"
        )  # giving player ability to exit the game
        if user_input == "Y" or user_input == "y":
            isGameOn = False

    print("bye!")


# starts the game
if __name__ == "__main__":
    playWithAI()
