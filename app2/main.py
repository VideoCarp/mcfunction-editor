from sys import argv, exit
import highlighting, commands
from os.path import realpath, exists
from os import listdir
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
    QMenuBar,
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

def visualize(f):
    try:
        visual_extracter(f)
    except FileNotFoundError as err:
        print(err)
        file_name.setText("<h2>File: None</h2>")
        file_location.setText("<h2>Location: None</h2>")


def visual_extracter(f):
    # get path to directory
    dirpath = "/".join(f.split("/")[:-1])
    # make the visualisations
    files = listdir(dirpath)
    visualstring = "".join(f"{file}\n" for file in files)
    file_location.setText(visualstring)
    # do the file name
    text = f[f.rfind("/") + 1:]
    file_name.setText(f"<h2>Editing: {text}</h2>")


def open_file():
        f, _ = QFileDialog.getOpenFileName()
        if exists(f):
            with open(realpath(f)) as file:
                main_text_box.setPlainText(file.read())
                return
        print("Logging: Failed to open file.")
    
def save_file():
    if ScopeAvoid.normal_save_path is None:
        f, _ = QFileDialog.getSaveFileName()
        pathto = realpath(f)
        ScopeAvoid.normal_save_path = f
        with open(pathto, "w+") as file:
            file.write(main_text_box.toPlainText())

        visualize(f)

    else:
        filepath = ScopeAvoid.normal_save_path
        if exists(filepath):
            with open(realpath(filepath), "w+") as file:
                file.write(main_text_box.toPlainText())
                return visualize(filepath)

        print("Logging: Invalid save path.")
        ScopeAvoid.normal_save_path = None

def save_as():
    ScopeAvoid.normal_save_path = None
    save_file()


def swap_theme():
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
lay1 = QHBoxLayout()
spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
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
file_name = QLabel("<h2>Editing: None</h2>", parent=window)
file_location = QLabel("No directory opened", parent=window)
# Menu bar
menubar = QMenuBar(None)
file_menu = menubar.addMenu("File")
theme_menu = menubar.addMenu("Theme")
file_menu.addAction("Save...", save_file, "save")
file_menu.addAction("Open...", open_file, "open")
file_menu.addAction("Save as...", save_as, "saveas")
theme_menu.addAction("Swap Theme", swap_theme, "Swap Theme")

# connections
run_command.clicked.connect(lambda: commands.Execute(command_interface.text()))
main_text_box.textChanged.connect(countlines)


# LEFT SIDE
lay.addWidget(line_counter)
lay.addWidget(file_location)
lay.addItem(spacer)


# RIGHT SIDE
lay0.addWidget(main_text_box)
lay0.addWidget(command_interface)
lay0.addWidget(run_command)
lay0.addWidget(file_name)
lay0.addItem(spacer)
lay1 = QHBoxLayout()
lay1.addLayout(lay)
lay1.addLayout(lay0)

# finish up the layout
finished = QVBoxLayout()
finished.addWidget(menubar)
finished.addLayout(lay1)


# Shortcut:
shortcut_save = QShortcut(QKeySequence("Ctrl+S"), window)
shortcut_save.activated.connect(save_file)

shortcut_open = QShortcut(QKeySequence("Ctrl+O"), window)
shortcut_open.activated.connect(open_file)

shortcut_py = QShortcut(QKeySequence("Ctrl+P"), window)
removepybox = QShortcut(QKeySequence("Ctrl+Shift+P"), window)
shortcut_py.activated.connect(pythonbox)
removepybox.activated.connect(lambda: pythonbox("remove"))

# end
if pybox == True:
    pythonbox()
window.setLayout(finished)
window.show()
print("Window shown.")
exit(app.exec())
