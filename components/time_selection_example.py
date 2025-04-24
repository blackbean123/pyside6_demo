from PySide6.QtWidgets import QWidget, QVBoxLayout, QDateTimeEdit, QLabel
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QFont

class TimeSelectionExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("时间选择示例")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Segoe UI", 10)

        self.label = QLabel("当前时间: ")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.time_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.time_edit.setFont(font)
        self.time_edit.setCalendarPopup(True)
        self.time_edit.dateTimeChanged.connect(self.update_time_label)
        layout.addWidget(self.time_edit)

    def update_time_label(self, date_time):
        self.label.setText(f"选择的时间: {date_time.toString('yyyy-MM-dd HH:mm:ss')}")