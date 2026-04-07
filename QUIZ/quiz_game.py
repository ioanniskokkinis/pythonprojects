from Words import questions  # Assuming 'questions' is a list in words.py
from answers import answers    

count = 0

for i in range(10):
    print(f"\nQuestion {i+1}: {questions[i]}")
    
    while True:
        na = input("Give me an option between 1 and 3: ")
        
        # Validate that the input is one of the allowed strings
        if na in ["1", "2", "3"]:
            # Check if the answer is correct
            # Note: ensuring both are strings for a valid comparison
            if str(answers[i]) == na:
                count += 1
                print("Correct!")
            else:
                print("Wrong answer.")
            
            # Break the while loop once a valid input is provided
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

print(f"\nGame Over! Your final score is: {count}/10")