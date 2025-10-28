'''
Make a flashcard review game that reads through a file
where each line consists of a term and its definition.

An example text file and an example CSV file have been provided to you.

A masterful program includes the ability to create a new file
and load your own terms/definitions into it, before running the quiz on that file.

Save game records to a different file. Log username and high score.
Allow the user the option to view this file by printing it to the console.

You should at minimum edit the helper functions.
You may not necessarily have to edit the main function.
'''

def show_scores():
    score_file = open("score_file.txt","x")
    score_file.write(points)
    points = 0
    username = input("Please enter your username:")
    score_file.write(username)


def play_quiz(filename):
    print(filename.readline())
    while line != ",\n":
        line = (filename.readline())
    input("")
    if input != (filename.readline()):
        input("Error please try again:")
    if input == (filename.readline()):
        points = +1
        for i in filename:
            (filename.read())
        
    
    

def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

def main():
    #initialize variables
    initial_choices = ["play","see history","exit"]
    file_types = [".txt", ".csv", "txt", "csv"]
    p_options = ["play","p","play game"]
    h_options = ["see history", "history", "h", "see", "sh", "s"]
    e_options = ["exit","e","exit game"]
    first_choice = ""
    game_on = True

    while game_on:
        print("welcome to the review game")
        while first_choice not in e_options:# first runs bc first_choice == "", then because they haven't said exit
            for item in initial_choices:
                print(f"- {item}")
            first_choice = input("what would you like to do?\n> ").lower().strip()#Function options
            if first_choice in p_options:
                quiz_fn = input("what is the name of your file?\n> ").lower().strip()#Enter file
                quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()#File type
                while quiz_ext not in file_types:#error
                    print_error()
                    print("your choices are:")#Prints choices
                    for item in file_types:
                        print(f"- {item}")
                    quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()#file type
                if quiz_ext in [".csv","csv"]:
                    file_url = quiz_fn+".csv"
                else:
                    file_url = quiz_fn+".txt"
                play_quiz(file_url)
                show_scores()
            elif first_choice in e_options:#exiting
                game_on = False
            else:#Error
                print_error()
        
        print("Goodbye!")

main()
    
'''
Sunday night study hall, start:
- add quizing/flash card program
- add program for correct and incorrect answers
- loop back to start
- delete print of functions such as play quiz function
- edit helper functions (play, exit etc.)
- create quiz file
- quiz file must have the same character seperating word and solution
- add title to txt
'''