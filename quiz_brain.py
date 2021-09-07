
class QuizBrain :
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):

        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False). ")
        self.answer_check(current_question.answer, user_answer)

    def answer_check(self, current_answer, user_answer):
        if current_answer.lower() == user_answer.lower():
            print("You've got it right!")
            self.score += 1
        else :
            print("That's wrong")
        print(f"The correct answer was {current_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

