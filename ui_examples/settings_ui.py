from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class SettingsUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置界面示例")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        self.theme_label = QLabel("主题:")
        self.theme_label.setFont(font)
        layout.addWidget(self.theme_label)

        self.theme_input = QLineEdit()
        self.theme_input.setFont(font)
        self.theme_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #ccc; border-radius: 5px; padding: 10px; }")
        layout.addWidget(self.theme_input)

        self.language_label = QLabel("语言:")
        self.language_label.setFont(font)
        layout.addWidget(self.language_label)

        self.language_input = QLineEdit()
        self.language_input.setFont(font)
        self.language_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #ccc; border-radius: 5px; padding: 10px; }")
        layout.addWidget(self.language_input)

        self.save_button = QPushButton("保存设置")
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: #45a049; }")
        self.save_button.clicked.connect(self.on_save_clicked)
        layout.addWidget(self.save_button)

    def on_save_clicked(self):
        theme = self.theme_input.text()
        language = self.language_input.text()
        print(f"主题: {theme}, 语言: {language}")