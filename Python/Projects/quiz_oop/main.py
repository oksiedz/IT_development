from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# we need the list of question objects
question_bank = []
for question in question_data:
    # creation of list of objects are created from the list of dictionaries
    question_bank.append(Question(in_text=question["text"], in_answer=question["answer"]))

quiz = QuizBrain(question_bank)
quiz.nex_question()