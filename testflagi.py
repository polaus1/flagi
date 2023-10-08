from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setFont(QFont('Calibri', 20))
main_layout = QVBoxLayout()
question = QLabel('Флаг какой страны на картинке?')
main_layout.addWidget(question, alignment=Qt.AlignCenter)

group_buttons = QGroupBox('Варианты ответа')

answer1 = QRadioButton('США')
answer2 = QRadioButton('Испания')
answer3 = QRadioButton('Франция')
answer4 = QRadioButton('Россия')
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
button = QPushButton('Ответить')
main_layout.addWidget(button, alignment=Qt.AlignCenter)

window.setLayout(main_layout)

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)
window.show()
app.exec_()                                                                                                                                                                                      
