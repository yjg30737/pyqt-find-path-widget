from setuptools import setup, find_packages

setup(
    name='pyqt-find-path-widget',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_find_path_widget.style': ['button.css', 'lineedit.css']},
    description='PyQt find path widget (QLabel - QLineEdit - QPushButton)',
    url='https://github.com/yjg30737/pyqt-find-path-widget.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)