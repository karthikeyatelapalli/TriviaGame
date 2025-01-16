# Driver Program
'''
Description: The main function that runs the trivia game is included in the driver software module. The module holding the collection of trivia
questions is imported. Two players take turns answering five or more questions each while the game is played between them. The 
player inputs their response after the software presents the question and four potential replies for each one. The player receives 
a point if the response is accurate. The application displays the points each player has earned once all questions have been answered,
and if both players have the same score, a tie is declared.

'''
# Import the get_questions function from the trivia_questions module
from trivia_questions import acquire_ques

# Define the play_game function, which accepts a list of questions.
def play_game(questions):
    # Make both players' starting scores zero.
    player1_score = 0
    player2_score = 0

    # Loop through each question in the list of questions.  
    for i in range(len(questions)):
        if i % 2 == 0:
            print("Question for the first player:")
        else:
            print("Question for the second player:")
        # Print the question and potential solutions.
        print(questions[i])
        # Request that the player enter their response.
        player_answer = int(input("Enter your solution (a number between 1 and 4): "))

        # Verify the correctness of the player's response.  
        if player_answer == questions[i].correct_answer:
            # Give the player a point if their response is correct.
            if i % 2 == 0:
                player1_score += 1
            else:
                player2_score += 1
            # Print a message confirming the correctness of the response.    
            print("That is the correct answer.\n")
        else:
            print("That is incorrect. The correct answer is", questions[i].correct_answer,"\n" )
                  

    # Display the players' combined final scores
    print("The first player earned", player1_score, "points.")
    print("The second player earned", player2_score, "points.")

    # Determine if the players are tied and display the appropriate message. 
    if player1_score == player2_score:
        print("It's a tie!")
    elif player1_score > player2_score:
        print("The first player wins the game.")
    else:
        print("The second player wins the game.")

if __name__ == '__main__':
    questions = acquire_ques()
    play_game(questions)
