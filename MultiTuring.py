class MultiTuring:
    word1 = None
    word2 = None
    caret1 = 0
    caret2 = 0
    result = None
    counter = 0
    model = None
    model2 = None
    word_len = []
    step_count = []
    maxCount = 0

    def start(self, word, model=None, model2=None):
        self.word1 = ' ' + word + ' '
        self.word2 = '   '
        self.caret1 = 0
        self.caret2 = 0
        self.result = None
        self.counter = 0
        self.model = model
        self.model2 = model2
        self.caret1 = 1
        self.caret2 = 1
        self.q1()
        print(self.word1)
        print(self.word2)
        # 0101c1010
        # 0101

    def q1(self):
        if self.word1[self.caret1] == '0' and self.word2[self.caret2] == ' ':
            self.word2 = self.word2[:self.caret2] + '0' + self.word2[self.caret2 + 1:] + ' '
            self.insert_state('(q1)')
            self.caret1 += 1
            self.caret2 += 1
            self.counter += 1
            self.q2()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == ' ':
            self.insert_state('(q1)')
            self.caret1 += 1
            self.caret2 -= 1
            self.counter += 1
            self.q3()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == ' ':
            self.insert_state('(q1)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == ' ':
            self.insert_state('(q1)')
            self.counter += 1
            self.q5()

    def q2(self):
        if self.word1[self.caret1] == '0' and self.word2[self.caret2] == ' ':
            self.insert_state('(q2)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == ' ':
            self.insert_state('(q2)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == ' ':
            self.word2 = self.word2[:self.caret2] + '1' + self.word2[self.caret2 + 1:] + ' '
            self.insert_state('(q2)')
            self.caret1 += 1
            self.caret2 += 1
            self.counter += 1
            self.q1()

    def q3(self):
        if self.word1[self.caret1] == '1' and self.word2[self.caret2] == '1':
            self.insert_state('(q3)')
            self.caret1 += 1
            self.caret2 -= 1
            self.counter += 1
            self.q3()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == '0':
            self.insert_state('(q3)')
            self.caret1 += 1
            self.caret2 -= 1
            self.counter += 1
            self.q3()
        elif self.word1[self.caret1] == ' ' and self.word2[self.caret2] == ' ':
            self.insert_state('(q3)')
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == '1':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == ' ' and self.word2[self.caret2] == '1':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == ' ' and self.word2[self.caret2] == '0':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == '0':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == '1':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == '0':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == ' ':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == ' ':
            self.insert_state('(q3)')
            self.counter += 1
            self.q5()

    def q4(self):
        if self.word1[self.caret1] == '1' and self.word2[self.caret2] == '1':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == '0':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == '1':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == ' ' and self.word2[self.caret2] == '1':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == ' ' and self.word2[self.caret2] == '0':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == '0':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == '1':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == '0':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == ' ':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == ' ':
            self.insert_state('(q4)')
            self.caret1 += 1
            self.counter += 1
            self.q4()
        elif self.word1[self.caret1] == ' ':
            self.word1 += '+'
            self.insert_state('(q4)')
            self.counter += 1
            if self.counter > self.maxCount:
                self.maxCount = self.counter
            return True

    def q5(self):
        if self.word1[self.caret1] == '1' and self.word2[self.caret2] == '1':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == '0':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == '1':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == '0':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == '1':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == ' ':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == 'c' and self.word2[self.caret2] == '0':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '1' and self.word2[self.caret2] == ' ':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == '0' and self.word2[self.caret2] == ' ':
            self.insert_state('(q5)')
            self.caret1 += 1
            self.counter += 1
            self.q5()
        elif self.word1[self.caret1] == ' ':
            self.word1 += '-'
            self.insert_state('(q5)')
            self.counter += 1
            if self.counter > self.maxCount:
                self.maxCount = self.counter
            return True

    def insert_state(self, state):
        if self.model is not None and self.model2 is not None:
            self.model.append(str(self.word1[:self.caret1] + state + self.word1[self.caret1 + 1:]))
            self.model2.append(str(self.word2[:self.caret2] + state + self.word2[self.caret2 + 1:]))

# 0101c1010
# 0101
tur = MultiTuring()
tur.start("01с")
