

class Turing:
    word = None
    caret = 0
    result = None
    counter = 0
    model = None
    word_len = []
    step_count = []
    maxCount = 0
    def input_word(self):
        return input()

    def get_word(self, word):
        self.word = word

    def start(self, word, model=None):
        self.word = ' ' + word + ' '
        self.caret = 0
        self.result = None
        self.counter = 0
        self.model = model
        self.caret += 1
        self.result = self.q1()
        print(self.word)

    def get_counter(self):
        return self.counter

    def q1(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q1)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q2()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q1)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q1)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q1)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q1)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q1)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q13()

    def q2(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q2)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q2)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q3()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q2)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q2)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q2)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q2)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q13()

    def q3(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q3)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q1()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q3)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q3)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q4()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q3)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q3)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q3)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q13()

    def q4(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q4)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q4)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q5()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q4)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q4)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q4)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q4)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q13()

    def q5(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q5)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q6()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q5)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q5)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q5)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q5)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q5)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q13()

    def q6(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q6)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q6)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q4()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q6)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q6)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q6)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q6)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q7()

    def q7(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q7)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q7()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q7)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q7()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q7)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q8()

    def q8(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q8)' + self.word[self.caret + 1:]))
            self.word = self.word[:self.caret] + 'x' + self.word[self.caret + 1:]
            self.caret += 1
            self.counter += 1
            self.q9()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q8)' + self.word[self.caret + 1:]))
            self.word = self.word[:self.caret] + 'x' + self.word[self.caret + 1:]
            self.caret += 1
            self.counter += 1
            self.q9()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q8)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q8()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q8)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q8()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q8)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q8()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q8)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q11()

    def q9(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q9)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q10()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q9)' + self.word[self.caret + 1:]))
            self.counter += 1
            self.q10()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q9)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q9()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q9)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q9()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q9)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q9()
        elif self.word[self.caret] == ' ':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q9)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q12()

    def q10(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q10)' + self.word[self.caret + 1:]))
            self.word = self.word[:self.caret] + 'y' + self.word[self.caret + 1:]
            self.caret -= 1
            self.counter += 1
            self.q8()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q10)' + self.word[self.caret + 1:]))
            self.word = self.word[:self.caret] + 'y' + self.word[self.caret + 1:]
            self.caret -= 1
            self.counter += 1
            self.q8()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q10)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q9()

    def q11(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q11)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q11)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q11)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q11()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q11)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q11()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q11)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q11()
        elif self.word[self.caret] == ' ':
            self.word += '+'
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q11)' + self.word[self.caret + 1:]))
            self.counter += 1
            if(self.counter > self.maxCount):
                self.maxCount = self.counter
            print(self.counter)
            return True

    def q12(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q12)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q12)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q12)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q12()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q12)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q12()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q12)' + self.word[self.caret + 1:]))
            self.caret -= 1
            self.counter += 1
            self.q12()
        elif self.word[self.caret] == ' ':

            self.word += '+'
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q12)' + self.word[self.caret + 1:]))
            self.counter += 1
            if (self.counter > self.maxCount):
                self.maxCount = self.counter
            return True

    def q13(self):
        if self.word[self.caret] == '0':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q13)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == '1':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q13)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'c':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q13)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'x':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q13)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == 'y':
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q13)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            self.q13()
        elif self.word[self.caret] == ' ':
            self.word += '-'
            if self.model is not None:
                self.model.append(str(self.word[:self.caret] + '(q13)' + self.word[self.caret + 1:]))
            self.caret += 1
            self.counter += 1
            print(self.counter)
            if (self.counter > self.maxCount):
                self.maxCount = self.counter
            return False


