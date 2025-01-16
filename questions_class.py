# Questions Class
'''
Description: The Questions Class module defines a class which corresponds to a trivia question. It includes six characteristics, including the question itself,
four potential responses, and the number of the right response. These properties are initialized via the class's init function, and other methods
can be added if required. The trivia game will use the questions that are created using the model provided in this module.
'''
# Define the Trivia class.
class Trivia:
    # Define the six parameters needed for the initialization function.
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        # Set the class's instance variables to the arguments received
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

    # Define the class's string representation
    def __str__(self):
        # Output a formatted string with the query and the four possible responses.
        return f"{self.question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}"
