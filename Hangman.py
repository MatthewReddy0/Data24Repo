def get_initial_word() -> str:
    parser = True                                                        ##'Parser' here used with the while loop to ensure
    while parser:                                                        ##that all inputs are only alphabetical
        key = input("Please enter the word you want them to guess: ")    ##Gets input
        if key.isalpha():                                                ##Checks for alphabetical answer
            return key.lower()                                                   ##Returns the word if good
        else:
            print("Try again, make sure the word only contains letters") ##Loops again if not
def generate_key(string: str) -> str:                                    ##Takes the accepted initial word
    length = len(string)                                                 ##gets its length
    guess_string = ""
    for i in range(length):                                              ##and fills an empty string with underscores
        guess_string += "_"                                              ##to match the answer key
    return guess_string


# Function that draws the picture after each guess. Takes in th number of incorrect guesses.
def draw_picture(count: int):
    for i in range(count):
        print(list_of_drawings[i])
    print(f'                 {8-count} lives left')
    return 0


list_of_drawings = ['  _________'
, '  |       |'
, ' ( )      |'
, '  |       |'
, ' /|\      |'
, '  |       |'
, ' / \      |'
, '/   \     |      <-- Dead']


def get_input(guessed_letters) -> str:                                          ##Will output the guess as a length 1 string
    error = True
    while error:                                                                ##While loop to ensure correct format
        guess = input("Please enter one letter to guess - ")
        if len(guess) > 1 or guess.isalpha() == False:
            print("Try again, make sure it's only one letter")
        elif guess.lower() in guessed_letters:
            print(f"Try again, you have already guessed {guessed_letters}")
        else:
            return guess.lower()


def log_input(guessed_letters: str, guess: str) -> str:                           ##Appends guess onto list of current
    return guessed_letters + guess                                                ##guesses
def is_letter_in_the_word(letter: str, word: str) -> bool:
    return letter.lower() in word.lower()


# What to do if the guess is correct
def letter_is_right(word: str, letter: str, underscores:str, count: int):
    print('Correct.')
    draw_picture(count)
    where_is_the_character = []
    for position, character in enumerate(word):
        if (character == letter):
             where_is_the_character.append(position)
#        print(where_is_the_character)
    for i in where_is_the_character:
        underscores = underscores[:i] + letter + underscores[i + 1:]
    print(underscores+"\n")
    return underscores


# What to do if letter is incorrect
def letter_is_wrong(letter:str, count: int):
    print(f'Wrong. {letter} is not in the word.')
    count += 1
    draw_picture(count)
#    print(f'\n{print_word()}')
    return count


def print_past_guesses(strang):
    list =[]
    for i in range(len(strang)):
        list.append(strang[i])
    print(f"So far you have guessed: {list}")
    return 0
def final_check(answer: str, guess: str, lives: int) -> bool:
    if answer != guess:
        print(f"Your current guess is {guess}, and you have {lives} guesses left.\n")
        return False
    else:
        return True

answer_str = get_initial_word()
guess_str = generate_key(answer_str)
incorrect_guesses_no = 0
past_guesses_vals = ""
while incorrect_guesses_no < 8:
    print_past_guesses(past_guesses_vals)
    this_guess = get_input(past_guesses_vals)
    past_guesses_vals = log_input(past_guesses_vals, this_guess)


    if is_letter_in_the_word(this_guess, answer_str):
        guess_str = letter_is_right(answer_str, this_guess, guess_str, incorrect_guesses_no)
    else:
        incorrect_guesses_no = letter_is_wrong(this_guess, incorrect_guesses_no)
    if final_check(answer_str, guess_str, 8-incorrect_guesses_no):
        break
if incorrect_guesses_no == 8:
    print("You have killed a man on this day.\nLook at him")
    draw_picture(8)
else:
    print("Congratulations! Man has not hanged :)")