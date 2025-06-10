from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))
        
quiz = Quiz(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
print(f"Game Over!\nFinal Score: {quiz.score}/{quiz.question_num}")         
   