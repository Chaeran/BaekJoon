#객체로 묶을 수 있을까?
class Course:
    def __init__(self, name, credit, letter):
        self.name = name
        self.credit = float(credit)
        self.letter = letter
        self.grade = 0.0       
            
    def letterToscore(self, letter):
        if letter == "A+":
            self.grade = 4.5
        elif letter == "A0":
            self.grade = 4.0
        elif letter == "B+":
            self.grade = 3.5
        elif letter == "B0":
            self.grade = 3.0
        elif letter == "C+":
            self.grade = 2.5
        elif letter == "C0":
            self.grade = 2.0
        elif letter == "D+":
            self.grade = 1.5
        elif letter == "D0":
            self.grade = 1.0
        else: #F인경우
            self.grade = 0.0
            
#이름, credit, 성적
#except 문 써서 더이상 입력이 없으면 성적 평균 프린트 후 종료

sumCredit = 0 #학점 총합
sum = 0 #성적 총합

while(1):
    try:
        name, credit, letter = input().split()
        if letter == 'P':
            continue
        a = Course(name, credit, letter)
        a.letterToscore(a.letter)
        sumCredit += a.credit
        sum += a.credit * a.grade
    except:
        print(sum/sumCredit)
        break
