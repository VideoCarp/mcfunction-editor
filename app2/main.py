from sys import argv, exit
import highlighting, commands
from os.path import realpath
from os import getcwd
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGridLayout,
    QPushButton,
    QPlainTextEdit,
    QFileDialog,
    QLineEdit,
)

Pybox = False
##### Set this to 'True' if you want a box in which you can execute some Python.
##### You can use libraries with this too if you have them installed.
##### a bind (Ctrl+P) is also available. you can turn off PythonBox with ctrl+shift+p
saveLocation = None


class ScopeAvoid:
    current = "dark"
    normalSavePath = None


def Prompt(option):
    if option == "open":
        f, _FILTER = QFileDialog.getOpenFileName()
        try:
            with open(realpath(f)) as file:
                mainTextBox.setPlainText(file.read())
        except:
            print("Logging: Failed to get path for file.")
    else:
        if ScopeAvoid.normalSavePath is None:
            try:
                f, _FILTER = QFileDialog.getSaveFileName()
                try:
                    open(realpath(f))
                except:
                    ScopeAvoid.normalSavePath = None
                    return
                ScopeAvoid.normalSavePath = f
                with open(realpath(f)) as file:
                    file.write(mainTextBox.toPlainText())
            except:
                print(
                    "May have failed to save, try checking if file was updated, or press 'Ctrl+S' again."
                )

        if ScopeAvoid.normalSavePath is not None:
            try:
                with open(realpath(ScopeAvoid.normalSavePath), "w+") as file:
                    file.write(mainTextBox.toPlainText())
            except:
                print("Logging: Failed to get file path.")


def SwapTheme():
    if ScopeAvoid.current == "dark":
        with open(realpath("styles/light.qss"), "r") as f:
            window.setStyleSheet(f.read())
        ScopeAvoid.current = "light"
    else:
        with open(realpath("styles/dark.qss")) as f:
            window.setStyleSheet(f.read())
        ScopeAvoid.current = "dark"


def countlines():
    if mainTextBox.textChanged:
        lines = mainTextBox.toPlainText()
        lineLen = len(lines.split("\n"))
        lineCounter.setText(f"<h1>Lines: {lineLen}</h1>")


class TxtCustom(QPlainTextEdit):
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        options = {"[": "]", '"': '"', "{": "}", "(": ")"}
        option = options.get(event.text())
        if option is not None:
            tc = self.textCursor()
            p = tc.position()
            self.insertPlainText(option)
            tc.setPosition(p)
            self.setTextCursor(tc)


def PythonBox(arg=None):
    if arg != None:
        try:
            lay.removeWidget(pythonBox)
            lay.removeWidget(executeBox)
            return
        except:
            return
    pythonBox = QPlainTextEdit(
        "Type in Python here. Libs, if installed correctly will work too.",
        parent=window,
    )
    lay.addWidget(pythonBox, 1, 1)
    pythonBox.setFixedSize(screen_x / 4, screen_y / 4)
    executeBox = QPushButton("Run Python")

    def runpy():
        try:
            exec(pythonBox.toPlainText())
        except:
            print("PythonBox errored.")

    executeBox.clicked.connect(runpy)
    lay.addWidget(executeBox, 2, 1)


app = QApplication(argv)
window = QWidget()

with open(realpath("styles/dark.qss")) as sheet:
    window.setStyleSheet(sheet.read())

window.setWindowTitle("MCFunction Editor")
screen_x, screen_y = 1200, 750
window.setGeometry(0, 0, screen_x, screen_y)
window.move(960, 540)


lay = QGridLayout()
# lay.addWidget(widget, row, column)
saveButton = QPushButton("Save...", parent=window)
openButton = QPushButton("Open...", parent=window)
themeButton = QPushButton("Swap Theme", parent=window)

commandInterface = QLineEdit("tutorial", parent=window)
runCommand = QPushButton("Click to register command.", parent=window)
runCommand.clicked.connect(lambda: commands.Execute(commandInterface.text()))
mainTextBox = TxtCustom("Start typing...", parent=window)
mainTextBox.setFixedSize(screen_x, int(screen_y / 1.5))
highlight = highlighting.MCFunction(mainTextBox.document())
execBox = QPushButton("push")
lineCounter = QLabel("<h2>Lines: 0</h2>", parent=window)
lineCounter.setStyleSheet(
    """
lineCounter {
    text-align: center;
}"""
)

# connections
saveButton.clicked.connect(lambda: Prompt("save"))
openButton.clicked.connect(lambda: Prompt("open"))
themeButton.clicked.connect(SwapTheme)
mainTextBox.textChanged.connect(countlines)

# Adding to layout
lay.addWidget(saveButton, 0, 0)
lay.addWidget(openButton, 0, 1)
lay.addWidget(themeButton, 0, 2)
lay.addWidget(mainTextBox, 1, 0)
lay.addWidget(lineCounter, 1, 1)
lay.addWidget(commandInterface, 2, 0)
lay.addWidget(runCommand, 3, 0)

# Shortcut:
shortcutSave = QShortcut(QKeySequence("Ctrl+S"), window)
shortcutSave.activated.connect(lambda: Prompt("save"))

shortcutOpen = QShortcut(QKeySequence("Ctrl+O"), window)
shortcutOpen.activated.connect(lambda: Prompt("open"))

shortcutPy = QShortcut(QKeySequence("Ctrl+P"), window)
removePybox = QShortcut(QKeySequence("Ctrl+Shift+P"), window)
shortcutPy.activated.connect(PythonBox)
removePybox.activated.connect(lambda: PythonBox("remove"))

# end
if Pybox == True:
    PythonBox()
else:
    pass
window.setLayout(lay)
window.show()
print("Window shown.")
exit(app.exec())
