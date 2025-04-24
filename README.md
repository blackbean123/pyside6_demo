# PySide6 示例项目

这是一个使用 PySide6 构建的示例项目，包含各种组件的示例和典型的界面示例。

## 项目结构

- `main.py`: 主程序入口
- `components/`: 包含各种组件的示例
  - `button_example.py`: 按钮示例
  - `label_example.py`: 标签示例
  - `line_edit_example.py`: 输入框示例
- `ui_examples/`: 包含典型的界面示例
  - `login_ui.py`: 登录界面示例
  - `settings_ui.py`: 设置界面示例
- `requirements.txt`: 项目依赖文件
- `setup.py`: 打包脚本

## 安装依赖

## 打包exe
### 使用 PyInstaller 打包
在项目根目录下运行以下命令来打包你的应用程序
```commandline
pyinstaller --onefile --windowed --icon=app_icon.ico main.py
```
- --onefile：将所有文件打包成一个单独的可执行文件。
- --windowed：创建一个无控制台窗口的应用程序。
- --icon=app_icon.ico：指定应用程序的图标。

#### 注意事项
- 确保 app_icon.ico 文件存在于项目根目录下，或者根据实际路径调整 --icon 参数。
- 如果你的项目中有其他资源文件（如图片、配置文件等），需要在 setup.py 中的 include_files 列表中添加这些文件的路径

#### 可选：优化打包大小
如果你发现生成的可执行文件过大，可以尝试以下方法：
- 使用 --noconsole 参数来隐藏控制台窗口。
- 使用 --upx-dir 参数指定 UPX 压缩工具的路径，以减小文件大小。
```commandline
pyinstaller --onefile --windowed --icon=app_icon.ico --noconsole --upx-dir=path_to_upx main.py
```