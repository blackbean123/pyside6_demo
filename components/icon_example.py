from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QGridLayout,
                               QPushButton, QGroupBox, QLabel, QStyle)
from PySide6.QtGui import QIcon, QFont


class IconExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("内置图标示例（修正版）")
        self.setGeometry(100, 100, 800, 600)

        # 图标映射更新（部分图标更改为更现代的映射）
        self.ICON_MAPPING = {
            "add": QStyle.StandardPixmap.SP_FileIcon,  # 更直观的图标
            "delete": QStyle.StandardPixmap.SP_TrashIcon,
            "edit": QStyle.StandardPixmap.SP_FileDialogDetailedView,
            "save": QStyle.StandardPixmap.SP_DialogSaveButton,
            "open": QStyle.StandardPixmap.SP_DirOpenIcon,
            "close": QStyle.StandardPixmap.SP_DialogCloseButton,
            "back": QStyle.StandardPixmap.SP_ArrowBack,
            "forward": QStyle.StandardPixmap.SP_ArrowForward,
            "refresh": QStyle.StandardPixmap.SP_BrowserReload,
            "search": QStyle.StandardPixmap.SP_FileDialogStart,
            "help": QStyle.StandardPixmap.SP_TitleBarContextHelpButton,
            "information": QStyle.StandardPixmap.SP_MessageBoxInformation,
            "warning": QStyle.StandardPixmap.SP_MessageBoxWarning,
            "error": QStyle.StandardPixmap.SP_MessageBoxCritical
        }

        layout = QVBoxLayout()
        self.setLayout(layout)

        font = QFont("Segoe UI", 10)

        # 创建分组框（保持原结构）
        file_group = self._get_group_layout("文件操作")
        navigation_group = self._get_group_layout("导航")
        status_group = self._get_group_layout("状态")

        # 图标分类定义（保持原结构）
        icons = {
            "文件操作": [
                ("新建", "add"),
                ("删除", "delete"),
                ("编辑", "edit"),
                ("保存", "save"),
                ("打开", "open"),
                ("关闭", "close")
            ],
            "导航": [
                ("上一页", "back"),
                ("下一页", "forward"),
                ("刷新", "refresh"),
                ("搜索", "search")
            ],
            "状态": [
                ("帮助", "help"),
                ("信息", "information"),
                ("警告", "warning"),
                ("错误", "error")
            ]
        }

        # 修改后的按钮生成逻辑
        for group_name, icon_list in icons.items():
            group = self._get_group_layout(group_name)
            group_layout = group.layout()  # 获取分组的布局

            row, col = 0, 0
            for label, icon_name in icon_list:
                button = self._create_icon_button(label, icon_name, font)
                group_layout.addWidget(button, row, col)
                col = (col + 1) % 4  # 每行4列自动换行
                row += 1 if col == 0 else 0

            layout.addWidget(group)  # 将分组添加到主布局

    def _get_group_layout(self, group_name):
        """返回对应分组的布局"""
        group = QGroupBox(group_name)
        layout = QGridLayout()
        group.setLayout(layout)  # 确保布局与分组关联
        return group  # 返回 QGroupBox 而不是 QGridLayout

    def _create_icon_button(self, label, icon_name, font):
        button = QPushButton(label)
        button.setFont(font)

        # 添加现代按钮样式
        button.setStyleSheet("""
            QPushButton {
                padding: 8px;
                border: 1px solid #D0D0D0;
                border-radius: 4px;
                background-color: #F8F8F8;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
        """)

        # 图标设置（增加尺寸）
        icon = self.style().standardIcon(
            self.ICON_MAPPING.get(icon_name, QStyle.StandardPixmap.SP_MessageBoxQuestion)
        )
        button.setIcon(icon)
        button.setIconSize(button.sizeHint().scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))  # 固定图标尺寸

        return button
