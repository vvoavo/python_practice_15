import random
from typing import Union


def getMoveName(move_id: int) -> str:
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
    """Return bool value of win, in case of tie returns string 'tie'"""
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
    return random.randint(1, 3)


def getPlayerMove() -> int:
    isInputCorrect = False

    while not isInputCorrect:
        print("Choose your move:")
        print(f"1 - {getMoveName(1)}")
        print(f"2 - {getMoveName(2)}")
        print(f"3 - {getMoveName(3)}")
        user_input = input()
        if not user_input.isalnum() or len(user_input) > 1:
            print("\n---\nInvalid input, please choose correct option\n---\n")
            continue

        user_input = int(user_input)
        if user_input > 3 or user_input < 1:
            print("\n---\nInvalid move id, please choose correct option\n---\n")
        else:
            isInputCorrect = True
    return user_input


def playWithAI():
    isGameOn = True
    while isGameOn:
        player_move_id = getPlayerMove()
        ai_move_id = getAIMove()
        print(f"Your move\t: {getMoveName(player_move_id)}")
        print(f"Ai move\t\t: {getMoveName(ai_move_id)}")

        isWin = isFirstWinner(player_move_id, ai_move_id)
        if isWin == "tie":
            print("===TIE===")
        elif isWin:
            print("\\\\\\YOU WIN///")
        else:
            print("///YOU LOOSE\\\\\\")

        user_input = input(
            "Continue playing? [Y/y to continue | Any other input to exit]: "
        )
        if user_input == "Y" or user_input == "y":
            continue
        isGameOn = False
    print("bye!")


if __name__ == "__main__":
    playWithAI()
