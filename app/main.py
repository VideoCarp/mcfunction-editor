import sys
import time
import highlighting, commands
from os import path
from PySide2.QtGui import QTextDocument, QKeySequence
from PySide2.QtWidgets import QApplication,QLabel,QWidget,QGridLayout,QPushButton\
,QPlainTextEdit,QFileDialog, QCompleter, QShortcut, QLineEdit
import threading

saveLocation = None
class ScopeAvoid():
    current = "dark"
    normalSavePath = None

def Prompt(option):
    if option == "open":
         f, _FILTER = QFileDialog.getOpenFileName()
         try:
             with open(path.realpath(f)) as file:
                 mainTextBox.setPlainText(file.read())
         except:
             print("Logging: Failed to get path for file.")
    else:
        if ScopeAvoid.normalSavePath is None:
            try:
                f, _FILTER = QFileDialog.getSaveFileName()
                ScopeAvoid.normalSavePath = f
                with open(path.realpath(f)) as file:
                    file.write(mainTextBox.toPlainText())
            except:
                pass

        if ScopeAvoid.normalSavePath is not None:
            try:
                with open(path.realpath(ScopeAvoid.normalSavePath), "w+") as file:
                    file.write(mainTextBox.toPlainText())
            except:
                print("Logging: Failed to get file path.")

 
def SwapTheme():
    if ScopeAvoid.current == "dark":
        with open(path.realpath("styles/light.qss"), "r") as f:
            window.setStyleSheet(f.read())
        ScopeAvoid.current = "light"
    else:
        with open(path.realpath("styles/dark.qss")) as f:
            window.setStyleSheet(f.read())
        ScopeAvoid.current = "dark"

def Loop():
    while True:
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


app = QApplication(sys.argv)
window = QWidget()
with open("styles/dark.qss") as sheet:
    window.setStyleSheet(sheet.read())

window.setWindowTitle("MCFunction Editor")
screen_x, screen_y = 500, 300
window.setGeometry(0, 0, screen_x, screen_y)
window.move(60, 15)

autoCompletions = [
    "execute", "tag", "testforblock", "setblock", "fill",
    "effect", "teleport", "summon", "clear", "give", "tellraw", "title",
    "particle", "scoreboard", "testfor", "tickingarea", "add", "remove",
    "gamerule", "true", "false", "tp", "type", "name"
]

lay = QGridLayout()
# lay.addWidget(widget, row, column)
saveButton = QPushButton("Save...", parent=window)
openButton = QPushButton("Open...", parent=window)
themeButton = QPushButton("Swap Theme", parent=window)

commandInterface = QLineEdit("Type a Command (see /help)", parent=window)
runCommand = QPushButton("Click to register command.", parent=window)
runCommand.clicked.connect(lambda: commands.Execute(commandInterface.text()))
mainTextBox = TxtCustom("Start typing...", parent=window)
mainTextBox.setFixedSize(screen_x, int(screen_y/1.5))
highlight = highlighting.MCFunction(mainTextBox.document())

lineCounter = QLabel("<h2>Lines: 0</h2>", parent=window)
lineCounter.setStyleSheet("lineCounter {\
    text-align: center;\
}")

saveButton.clicked.connect(lambda: Prompt("save"))
openButton.clicked.connect(lambda: Prompt("open"))
themeButton.clicked.connect(SwapTheme)


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
# end
threading.Thread(target=Loop, daemon=True).start()
window.setLayout(lay)
window.show()
print("Window shown.")
sys.exit(app.exec_())
print("Finished last line.")
