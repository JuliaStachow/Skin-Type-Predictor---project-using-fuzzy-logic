import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from SkinTypeSys import FuzzyModel


class FuzzyLogicApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.acneFrequency_label = QLabel(self)
        self.externalFactorsResistance_label = QLabel(self)
        self.acneFrequency_edit = QLineEdit(self)
        self.externalFactorsResistance_edit = QLineEdit(self)
        self.result_label = QLabel(self)
        self.calculate_button = QPushButton('Calculate', self)
        self.legend = QLabel(self)

        self.acneFrequency_label.setText('How often does acne appear on your skin per month?\n(enter number from 0 to 30)')
        self.externalFactorsResistance_label.setText('How resistant your skin is to external factors?\n(enter number from 0 to 100)')
        self.legend.setText('Result Legend:\n0 - dry skin\n5 - mixed skin\n10 - oily skin')

        layout = QVBoxLayout(self)
        layout.addWidget(self.acneFrequency_label)
        layout.addWidget(self.acneFrequency_edit)
        layout.addWidget(self.externalFactorsResistance_label)
        layout.addWidget(self.externalFactorsResistance_edit)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.legend)

        self.calculate_button.clicked.connect(self.calculate_fuzzy_logic)

        self.setWindowTitle('Skin Type Predictor')
        self.setGeometry(100, 100, 300, 200)

    def calculate_fuzzy_logic(self):
        input1 = float(self.acneFrequency_edit.text())
        input2 = float(self.externalFactorsResistance_edit.text())

        output = FuzzyModel()
        result = output.perform_fuzzy_logic(input1, input2)

        self.result_label.setText(f'Result: {result}')

        output.view_plots()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = FuzzyLogicApp()
    main_window.show()
    sys.exit(app.exec_())

