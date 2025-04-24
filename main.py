import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QGroupBox
from PySide6.QtGui import QFont, QIcon, QPalette, QColor  # 导入 QIcon 类

from components.button_example import ButtonExample
from components.label_example import LabelExample
from components.line_edit_example import LineEditExample
from components.table_example import TableExample
from components.icon_example import IconExample  # 导入新增的 IconExample 组件
from components.file_selection_example import FileSelectionExample
from components.time_selection_example import TimeSelectionExample
from components.switch_example import SwitchExample
from components.number_input_example import NumberInputExample
from components.checkbox_example import CheckboxExample
from ui_examples.user_form_ui import UserFormUI  # 新增导入


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit_example_window = None
        self.label_example_window = None
        self.button_example_window = None
        self.setWindowTitle("PySide6 示例项目")
        self.setGeometry(400, 200, 1000, 600)

        # 设置应用程序图标
        self.setWindowIcon(QIcon("app_icon.ico"))  # 确保 icon.png 文件存在

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建 QTabWidget
        tab_widget = QTabWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(tab_widget)

        # 添加仿 form 示例标签页
        form_example_tab = QWidget()
        tab_widget.addTab(form_example_tab, "综合示例")
        form_example_layout = QVBoxLayout(form_example_tab)

        # 集成各组件到仿 form 示例页面
        components = [
            ("按钮示例", ButtonExample()),
            ("标签示例", LabelExample()),
            ("输入框示例", LineEditExample()),
            ("文件选择示例", FileSelectionExample()),
            ("时间选择示例", TimeSelectionExample()),
            ("Switch开关示例", SwitchExample()),
            ("数字输入框示例", NumberInputExample()),
            ("Checkbox多选框示例", CheckboxExample())
        ]

        for label, widget in components:
            group = QGroupBox(label)
            group_layout = QVBoxLayout()
            group.setLayout(group_layout)
            group_layout.addWidget(widget)
            form_example_layout.addWidget(group)

        # 添加图标示例标签页
        icon_example_tab = QWidget()
        tab_widget.addTab(icon_example_tab, "图标示例")
        icon_example_layout = QVBoxLayout(icon_example_tab)
        icon_example_widget = IconExample()
        icon_example_layout.addWidget(icon_example_widget)

        # 添加表格示例标签页
        table_example_tab = QWidget()
        tab_widget.addTab(table_example_tab, "表格示例")
        table_example_layout = QVBoxLayout(table_example_tab)
        table_example_widget = TableExample()
        table_example_layout.addWidget(table_example_widget)

        # 新增用户信息表单标签页
        user_form_tab = QWidget()
        tab_widget.addTab(user_form_tab, "用户信息表单")
        user_form_layout = QVBoxLayout(user_form_tab)
        user_form_widget = UserFormUI()
        user_form_layout.addWidget(user_form_widget)

    def show_button_example(self):
        from components.button_example import ButtonExample
        self.button_example_window = ButtonExample()
        self.button_example_window.show()

    def show_label_example(self):
        from components.label_example import LabelExample
        self.label_example_window = LabelExample()
        self.label_example_window.show()

    def show_line_edit_example(self):
        from components.line_edit_example import LineEditExample
        self.line_edit_example_window = LineEditExample()
        self.line_edit_example_window.show()

    def show_table_example(self):
        from components.table_example import TableExample
        self.table_example_window = TableExample()
        self.table_example_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("app_icon.ico"))  # 设置全局应用程序图标
    # Windows系统可能需要额外设置（通过ctypes）
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("heidou.app.1.0.0")
    # 使用现代风格
    # app.setStyle("WindowsVista")
    # 跨平台现代风格
    app.setStyle("Fusion")

    # 配置调色板（Fusion风格时需要）
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
    palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
