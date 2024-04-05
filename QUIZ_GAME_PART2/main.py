from quiz_brain import get_questiona

questions = get_questiona()

count_true = 0
count_false = 0
play = True

while(play):
    for question in questions:
        user_input = input(f"{question.text} ('True or false?'):")
        if user_input.lower() == question.answer.lower():
            print("Correct")
            count_true+=1
        else:
            count_false+=1
    answer = input("Do you still wanna play ('Yes or 'No')")
    if answer.lower()=='no':
        print("Thanks for playing")
        print(f"You scores {count_true} out of {count_false + count_true}")
        play = False
    else:
        print("Welcome back")
        print("____________\n")

