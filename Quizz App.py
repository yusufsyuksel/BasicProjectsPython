# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer
    
# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0

    def getQuestion(self):
        return self.questions[self.questionsIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print('-----------------------')
        print(f'Soru {self.questionsIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)

        answer = input('Cevap: ')
        if (question.checkAnswer(answer)):
            print('DOĞRU CEVAP')
        else:
            print('YANLIŞ CEVAP')
        print('-----------------------')
        self.quess(answer)
        self.loadQuestion()
        

    def quess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionsIndex += 1

    
    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            

    def showScore(self):
        print('Skor:',self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionsIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))
        

    
q1 = Question('En iyi prograhangisidirmlama dili  ?', ['C#','Python','Javascript','Java'], 'Python')
q2 = Question('En popüler dil hangisidir ?', ['Python','C#','Javascript','Java'], 'Python')
q3 = Question('En çok kazandıran dil hangisidir ?', ['C#','Javascript','Python','Java'], 'Python')

questions = [q1,q2,q3,]
        
quiz = Quiz(questions)

quiz.loadQuestion()
