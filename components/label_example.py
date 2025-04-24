from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class LabelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("标签示例")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        self.label = QLabel("这是一个标签")
        self.label.setFont(font)
        layout.addWidget(self.label)
