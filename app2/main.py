from sys import argv, exit
import highlighting, commands
from os.path import realpath
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QPlainTextEdit,
    QFileDialog,
    QLineEdit,
    QSpacerItem,
    QSizePolicy,
)
from PySide6.QtCore import Qt

pybox = False
##### Set this to 'True' if you want a box in which you can execute some Python.
##### You can use libraries with this too if you have them installed.
##### a bind (Ctrl+P) is also available. you can turn off pythonbox with ctrl+shift+p
save_location = None


class ScopeAvoid:
    current = "dark"
    normal_save_path = None


def prompt(option):
    if option == "open":
        f, _FILTER = QFileDialog.getOpenFileName()
        try:
            with open(realpath(f)) as file:
                main_text_box.setPlainText(file.read())
        except FileNotFoundError:
            print("Logging: Failed to get path for file.")
    else:
        if ScopeAvoid.normal_save_path is None:
            try:
                f, _FILTER = QFileDialog.getSaveFileName()
                try:
                    open(realpath(f))
                except FileNotFoundError:
                    ScopeAvoid.normal_save_path = None
                    return
                ScopeAvoid.normal_save_path = f
                with open(realpath(f)) as file:
                    file.write(main_text_box.toPlainText())
            except FileNotFoundError:
                print(
                    "May have failed to save, try checking if file was updated, or press 'Ctrl+S' again."
                )

        if ScopeAvoid.normal_save_path is not None:
            try:
                with open(realpath(ScopeAvoid.normal_save_path), "w+") as file:
                    file.write(main_text_box.toPlainText())
            except FileNotFoundError:
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
    if main_text_box.textChanged:
        lines = main_text_box.toPlainText()
        lineLen = len(lines.split("\n"))
        line_counter.setText(f"<h1>Lines: {lineLen}</h1>")


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


def pythonbox(arg=None):
    if arg != None:
        try:
            lay.removeWidget(pythonbox)
            lay.removeWidget(execute_box)
            return
        except:
            return
    pythonbox = QPlainTextEdit(
        "Type in Python here. Libs, if installed correctly will work too.",
        parent=window,
    )
    lay.addWidget(pythonbox, 1, 1)
    pythonbox.setFixedSize(screen_x / 4, screen_y / 4)
    execute_box = QPushButton("Run Python")

    def runpy():
        try:
            exec(pythonbox.toPlainText())
        except BaseException:
            print("pythonbox errored.")

    execute_box.clicked.connect(runpy)
    lay.addWidget(execute_box, 2, 1)


##############################
# Stuff other than functions #
##############################
app = QApplication(argv)
window = QWidget()

with open(realpath("styles/dark.qss")) as sheet:
    window.setStyleSheet(sheet.read())

window.setWindowTitle("MCFunction Editor")
screen_x, screen_y = 1200, 750
window.setGeometry(0, 0, screen_x, screen_y)
window.move(960, 540)


###################################
# Layouts  and widget definitions #
###################################
lay = QVBoxLayout()
lay0 = QVBoxLayout()
finished = QHBoxLayout()
spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
save_button = QPushButton("Save...", parent=window)
open_button = QPushButton("Open...", parent=window)
theme_button = QPushButton("Swap Theme", parent=window)
command_interface = QLineEdit("help", parent=window)
run_command = QPushButton("Click to register command.", parent=window)
main_text_box = TxtCustom("Start typing...", parent=window)
main_text_box.setFixedSize(screen_x, int(screen_y / 1.5))
highlight = highlighting.MCFunction(main_text_box.document())
exec_box = QPushButton("push")
line_counter = QLabel("<h2>Lines: 0</h2>", parent=window)
line_counter.setStyleSheet(
    """
line_counter {
    text-align: center;
}"""
)


# connections
run_command.clicked.connect(lambda: commands.Execute(command_interface.text()))
save_button.clicked.connect(lambda: prompt("save"))
open_button.clicked.connect(lambda: prompt("open"))
theme_button.clicked.connect(SwapTheme)
main_text_box.textChanged.connect(countlines)


# Sizing
small = 100
open_button.setFixedSize(small, small)
save_button.setFixedSize(small, small)
theme_button.setFixedSize(small, small)

"""
open_button  :: main_text_box
save_button  :: main_text_box
theme_button :: main_text_box
line_counter :: main_text_box
             :: command_interface :: run_command
"""
# LEFT SIDE
lay.addWidget(save_button)
lay.addWidget(open_button)
lay.addWidget(theme_button)
lay.addWidget(line_counter)
lay.addItem(spacer)

# RIGHT SIDE
lay0.addWidget(main_text_box)
lay0.addWidget(command_interface)
lay0.addWidget(run_command)
lay0.addItem(spacer)
finished = QHBoxLayout()
finished.addLayout(lay)
finished.addLayout(lay0)
# Shortcut:
shortcutSave = QShortcut(QKeySequence("Ctrl+S"), window)
shortcutSave.activated.connect(lambda: prompt("save"))

shortcutOpen = QShortcut(QKeySequence("Ctrl+O"), window)
shortcutOpen.activated.connect(lambda: prompt("open"))

shortcutPy = QShortcut(QKeySequence("Ctrl+P"), window)
removepybox = QShortcut(QKeySequence("Ctrl+Shift+P"), window)
shortcutPy.activated.connect(pythonbox)
removepybox.activated.connect(lambda: pythonbox("remove"))

# end
if pybox == True:
    pythonbox()
window.setLayout(finished)
window.show()
print("Window shown.")
exit(app.exec())
