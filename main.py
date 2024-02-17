#the project was improved with UI and new data (api)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []

#making questions
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_answer))

#quizbrain
quiz = QuizBrain(question_bank)


#game running

quiz_ui = QuizUI(quiz)

# while quiz.game_on():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")