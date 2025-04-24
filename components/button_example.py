from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class ButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("按钮示例")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        self.button = QPushButton("点击我")
        self.button.setFont(font)
        self.button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: #45a049; }")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        self.label = QLabel("未点击")
        self.label.setFont(font)
        layout.addWidget(self.label)

    def on_button_clicked(self):
        self.label.setText("按钮被点击了！")
