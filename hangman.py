 # Hangman game
 
import random

hangman_art = { 1:("       ",
                   "       ",
                   "       ",
                   "       ",
                   "       "),
                2:("       |",
                   "       |",
                   "       ",
                   "       ",
                   "       ",),
                3:("      |", 
                   "      |",
                   "      o",
                   "       ",
                   "       "),
                4:("      |",
                   "      |",
                   "      o",
                   "      |",
                   "      ",),
                5:("      |",
                   "      |",
                   "      o",
                   "     /|\\",
                   "        "),
                6:("      |",
                   "      |",
                   "      o",
                   "     /|\\",
                   "     / \\")}
def main():
    mistake = 0
    lives = 5
    row = []
    words = ["apple", "banana", "pineapple", "mango"]
    random_word = random.choice(words)
    print("----------------------------")
    print("Welcome to the hangman game!")
    print("----------------------------")
    row.extend("_" * len(random_word))
    while True: 
        print(f"You have {lives} lives left.")
        print(*hangman_art.get(mistake + 1), sep="\n")
        print(*row)
        if lives == 0:
            print("You lost! Better luck next time!")
            break
        if "_" not in row:
            print("Congratulations! You won!")
            break
        while True:
            answer = input("Enter a letter: ").lower()
            if answer.isalpha() == True and len(answer) == 1:
                if answer in random_word:
                    indices = [i for i,x in enumerate(random_word) if x == answer]
                    for index in indices:
                        row[index] = answer
                else:
                    mistake += 1
                    lives -= 1
                break
            else: 
                print("Invalid letter entered.")


if __name__ == "__main__":
    main()