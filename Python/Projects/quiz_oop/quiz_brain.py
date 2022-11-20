#TODO: asking a question
#TODO: checking if the answer is correct
#TODO: checking if we're at the of the quiz

# attributes - question_number = 0, questions_list
# method - next question()

class QuizBrain:
    def __init__(self, in_question_list):
        """Constructor stetting question number to 0 and as questions_list provided input"""
        self.question_number = 0
        self.questions_list = in_question_list

    def next_question(self):
        """Method asking the next question"""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")

    def still_have_questions(self):
        """Method returns boolean if there are still questions which were not asked"""
        return self.question_number < len(self.questions_list)

