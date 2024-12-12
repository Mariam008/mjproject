import random

def hangman():
    print("მოგესალმებით Hangman-ის თამაშში!")

    # წინასწარ განსაზღვრული სიტყვების სია
    word_list = ["apple", "banana", "cherry", "orange"]

    # შემთხვევითი სიტყვის არჩევა
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    # ფარული სიტყვა ქვედა ტირეებით
    display = ["_" for _ in range(word_length)]
    lives = 6

    print("სიტყვა: ", " ".join(display))

    game_over = False

    while not game_over:
        guess = input("გამოიცანი ასო: ").lower()

        # ასოს ვალიდაცია
        if len(guess) != 1 or not guess.isalpha():
            print("გთხოვთ, შეიყვანოთ მხოლოდ ერთი ასო.")
            continue

        if guess in display:
            print("ეს ასო უკვე გამოიცანით.")
            continue

        # ასოს შემოწმება სიტყვაში
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
            print(f"სწორია! ასო '{guess}' არის სიტყვაში.")
        else:
            lives -= 1
            print(f"არასწორია. თქვენ გაქვთ {lives} მცდელობა დარჩენილი.")

        print("სიტყვა: ", " ".join(display))

        # გამარჯვების ან წაგების შემოწმება
        if "_" not in display:
            game_over = True
            print(f"გილოცავთ! თქვენ გამოიცანით სიტყვა: {chosen_word}")
        elif lives == 0:
            game_over = True
            print(f"დამარცხდით! სიტყვა იყო: {chosen_word}")

if __name__ == "__main__":
    hangman()

