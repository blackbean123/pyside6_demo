from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class LineEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("输入框示例")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        self.line_edit = QLineEdit()
        self.line_edit.setFont(font)
        self.line_edit.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #ccc; border-radius: 5px; padding: 10px; }")
        layout.addWidget(self.line_edit)

        self.label = QLabel("输入内容将显示在这里")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.line_edit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        self.label.setText(f"输入的内容是: {text}")
