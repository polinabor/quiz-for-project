from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import randint, shuffle 


class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = [] 
questions_list.append(
        Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(
        Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(
        Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(
        Question('Какой сок собирается весной', 'Березовый', 'Томатный', 'Цветочный', 'Сосновый'))
questions_list.append(
        Question('Что согласно пословице весенний день кормит', 'Год', 'Человека', 'Месяц', 'Животных'))
questions_list.append(
        Question('Когда на Земле наступает астрономическая весна', '21 марта', '22 марта', '20 апреля', '19 мая'))
questions_list.append(
        Question('Какая часть растений первой отзывается на потепление весной', 'Корни', 'Листья', 'Ветви', 'Сердцевинка'))
questions_list.append(
        Question('Какой весенний месяц в старину назывался травник', 'Май', 'Март', 'Апрель', 'Июнь'))
questions_list.append(
        Question('Самый жаркий материк', 'Африка', 'Азия', 'Австралия', 'Евразия'))
questions_list.append(
        Question('В какой стране находится Тадж-Махал', 'Индия', 'Индонезия', 'Бали', 'Вьетнам'))
questions_list.append(
        Question('Прибор для определения влажности воздуха', 'Гигрометр', 'Термометр', 'Амперметр', 'Ацетометр'))
questions_list.append(
        Question('Прибор для измерения глубин', 'Эхолот', 'Эхохетор', 'Омметр', 'Рефлектометр'))
questions_list.append(
        Question('Какая рыба самая большая в мире', 'Китовая акула', 'Белуга', 'Белая акула', 'Мола'))
questions_list.append(
        Question('Какая рыба самая быстрая в мире', 'Меч-рыба', 'Рыба-парусник', 'Ваху', 'Барракуда'))
questions_list.append(
        Question('Какая охота всегда разрешена в лесу', 'Фотоохота', 'Обычная охота', 'Научная охота', 'Никакая'))
questions_list.append(
        Question('Какое дерево королева тайги', 'Лиственница', 'Пихта', 'Кедровая сосна', 'Сосна'))
questions_list.append(
        Question('Какую рыбу поймал Емеля', 'Щуку', 'Золотую рыбку', 'Карася', 'Форель'))
questions_list.append(
        Question('Какого цвета были волосы у Мальвины', 'Сине-голубой', 'Лазурный', 'Бирюзовый', 'Голубой'))
questions_list.append(
        Question('Самый большой остров в России', 'Сахалин', 'Врангеля', 'Северный', 'Ольхон'))
questions_list.append(
        Question('Самый большой океан', 'Тихий', 'Атлантический', 'Индийский', 'Южный'))


app = QApplication([])


btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() # показываем панель вопросов 


def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')
    


def next_question():
    ''' задает следующий вопрос из списка '''
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)

    if window.current_question < len(questions_list):
        q = questions_list[window.current_question]  # берем вопрос по текущему индексу
        ask(q)  # спросили
        window.current_question += 1  # увеличиваем индекс для следующего вопроса
    else:
        # Больше нет вопросов
        lb_Question.setText("Все вопросы пройдены!")
        RadioGroupBox.hide()
        btn_OK.hide() # Скрываем кнопку "Ответить"
        AnsGroupBox.show()
        lb_Correct.setText("Ваш итоговый рейтинг: " + str((window.score/window.total*100)) + "%") # Выводим итоговый рейтинг



def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('QUIZ')


btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит


window.score = 0
window.total = 0
window.current_question = 0 # Добавляем переменную для отслеживания текущего вопроса
next_question()
window.resize(400, 300)
window.show()
app.exec()
