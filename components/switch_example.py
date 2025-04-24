from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLabel
from PySide6.QtGui import QFont

class SwitchExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Switch开关示例")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Segoe UI", 10)

        self.label = QLabel("开关状态: 关")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.switch = QCheckBox("启用功能")
        self.switch.setFont(font)
        self.switch.stateChanged.connect(self.update_switch_state)
        layout.addWidget(self.switch)

    def update_switch_state(self, state):
        self.label.setText(f"开关状态: {'开' if state else '关'}")