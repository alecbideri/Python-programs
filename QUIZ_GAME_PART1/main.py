from data import get_question

quesstions = get_question()

count_true = 0
count_false = 0

play = 'True'
while(play):
    for question in quesstions:
        user_answer = input(f"{question.text} ('True or False?'):")
        if user_answer.lower() == question.answer.lower():
            print("Correct!")
            count_true += 1
        else:
            print("Incorrect!!")
            count_false += 1
    answer = input("Do you still wanna play?(Type 'yes' or no) :").lower()
    if (answer == 'no'):
        play = 'False'
        print("Thanks for playing!!")
        print(f"you scored {count_true} out of {count_false + count_true}")
        break
    else:
        print("Let's hope you make it better!!")


