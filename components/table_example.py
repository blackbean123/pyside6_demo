from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class TableExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("表格示例")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置字体
        font = QFont("Segoe UI", 10)

        self.table = QTableWidget()
        self.table.setFont(font)
        self.table.setColumnCount(3)
        self.table.setRowCount(5)
        self.table.setHorizontalHeaderLabels(["姓名", "年龄", "城市"])

        # 美化表格样式
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            QHeaderView::section {
                background-color: #e0e0e0;
                color: #333;
                font-weight: bold;
                padding: 10px;
                border: 1px solid #ccc;
                border-right: 2px solid #ccc;
            }
            QHeaderView::section:last {
                border-right: none;
            }
            QTableWidget QTableCornerButton::section {
                border: none;
            }
            QTableWidget QTableCornerButton::section:horizontal {
                border: none;
            }
            QTableWidget QTableCornerButton::section:vertical {
                border: none;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            QTableWidget::item:selected {
                background-color: #e0e0e0;
                color: #333;  /* 修改选中状态下的字体颜色为深灰色 */
            }
            QTableWidget::item:alternate {
                background-color: #f1f8e9;
            }
        """)

        # 添加数据
        data = [
            ["张三", "25", "北京"],
            ["李四", "30", "上海"],
            ["王五", "22", "广州"],
            ["赵六", "28", "深圳"],
            ["孙七", "35", "杭州"]
        ]

        for row, row_data in enumerate(data):
            for col, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                self.table.setItem(row, col, item)

        layout.addWidget(self.table)