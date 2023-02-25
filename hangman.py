import random
from WordsForHangman import word_list as lst

# getting a random word from a word list


def get_word():
    rand_word = random.choice(lst)
    return rand_word

# prints hangman bodies


def hangman(num):
    bod = [
        """
                           --------
                           |      |
                           |      O
                           |     \\|/
                           |      |
                           |     / \\
                           -
                        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """

        ]
    print(bod[num])

# to update the string according to how player guesses


def st_updt(s, w, c):
    word_as_list = list(s)
    ind = []
    for i in range(0, len(w)):
        if c == w[i]:
            ind.append(i)
    for i in ind:
        word_as_list[i] = w[i]
    new_str = "".join(word_as_list)
    return new_str


# Game starts
print("----------HANGMAN----------")
tries = 6
word = get_word()
st = "_" * len(word)
guessed_letters = []
guessed_words = []

while tries > 0:
    hangman(tries)
    print(st)
    guessed = input("guess a letter or word : ")
    if len(guessed) == 1 and guessed not in guessed_letters:
        if guessed in word:
            guessed_letters.append(guessed)
            print(f"Nice, {guessed} is in the word")
            st = st_updt(st, word, guessed)
        if '_' not in st:
            print("Hooray!! you guessed the word correctly")
            break
        elif guessed not in word:
            tries -= 1
            print("oops!! wrong guess")
            guessed_letters.append(guessed)
    elif len(guessed) == 1 and guessed in guessed_letters:
        print("you have already made that guess. try a new letter")
    else:
        if guessed == word:
            print("Hooray!! you guessed the word correctly")
            break
        else:
            tries -= 1
            print("Oops!! wrong word")
else:
    hangman(tries)
    print("you lost")
