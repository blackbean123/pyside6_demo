from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PySide6.QtGui import QFont

class FileSelectionExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件选择示例")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Segoe UI", 10)

        self.label = QLabel("未选择文件")
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.button = QPushButton("选择文件")
        self.button.setFont(font)
        self.button.clicked.connect(self.select_file)
        layout.addWidget(self.button)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            self.label.setText(f"选择的文件: {file_path}")