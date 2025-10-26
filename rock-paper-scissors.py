import random
import time

win_limit = 3

options = ["rock", "paper", "scissors"]
win_dict = [
    "Damn you crushed the computer pretty well!(●'◡'●)",
    "Okay that's the way ahead!😁",
    "That's the vibe mate❤️‍🔥",
    "Keep crushing 😉",
    "You are the one😎",
]
lose_dict = [
    "Do better cause you ain't got that vibe🤧",
    "Bruh what?You are going down😖",
    "Ugh why do I have to see this🥴",
    "Oops seems like computer is so much better than you😶",
    "Try again ,maybe luck will be with you for once😝",
]
tie_dict = [
    "It's a TIE! UGH!!😑",
    "Man what in the hell is this ?💀",
    "Tie? but WHY? X_X",
    "Hmmmm so sed bruh.🙄",
    "No words :[ TIE!!!!",
]
count_player = 0
count_computer = 0

emoji_map = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}


def play_again():
    again = (
        input(
            "Do you want to continue playing? yes/no or see scoreboard? score or reset the score? reset: "
        )
        .lower()
        .strip()
    )

    return again


def fireworks():
    frame = ["🎉", "✨", "🥳", "✨", "🎉"]
    for emoji in frame:
        print(emoji, "Winner winner")
        time.sleep(0.4)


def losing_animation():
    frames = ["💀", "😵", "😵‍💫", "🥴", "😩", "😭"]
    for emoji in frames:
        print(emoji, "You got rekt!")
        time.sleep(0.4)


def play_game():
    global count_computer, count_player
    player_rounds = []
    computer_rounds = []

    while True:
        computer_choice = random.choice(options)
        player_choice = (
            input("Enter your choice ('rock', 'paper', or 'scissors'): ")
            .lower()
            .strip()
        )
        if player_choice not in options:
            print("Invalid choice! Try again.")
            continue

        print("Rock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("Shoot!")
        time.sleep(0.3)

        print("-------------------\n")
        print("Your choice :", player_choice, emoji_map[player_choice])
        print("Computer's choice:", computer_choice, emoji_map[computer_choice])
        print("-------------------\n")

        if player_choice == "rock" and computer_choice == "scissors":
            print("Rock crushes scissors! 🪨✂️ Boom!")
        elif player_choice == "paper" and computer_choice == "rock":
            print("Paper wraps rock! 📄🪨 Nice!")
        elif player_choice == "scissors" and computer_choice == "paper":
            print("Scissors cut paper! ✂️📄 Gotcha!")

        if player_choice == computer_choice:
            print(random.choice(tie_dict))

        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):

            print(random.choice(win_dict))
            print("YOU WIN, MATE!")
            count_player = count_player + 1
            player_rounds.append(emoji_map[player_choice])
        else:

            print(random.choice(lose_dict))
            print("THE COMPUTER GOT YOU ")
            count_computer = count_computer + 1
            computer_rounds.append(emoji_map[computer_choice])
        print("-------------------\n")

        print("Score -> You: ", count_player, " Computer: ", count_computer)

        match_over = (count_player >= win_limit) or (count_computer >= win_limit)
        if match_over:
            if count_player >= win_limit:
                fireworks()
                print(
                    "CONGRATS! YOU'VE WON THE MATCH! SLAY ~~~~~❤️‍🔥\nPamparampam 🎷🍾🥳🙌"
                )
            else:
                losing_animation()
                print(
                    "OH NO! YOU LOSE AND THE COMPUTER WINS!\nFIND SOMEWHERE TO HIDE YOUR FACE💀\n"
                )

        while True:  # ask to play again until valid input
            again = play_again()
            if again == "score":
                print(
                    "Score -> You: ",
                    "".join(player_rounds),
                    f"({count_player})",
                    " | Computer: ",
                    "".join(computer_rounds),
                    f"({count_computer})",
                )
                continue

            if match_over:
                if again in ("yes", "reset"):
                    count_player = 0
                    count_computer = 0
                    print("Scores reset. Starting a new match!\n")
                    print("OKIE! Get ready for the next match! ⚡")
                    break
                elif again == "no":
                    print("Thank you for playing. Goodbye!")
                    return
                else:
                    print("Please enter yes / no / score / reset.")
                    continue
            else:
                if again == "yes":
                    break
                elif again == "no":
                    print("Thank you for playing😊. Goodbye!❤️")
                    return
                elif again == "reset":
                    count_player = 0
                    count_computer = 0
                    print("Scores reset. Continuing with fresh scores.\n")
                    break
                else:
                    print("Please enter yes / no / score / reset.")
                    continue


def main():
    print("Welcome to my mini ROCK-PAPER-SCISSOR game! Have fun~~❤️")
    play_game()


main()