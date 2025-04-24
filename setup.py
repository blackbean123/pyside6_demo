from setuptools import setup, find_packages

setup(
    name="qt_demo",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PySide6==6.5.1"
    ],
    entry_points={
        'console_scripts': [
            'qt_demo = main:main',
        ],
    },
    include_package_data=True,
    options={
        'build_exe': {
            'include_files': ['app_icon.ico'],  # 包含图标文件
        }
    }
)