#-----------------------------------------------------------
# AUTHOR: Julianne Ong
# FILENAME: calculator.py
# SPECIFICATION: Creates a calculator that uses ChatGPT to process and calculate equations.
# FOR: CS 4800 - Assignment 1
# ESTIMATED TIME: 4 Hours
# TIME SPENT: 8:00-9:45 (1 hour 45 minutes)
#-----------------------------------------------------------

from openai import OpenAI

# Explain to user how it works, prompt for an equation to solve (in plainspeak is fine)
quitProgram = False

print ("Welcome to the AI-Powered calculator!\n")

while(not quitProgram):

    print ("Please choose a command:")
    print ("\te - Evaluate a new expression")
    print ("\ti - info")
    print ("\tq - Quit the program")

    command = input()
    expression = ""

    if(command == "e"):
        loop = True
        while(loop):
            print("\n-------------------------------------")
            print("Please enter an expression. Plaintext is fine, there is no need to format the expression.")
            expression = input()

            prompt = "Please evaluate the following expression in brackets, if and only if it is a mathematical expression.\n[" + expression + "]\nDo not use brackets in your response."

            #print(prompt)

            # Send equation prompt to OpenAI for evaluation
            client = OpenAI(
            api_key="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"
            )

            completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
            )

            response = completion.choices[0].message.content
            print(response.replace("\\", ""));
            print("-------------------------------------\n")

            print("Enter e to evaluate a new expression, or anything else to return to menu.")
            newExpression = input()
            newExpression = newExpression.lower()
            if(newExpression != "e"):
                loop = False

        print("-------------------------------------\n")
        # Return solution to user

        
    elif(command == "i"):
        print("\n-------------------------------------")
        print("AI-Powered Calculator - Developed by Julianne Ong for CS 4800")
        print("Estimated Work Time: 4 hours \n Actual Work Time: 1 hour 45 minutes")
        print("Program Description: This program uses OpenAI's API to connect to the ChatGPT learning model and evaluate a user given expression, \n\t\teven one given in plain-text rather than formatted like a proper expression.")
        print("-------------------------------------\n")
    elif(command == "q"):
        print("Thank you for using the AI-Powered calculator!")
        quitProgram = True
    else:
        print("Invalid command, please try again.")

