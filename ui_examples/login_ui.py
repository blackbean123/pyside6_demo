from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录界面示例")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        self.username_label = QLabel("用户名:")
        self.username_label.setFont(font)
        layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #ccc; border-radius: 5px; padding: 10px; }")
        layout.addWidget(self.username_input)

        self.password_label = QLabel("密码:")
        self.password_label.setFont(font)
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("QLineEdit { background-color: white; border: 1px solid #ccc; border-radius: 5px; padding: 10px; }")
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("登录")
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton { background-color: #2196F3; color: white; border-radius: 5px; padding: 10px; } QPushButton:hover { background-color: #0b7dda; }")
        self.login_button.clicked.connect(self.on_login_clicked)
        layout.addWidget(self.login_button)

    def on_login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(f"用户名: {username}, 密码: {password}")
