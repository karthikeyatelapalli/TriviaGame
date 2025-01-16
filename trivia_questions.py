# Trivia Questions
'''
Description: The Trivia Questions module defines a function which creates a list of trivia question objects. 
The module containing the definition of the Questions Class is imported. The function produces
at least 10 question objects, each of which has a question, four potential responses, and the
answer's numerical value.
'''
# Import the Trivia class from the module questions_class
from questions_class import Trivia

# Create the acquire_ques function.
def acquire_ques():
    # Make a list of the objects for trivia questions.
    questions = [
        Trivia("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2),
        Trivia("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4),
        Trivia("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3),
        Trivia("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", 2),
        Trivia("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4),
        Trivia("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1),
        Trivia("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3),
        Trivia("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2),
        Trivia("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 1),
        Trivia("How many days are in a lunar year?", "354", "365", "243", "379", 1)
    ]
    # Return a list of the items for trivia questions.
    return questions