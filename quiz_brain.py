class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.q_list = q_list

    def go_to_next(self):
        q_current = self.q_list[self.q_no]
        self.q_no += 1
        answer = input(f"Q.{self.q_no}: {q_current.question} (True/False) ")
        self.check_answer(answer, q_current.answer)

    def still_has_questions(self):
        return self.q_no < len(self.q_list)

    def check_answer(self, a_user, a_correct):
        if a_user.lower() == a_correct.lower():
            print("Smasher!")
            self.score += 1
        else:
            print("Olodo!")
        print(
            f"The correct answer was: {a_correct}\nYour Current score is {self.score}/{self.q_no}\n"
        )
