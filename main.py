import random

h_men = ["""
                   --------
                   |      |
                   |      O
                   |     /|\\
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
                   |     / \\
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
class hm:                                       #class containing all functions and variables necessary for the game
    def __init__(self):                         #initialisation function
        self.guess = []
        self.word = ()
        self.l = ''
        self.al = 7


    def correct_guess(self):                    #function to be run in case of correct guess
        i = 0
        while i < len(self.word[0]):
            if self.word[0][i] == self.l:
                self.guess[i] = self.l
            i += 1
        print(self.guess)

    def accept_guess(self):                     #function to be run after accepting the letter
        if self.l.isalpha() and len(self.l) == 1:
            if self.l in self.word[0]:
                self.correct_guess()
            else:
                self.wrong_guess()
        else:
            print("you have entered an invalid character, please enter a letter: ")
            self.correct_guess()

    def wrong_guess(self):                      #function to be run in case of wrong guess
        self.al -= 1
        print("Wrong guess! You have", self.al, " guesses left.")
        print(h_men[self.al])

    def rand_word(self):                        #function to generate random word and associated hint
        m = {'astronaut':'Person living in space','android':'competes with IOS','attitude':'main feature of a person','bugatti':'car with powerful engines','dhoni':'only captain with all ICC trophies','emblem':'one of our national symbol','joker':'person who makes everyone laugh','marvel':'universe with superheroes','rollsroyce':'most comfortable cars','pressure':'students feel this all the time'}
        self.word = random.choice(list(m.items()))
        print("Hint: ", self.word[1])
        for i in self.word[0]:
             self.guess.append('_')
        print(self.guess)

    def chk(self):                                 #function to check if you have won
        i = 0
        c_guess = "".join(self.guess)
        if c_guess == self.word[0]:
            return True
        else:
            return False


    def play(self):                                 #function to start the game
        self.rand_word()
        while self.al != 0:
            if self.chk() :
                print("You have won and saved the man")
                break
            else:
                self.l = input("Enter guess: ")
                self.accept_guess()
        if self.al == 0:
            print("You have run out of guesses. The man has been hung")


h1 = hm()                                           #initialisation of object of type hm
h1.play()


