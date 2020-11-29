class Turing:
    word = []
    caret = 0
    result = None

    def input_word(self):
        return input()

    def start(self):
        self.word = ' '
        self.word += self.input_word()
        self.word += ' '
        self.caret += 1
        self.result = self.q1()
        print(self.word)

    def q1(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q2()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.q13()

    def q2(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q3()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.q13()

    def q3(self):
        if self.word[self.caret] == '0':
            self.q1()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q4()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.q13()

    def q4(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q5()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.q13()

    def q5(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q6()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.q13()

    def q6(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == '1':
            self.q4()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret -= 1
            self.q7()

    def q7(self):
        if self.word[self.caret] == '0':
            self.caret -= 1
            self.q7()
        elif self.word[self.caret] == '1':
            self.caret -= 1
            self.q7()
        elif self.word[self.caret] == 'c':
            self.caret -= 1
            self.q8()

    def q8(self):
        if self.word[self.caret] == '0':
            self.word = self.word[:self.caret] + 'x' + self.word[self.caret + 1:]
            self.caret += 1
            self.q9()
        elif self.word[self.caret] == '1':
            self.word = self.word[:self.caret] + 'x' + self.word[self.caret + 1:]
            self.caret += 1
            self.q9()
        elif self.word[self.caret] == 'c':
            self.caret -= 1
            self.q8()
        elif self.word[self.caret] == 'x':
            self.caret -= 1
            self.q8()
        elif self.word[self.caret] == 'y':
            self.caret -= 1
            self.q8()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.q11()

    def q9(self):
        if self.word[self.caret] == '0':
            self.q10()
        elif self.word[self.caret] == '1':
            self.q10()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q9()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q9()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q9()
        elif self.word[self.caret] == ' ':
            self.caret -= 1
            self.q12()

    def q10(self):
        if self.word[self.caret] == '0':
            self.word = self.word[:self.caret] + 'y' + self.word[self.caret + 1:]
            self.caret -= 1
            self.q8()
        elif self.word[self.caret] == '1':
            self.word = self.word[:self.caret] + 'y' + self.word[self.caret + 1:]
            self.caret -= 1
            self.q8()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q9()

    def q11(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q11()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q11()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q11()
        elif self.word[self.caret] == ' ':
            self.word += '+'
            return True

    def q12(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            self.caret -= 1
            self.q12()
        elif self.word[self.caret] == 'x':
            self.caret -= 1
            self.q12()
        elif self.word[self.caret] == 'y':
            self.caret -= 1
            self.q12()
        elif self.word[self.caret] == ' ':
            self.word += '+'
            return True

    def q13(self):
        if self.word[self.caret] == '0':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == '1':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            self.caret += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.caret += 1
            self.word += '-'
            return False


tur = Turing()
tur.start()
