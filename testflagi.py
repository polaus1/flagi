from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
app = QApplication([])

start_window = QWidget()
start_window.setWindowTitle('Тест на флаги')
start_window.setFixedSize(600, 400)

start_text = QLabel('это тест на флаги, проверь знание географии')
start_text.setFont(QFont('Arial', 20))

start_button = QPushButton('унижать глупый бургер')
start_button.setFont(QFont('Arial', 50))
start_button.setStyleSheet('''
    QPushButton {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #00bfff, stop:1 #006699);
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #006699, stop:1 #00bfff);
    }
''')
start_button.setCursor(QCursor(Qt.PointingHandCursor))

start_imagepic = QLabel()
start_image = QPixmap()
start_image = start_image.scaled(300, 200)
start_imagepic.setPixmap(start_image)

start_layout = QVBoxLayout()
start_layout.addWidget(start_text, alignment=Qt.AlignCenter)
start_layout.addWidget(start_imagepic, alignment=Qt.AlignCenter)
start_layout.addWidget(start_button, alignment=Qt.AlignCenter)

start_window.setLayout(start_layout)
start_window.show()


window = QWidget()
window.setWindowTitle('Тест на флаги')
window.setFont(QFont('Calibri', 20))
main_layout = QVBoxLayout()
question = QLabel('Какой это флаг')
main_layout.addWidget(question, alignment=Qt.AlignCenter)

question_image_label = QLabel()
question_image = QPixmap()
question_image = question_image.scaled(300,200)
question_image_label.setPixmap(question_image)
main_layout.addWidget(question_image_label, alignment=Qt.AlignCenter)

group_buttons = QGroupBox('Варианты ответа')

answer1 = QRadioButton('1')
answer2 = QRadioButton('2')
answer3 = QRadioButton('3')
answer4 = QRadioButton('4')
layout_btn_main = QHBoxLayout()
layout_btn_left = QVBoxLayout()
layout_btn_left.addWidget(answer1, alignment=Qt.AlignCenter)
layout_btn_left.addWidget(answer2, alignment=Qt.AlignCenter)
layout_btn_right = QVBoxLayout()
layout_btn_right.addWidget(answer4, alignment=Qt.AlignCenter)
layout_btn_right.addWidget(answer3, alignment=Qt.AlignCenter)

layout_btn_main.addLayout(layout_btn_left)
layout_btn_main.addLayout(layout_btn_right)

group_buttons.setLayout(layout_btn_main)

main_layout.addWidget(group_buttons, alignment=Qt.AlignCenter)

correct_answer_group = QGroupBox('Ответ')
line_answer = QVBoxLayout()
yes_or_no = QLabel('Верно/Неверно')
correct_answer = QLabel('Правильный ответ')
percent = QLabel('Процент ответов:')
line_answer.addWidget(yes_or_no, alignment=Qt.AlignLeft)
line_answer.addWidget(correct_answer, alignment=Qt.AlignCenter)
line_answer.addWidget(percent, alignment=Qt.AlignLeft)
correct_answer_group.setLayout(line_answer)
main_layout.addWidget(correct_answer_group)

button = QPushButton('Ответить')
main_layout.addWidget(button, alignment=Qt.AlignCenter)

window.setLayout(main_layout)

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)
def show_question():
    correct_answer_group.hide()
    group_buttons.show()
    button.setText('Ответить')
def show_result():
    percent.setText('<span style="color:#00FF00">\nКоличество правильных ответов:</span>' + str(window.score/window.total*100) + '%'  )               
    group_buttons.hide()
    correct_answer_group.show()
    button.setText('Следующий вопрос')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
from random import *
answers = [answer1, answer2, answer3, answer4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    question_image = QPixmap(q.image)
    question_image = question_image.scaled(300,200)
    question_image_label.setPixmap(question_image)
    correct_answer.setText(q.right_answer)
    show_question()
def next_question():
    window.count_question += 1
    window.total += 1
    if window.count_question == len(question_list):
        shuffle(question_list)
        window.count_question = 0
    ask(question_list[window.count_question])

def show_correct(res):
    yes_or_no.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        window.score += 1
        show_correct('<span style="color:#00FF00">Правильно!</span>')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('<span style="color:#FF0000">Неверно!</span>')
button.clicked.connect(start_test)

window.count_question = -1

class Question():
    def __init__ (self, question,right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.image = None
    def setImage(self, image):
        self.image = image 
q1 = Question('Что такое же большое как слон, но ничего не весит?', 'Тень', 'Воздух', 'Вата', 'Слон')
q1.setImage('Tayvan.png')
q2 = Question('Что похоже на половину яблока?', 'Вторая половина яблока', 'Груша', 'Половина груши', 'Ананас')
q3 = Question('Какая фамилия у Аллы Пугачевой?', 'Пугачева', 'Галкина', 'Миллион алых роз', 'Пупкина')
q4 = Question('Какого цвета белая лошадь?', 'Белого', 'Черного', 'Игнат', 'Рыжего')
q5 = Question('Как зовут отца Александра Сергеевича Пушкина?', 'Сергей', 'Игнат', 'Леонид', 'Марина')
question_list = [q1, q2, q3, q4, q5]

window.total = 0
window.score = 0

next_question()

def StartApp():
    window.show()
    start_window.close()
start_button.clicked.connect(StartApp)

app.exec_()
