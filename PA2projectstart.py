'''
Katherine James PA2
This is a flashcard app that you can insert files and it will return questions to you and check your answer
WWW: I am proud of how I learned and now understand .split and .strip
If I had more time I would make it so you could create a file/deck in the program
'''

points = 0

def play_quiz(filename):
    with open(filename) as f: #f is file name so swap name for f and delete read line as cursor moves on
        for x in f:
            line = x.split(",") 
            print(line[0])
            answer = input("Enter answer: ")
            if answer == line[1].strip("\n"):
                print("Correct!")
                points += 1
            else:
                print("That is incorrect!")
    
       
#def see_history(history):
    #history = open("history.txt","x")
    #username = input("Please enter your username: ")
    #history.write(username)
    #history.write(points)
    
def add_scores(new_score):
    points = new_score
    score_file = open("score_file.txt","x")
    score_file.write(new_score)
    
def show_scores(score_file):
    print(score_file)


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
        print("Welcome to the review game")
        while first_choice not in e_options:# first runs bc first_choice == "", then because they haven't said exit
            for item in initial_choices:
                print(f"- {item}")
            first_choice = input("What would you like to do?\n> ").lower()#Function options
            if first_choice in p_options:
                quiz_fn = input("What is the name of your file?\n> ").lower().strip()#Enter file
                quiz_ext = input("Is it a .txt or .csv file?\n> ").lower().strip()#File type
                while quiz_ext not in file_types:#error
                    print_error()
                    print("Your choices are:")#Prints choices
                    for item in file_types:
                        print(f"- {item}")
                    quiz_ext = input("Is it a .txt or .csv file?\n> ").lower().strip()#file type
                if quiz_ext in [".csv","csv"]:
                    file_url = quiz_fn+".csv"
                else:
                    file_url = quiz_fn+".txt"
                user_score = play_quiz(file_url) #int score
                show_scores(user_score)
            elif first_choice in e_options:#exiting
                game_on = False
            elif first_choice in h_options:
                history = open("history.txt","a")
                username = input("Please enter your username: ")
                history.write(f"{username} : {points}\n")
                h = open("history.txt")
                print(h.read())
            else:#Error

                print_error()
            
        print("Goodbye!")

main()
    
