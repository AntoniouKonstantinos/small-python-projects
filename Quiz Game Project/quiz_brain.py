class Quiz:
    
    def __init__(self, a_list):
        self.question_num = 0
        self.q_list = a_list
        self.score = 0
        
    def still_has_questions(self):
        return self.question_num < len(self.q_list)
      
    def next_question(self):
        current_q = self.q_list[self.question_num]
        answer = input(f"Q.{self.question_num + 1}: {current_q.text}. (True/False)? : ")
        self.check_answer(answer)
        self.question_num += 1
    
    def check_answer(self, answer):
        correct_answer = self.q_list[self.question_num]
        print("\n")
        if answer.lower() == correct_answer.answer.lower():
            self.score += 1
            print(f"You got it right!\nCurrent score: {self.score}/{self.question_num+1}")
        else:
            print(f"Sorry wrong answer!\nCurrent score: {self.score}/{self.question_num+1}")    
        print("\n")
