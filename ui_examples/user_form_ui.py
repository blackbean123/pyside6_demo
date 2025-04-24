from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, \
    QMessageBox, QGridLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QDate
from PySide6.QtGui import QFont, Qt


class UserFormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("用户信息表单")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        # 创建表单布局（改为两列）
        form_layout = QGridLayout()
        layout.addLayout(form_layout)

        # 设置列宽比例，左边列比右边列窄
        form_layout.setColumnStretch(0, 1)  # 左边列
        form_layout.setColumnStretch(1, 2)  # 右边列

        # 调整行间距和列间距以使界面更加紧凑
        form_layout.setSpacing(3)  # 减少控件之间的垂直间距
        form_layout.setHorizontalSpacing(5)  # 减少标签和控件之间的水平间距
        form_layout.setContentsMargins(5, 5, 5, 5)  # 减少整体布局的外边距

        # 用户名
        form_layout.addWidget(QLabel("用户名:    "), 0, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.username_input = QLineEdit()
        self.username_input.setFont(font)
        self.username_input.setFixedWidth(200)  # 限制输入框宽度
        form_layout.addWidget(self.username_input, 0, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        # 密码
        form_layout.addWidget(QLabel("密码:    "), 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFont(font)
        self.password_input.setFixedWidth(200)  # 限制输入框宽度
        form_layout.addWidget(self.password_input, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        # 性别
        form_layout.addWidget(QLabel("性别:    "), 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["男", "女", "其他"])
        self.gender_combo.setFont(font)
        self.gender_combo.setFixedWidth(200)  # 限制下拉框宽度
        form_layout.addWidget(self.gender_combo, 2, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        # 生日
        form_layout.addWidget(QLabel("生日:    "), 3, 0, alignment=Qt.AlignmentFlag.AlignRight)
        self.birthday_picker = QDateEdit()
        self.birthday_picker.setDate(QDate.currentDate())
        self.birthday_picker.setFont(font)
        self.birthday_picker.setFixedWidth(200)  # 限制日期选择器宽度
        form_layout.addWidget(self.birthday_picker, 3, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        # 提交按钮
        submit_button = QPushButton("提交")
        submit_button.setFont(font)
        submit_button.setFixedWidth(100)  # 限制按钮宽度
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        submit_button.clicked.connect(self.submit_form)

        # 调整底部外边距使按钮更贴近控件
        form_layout.setContentsMargins(5, 5, 5, 1)  # 删除: form_layout.setContentsMargins(5, 5, 5, 5)

        # 将提交按钮水平居中且垂直居上
        form_layout.addWidget(
            submit_button, 
            4, 0, 1, 2, 
            alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

    def submit_form(self):
        # 获取表单数据并进行简单验证
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        gender = self.gender_combo.currentText()
        birthday = self.birthday_picker.date().toString("yyyy-MM-dd")

        if not username or not password:
            QMessageBox.warning(self, "表单错误", "用户名和密码不能为空！")
            return

        # 显示提交成功消息
        QMessageBox.information(
            self,
            "提交成功",
            f"表单已提交！\n用户名: {username}\n性别: {gender}\n生日: {birthday}"
        )



