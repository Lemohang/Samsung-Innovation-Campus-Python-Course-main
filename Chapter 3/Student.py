class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.eng_quiz = []
        self.math_quiz = []
        self.science_quiz = []
    
    def set_name(self, name):
        self.name = name

    def set_student_id(self, student_id):
        self.student_id = student_id
    def set_eng_quiz(self, eng_quiz):
        self.eng_quiz = eng_quiz
    def set_math_quiz(self, math_quiz):
        self.math_quiz = math_quiz

    def set_science_quiz(self, science_quiz):
        self.science_quiz = science_quiz
    
    def get_name(self):
        return self.name
    def get_student_id(self):
        return self.student_id
    def get_eng_quiz(self):
        return self.eng_quiz
    def get_math_quiz(self):
        return self.get_math_quiz
    def get_science_quiz(self):
        return self.science_quiz
    
    def get_total_score(self):
        return sum(self.eng_quiz) + sum(self.math_quiz) + sum(self.science_quiz)
    
    def get_avg_score(self):
        return (sum(self.eng_quiz) + sum(self.math_quiz) + sum(self.science_quiz)) / 3
    def __str__(self):
        return "Name: {}, Student ID: {}, English Quiz: {}, Math Quiz: {}, Science Quiz: {}".format(self.name, self.student_id, self.eng_quiz, self.math_quiz, self.science_quiz)