import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, \
    QGridLayout, QTabWidget
from PySide6.QtGui import QFont, QIcon  # 导入 QIcon 类

from components.button_example import ButtonExample
from components.label_example import LabelExample
from components.line_edit_example import LineEditExample
from ui_examples.login_ui import LoginUI
from ui_examples.settings_ui import SettingsUI


# 获取图标绝对路径（确保图标文件存在）
def resource_path(relative_path):
    """ 获取资源的绝对路径（兼容打包后的情况）"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit_example_window = None
        self.label_example_window = None
        self.button_example_window = None
        self.setWindowTitle("PySide6 示例项目")
        self.setGeometry(100, 100, 400, 300)

        # 设置应用程序图标
        self.setWindowIcon(QIcon("app_icon.ico"))  # 确保 icon.png 文件存在

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建 QTabWidget
        tab_widget = QTabWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(tab_widget)

        # 添加按钮示例标签页
        button_example_tab = QWidget()
        tab_widget.addTab(button_example_tab, "按钮示例")
        button_example_layout = QVBoxLayout(button_example_tab)
        button_example_widget = ButtonExample()
        button_example_layout.addWidget(button_example_widget)

        # 添加标签示例标签页
        label_example_tab = QWidget()
        tab_widget.addTab(label_example_tab, "标签示例")
        label_example_layout = QVBoxLayout(label_example_tab)
        label_example_widget = LabelExample()
        label_example_layout.addWidget(label_example_widget)

        # 添加输入框示例标签页
        line_edit_example_tab = QWidget()
        tab_widget.addTab(line_edit_example_tab, "输入框示例")
        line_edit_example_layout = QVBoxLayout(line_edit_example_tab)
        line_edit_example_widget = LineEditExample()
        line_edit_example_layout.addWidget(line_edit_example_widget)

        # 添加登录界面示例标签页
        login_ui_tab = QWidget()
        tab_widget.addTab(login_ui_tab, "登录界面示例")
        login_ui_layout = QVBoxLayout(login_ui_tab)
        login_ui_widget = LoginUI()
        login_ui_layout.addWidget(login_ui_widget)

        # 添加设置界面示例标签页
        settings_ui_tab = QWidget()
        tab_widget.addTab(settings_ui_tab, "设置界面示例")
        settings_ui_layout = QVBoxLayout(settings_ui_tab)
        settings_ui_widget = SettingsUI()
        settings_ui_layout.addWidget(settings_ui_widget)

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

    def show_login_ui(self):
        from ui_examples.login_ui import LoginUI
        self.login_ui_window = LoginUI()
        self.login_ui_window.show()

    def show_settings_ui(self):
        from ui_examples.settings_ui import SettingsUI
        self.settings_ui_window = SettingsUI()
        self.settings_ui_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("app_icon.ico"))  # 设置全局应用程序图标
    # Windows系统可能需要额外设置（通过ctypes）
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("heidou.app.1.0.0")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
