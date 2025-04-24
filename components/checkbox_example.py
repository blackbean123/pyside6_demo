from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLabel
from PySide6.QtGui import QFont

class CheckboxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox多选框示例")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Segoe UI", 10)

        self.label = QLabel("选择的选项: ")
        self.label.setFont(font)
        layout.addWidget(self.label)

        options = ["选项1", "选项2", "选项3"]
        self.checkboxes = []
        for option in options:
            checkbox = QCheckBox(option)
            checkbox.setFont(font)
            checkbox.stateChanged.connect(self.update_checkbox_label)
            layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

    def update_checkbox_label(self):
        selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        self.label.setText(f"选择的选项: {', '.join(selected) if selected else '无'}")