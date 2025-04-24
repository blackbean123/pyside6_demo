from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QLabel
from PySide6.QtGui import QFont

class NumberInputExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("数字输入框示例")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Segoe UI", 10)

        self.label = QLabel("输入的数字: 0")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.spin_box = QSpinBox()
        self.spin_box.setFont(font)
        self.spin_box.setMinimum(0)
        self.spin_box.setMaximum(100)
        self.spin_box.valueChanged.connect(self.update_number_label)
        layout.addWidget(self.spin_box)

    def update_number_label(self, value):
        self.label.setText(f"输入的数字: {value}")