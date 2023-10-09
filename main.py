from data import question_data as questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in questions:
    new_question = Question(question["q"], question["a"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.go_to_next()

print(
    f"Congrats! You've completed the quiz!\nYour final score was {quiz.score}/{quiz.q_no}"
)
