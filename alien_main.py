import os.path

from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QMenu, QApplication, QSystemTrayIcon
import sys
import random

IMG_ROOT = './resource/image'


class Hero(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        # 进行窗口的相关初始化设置，置顶、无边框等
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # 不自动填充背景色，背景透明
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.repaint()
       # 加载图片资源
        icon, self.pixmaps = self.load_resource()
        # 在任务栏显示，添加退出菜单：任务栏层级为 tray_icon -> tray_menu -> action
        quit_action = QAction('退出', self, triggered=self.quit)
        quit_action.setIcon(icon)
        self.tray_menu = QMenu(self)
        self.tray_menu.addAction(quit_action)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        # 设置窗体内容（显示图片）
        self.hero = QLabel(self)
        self.hero.setPixmap(self.pixmaps[0])
        self.resize(1024, 1024)
        self.random_pos()
        self.show()
        # 设置定时切换图片效果
        self.action_pointer = 0
        self.action_len = len(self.pixmaps)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.action)
        self.timer.start(500)

    def quit(self):
        self.close()
        sys.exit()

    def load_resource(self):
        # 任务栏、菜单的图标
        icon = QIcon(os.path.join(IMG_ROOT, self.name, f"{self.name}1.png"))
        # 用于循环播放的图片
        pixmaps = [QPixmap(os.path.join(IMG_ROOT, self.name, f"{self.name}{i}.png")) for i in range(1, 4)]
        return icon, pixmaps

    def random_pos(self):
        screen_geo = QApplication.primaryScreen().geometry()
        hero_geo = self.geometry()
        x = (screen_geo.width() - hero_geo.width()) * random.random()
        y = (screen_geo.height() - hero_geo.height()) * random.random()
        self.move(x, y)

    def action(self):
        self.hero.setPixmap(self.pixmaps[self.action_pointer])
        self.action_pointer += 1
        if self.action_pointer >= self.action_len:
            self.action_pointer = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hero = Hero(random.choice(['xiaoying', 'L']))
    hero.show()
    sys.exit(app.exec())
