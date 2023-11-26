import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_row1 = QHBoxLayout()
        layout_row2 = QHBoxLayout()
        layout_number = QGridLayout()
        layout_display = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        
        self.equation = QLineEdit("")
        self.expression = ""


        ### layout_display 레이아웃에 수식, 답 위젯을 추가
        layout_display.addRow(self.equation)

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 추가 버튼 생성
        button_moduler = QPushButton("%")
        button_reciprocal = QPushButton("1/x")
        button_power = QPushButton("x²")
        button_sqrt = QPushButton("√x")
        button_clearEntry = QPushButton("CE")
        button_signChange = QPushButton("+/-")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### 추가 버튼 클릭시 시그널 생성
        button_signChange.clicked.connect(self.button_signChange_clicked)
        button_clearEntry.clicked.connect(self.button_clearEntry_clicked)
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)

        ### layout_row1 레이아웃에 버튼 추가

        layout_row1.addWidget(button_clearEntry)
        layout_row1.addWidget(button_clear)
        layout_row1.addWidget(button_backspace)
        

        ### layout_row2 레이아웃에 버튼 추가
        layout_row2.addWidget(button_reciprocal)
        layout_row2.addWidget(button_division)

        ### layout_number 레이아웃에 버튼 추가
        layout_number.addWidget(button_product,0,3)
        layout_number.addWidget(button_minus,1,3)
        layout_number.addWidget(button_plus,2,3)
        layout_number.addWidget(button_equal,3,3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], 2-x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        ### +/- 버튼 시그널 생성
        layout_number.addWidget(button_signChange, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_display)
        main_layout.addLayout(layout_row1)
        main_layout.addLayout(layout_row2)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)
        self.expression += str(num)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText("")
        self.expression = equation

    def button_equal_clicked(self):
        equation = self.expression
        solution = eval(equation)
        self.equation.setText(str(solution))
        self.expression = str(solution)

    def button_clear_clicked(self):
        self.equation.setText("")
        self.expression = ""

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

    def button_signChange_clicked(self):
        equation = self.equation.text()
        self.expression = self.expression[:-len(equation)]
        equation = '-' + equation
        self.expression += equation
        self.equation.setText(equation)
    
    def button_clearEntry_clicked(self):
        equation = self.equation.text()
        self.expression = self.expression[:-len(equation)]
        self.equation.setText("")

    def button_reciprocal_clicked(self):
        equation = self.equation.text()
        self.expression = self.expression[:-len(equation)]
        equation = 1 / float(equation)
        self.expression += str(equation)
        self.equation.setText(str(equation))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())