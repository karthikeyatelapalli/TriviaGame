# Trivia Game

This Python program is a two-player trivia game where players take turns answering questions from a predefined set. Each correct answer earns a point, and the program announces the winner at the end. If both players score the same points, the game ends in a tie.

---

## **Features**
1. **Questions Class**:
   - Defines a `Trivia` class with attributes:
     - Question text.
     - Four possible answers.
     - Correct answer (as an integer corresponding to the correct option).
   - Includes a `__str__` method to format the question and its answers for display.

2. **Trivia Questions**:
   - Provides a collection of at least 10 trivia questions using the `Trivia` class.
   - Each question has:
     - Text of the question.
     - Four answer options.
     - A numerical value indicating the correct answer.

3. **Gameplay**:
   - Players take turns answering questions.
   - Correct answers earn a point.
   - At the end, the program announces the scores and determines the winner.

4. **Error Handling**:
   - Ensures player input is between 1 and 4.

---

## **How to Run**

### **Requirements**
- Python 3.x
- No additional libraries are required.

### **Steps**
1. Ensure the following files are in the same directory:
   - `questions_class.py`
   - `trivia_questions.py`
   - `trivia_game.py`
2. Run the program:
   ```ba
