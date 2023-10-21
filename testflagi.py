from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
app = QApplication([])

start_window = QWidget()
start_window.setWindowTitle('Тест на флаги')
start_window.setFixedSize(600, 400)

start_text = QLabel('Это тест на флаги, проверь знание географии')
start_text.setFont(QFont('Arial', 19))

start_button = QPushButton('Начать')
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
start_image = QPixmap('pig.gif')
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
    EndApp()
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
q1 = Question('Флаг какой страны ты видишь?', 'Казахстан', 'Россия', 'Украина', 'Китай')
q1.setImage('kazahstan.png')
q2 = Question('Флаг какой страны ты видишь?', 'Россия', 'Беларусь', 'Украина', 'Казахстан')
q2.setImage('russia.png')
q3 = Question('Флаг какой страны ты видишь?', 'Киргизия', 'Узбекистан', 'Армения', 'Таджикистан')
q3.setImage('kirgizia.png')
q4 = Question('Флаг какой страны ты видишь?', 'Узбекистан', 'Таджикистан', 'Армения', 'Пакистан')
q4.setImage('uzbekistan.png')
q5 = Question('Флаг какой страны ты видишь?', 'Литва', 'Латвия', 'Эстония', 'Финляндия')
q5.setImage('litva.png')
q6 = Question('Флаг какой страны ты видишь?', 'Латвия', 'Беларусь', 'Румыния', 'Финляндия')
q6.setImage('latvia.png')
q7 = Question('Флаг какой страны ты видишь?', 'Эстония', 'Норвегия', 'КНДР', 'Швеция')
q7.setImage('estonia.png')
q8 = Question('Флаг какой страны ты видишь?', 'Туркменистан', 'Литва', 'Киргизия', 'Швеция')
q8.setImage('turkmenistan.png')
q9 = Question('Флаг какой страны ты видишь?', 'Молдавия', 'Румыния', 'Сев. Македония', 'Германия')
q9.setImage('moldavya.png')
q10 = Question('Флаг какой страны ты видишь?', 'Беларусь', 'Польша', 'Казахстан', 'Норвегия')
q10.setImage('belarus.png')
q11 = Question('Флаг какой страны ты видишь?', 'Украина', 'Беларусь', 'Пакистан', 'Алжир')
q11.setImage('ukraine.png')
q12 = Question('Флаг какой страны ты видишь?', 'Азербайджан', 'Китай', 'Монголия', 'Индия')
q12.setImage('azerbaydjan.png')
q13 = Question('Флаг какой страны ты видишь?', 'Китай', 'КНДР', 'Монголия', 'Индия')
q13.setImage('kitai.png')
q14 = Question('Флаг какой страны ты видишь?', 'КНДР', 'Монголия', 'Алжир', 'Уганда')
q14.setImage('kndr.png')
q15 = Question('Флаг какой страны ты видишь?', 'США', 'Мексика', 'Аргентина', 'Индия')
q15.setImage('usa.png')
q16 = Question('Флаг какой страны ты видишь?', 'Индия', 'Бангладеш', 'Япония', 'Фиджи')
q16.setImage('india.png')
q17 = Question('Флаг какой страны ты видишь?', 'Боливия', 'Япония', 'Доминикана', 'Колумбия')
q17.setImage('bolivia.png')
q18 = Question('Флаг какой страны ты видишь?', 'Великобритания', 'Германия', 'Италия', 'Франция')
q18.setImage('britian.png')
q19 = Question('Флаг какой страны ты видишь?', 'Швеция', 'Норвегия', 'Дания', 'Финляндия')
q19.setImage('shvecia.png')
q20 = Question('Флаг какой страны ты видишь?', 'Турция', 'Алжир', 'Египет', 'Иран')
q20.setImage('turcia.png')
q21 = Question('Флаг какой страны ты видишь?', 'Тайвань', 'Китай', 'Япония', 'Южная Корея')
q21.setImage('tayvan.png')
q22 = Question('Флаг какой страны ты видишь?', 'Вьетнам', 'Китай', 'Чили', 'Индия')
q22.setImage('vietnam.png')
q23 = Question('Флаг какой страны ты видишь?', 'Дания', 'Сев. Македония', 'Сербия', 'Иордания')
q23.setImage('danya.png')
q24 = Question('Флаг какой страны ты видишь?', 'Бразилия', 'Колумбия', 'Эквадор', 'Панама')
q24.setImage('brazilia.png')
q25 = Question('Флаг какой страны ты видишь?', 'Монголия', 'Китай', 'Гана', 'Индия')
q25.setImage('mongolia.png')
q26 = Question('Флаг какой страны ты видишь?', 'Финляндия', 'Швеция', 'Шотландия', 'Украина')
q26.setImage('finlyandya.png')
q27 = Question('Флаг какой страны ты видишь?', 'Норвегия', 'Швеция', 'Румыния', 'Дания')
q27.setImage('norvegia.png')
q28 = Question('Флаг какой страны ты видишь?', 'Испания', 'Португалия', 'Панама', 'Гондурас')
q28.setImage('ispania.png')
q29 = Question('Флаг какой страны ты видишь?', 'Аргентина', 'Боливия', 'Чили', 'Уганда')
q29.setImage('argentina.png')
q30 = Question('Флаг какой страны ты видишь?', 'Италия', 'Испания', 'Тринидад и Тобаго', 'Мексика')
q30.setImage('italia.png')
question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q1, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30]
window.total = 0
window.score = 0
next_question()
end_window = QWidget()
end_window.setWindowTitle('Тест на флаги')
end_window.setFixedSize(600, 400)

end_text = QLabel('Ты прошел тест! Твой результат: ' + str(window.score)+'/30 вопросов')
end_text.setFont(QFont('Arial', 19))

end_button = QPushButton('Закончить')
end_button.setFont(QFont('Arial', 50))
end_button.setStyleSheet('''
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
end_button.setCursor(QCursor(Qt.PointingHandCursor))

end_imagepic = QLabel()
end_image = QPixmap('end_picture.png')
end_image = end_image.scaled(300, 200)
end_imagepic.setPixmap(end_image)

end_layout = QVBoxLayout()
end_layout.addWidget(end_text, alignment=Qt.AlignCenter)
end_layout.addWidget(end_imagepic, alignment=Qt.AlignCenter)
end_layout.addWidget(end_button, alignment=Qt.AlignCenter)

end_window.setLayout(end_layout)

def StartApp():
    window.show()
    start_window.close()
start_button.clicked.connect(StartApp)
def EndApp():
    end_text.setText('Ты прошел тест! Твой результат: ' + str(window.score)+'/30 вопросов')
    if window.total == 30:
        window.close()
        end_window.show()
def CloseApp():
    end_window.close()
end_button.clicked.connect(CloseApp)

app.exec_()

