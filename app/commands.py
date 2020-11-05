# Manages commands.
from inspect import getsource
from webbrowser import open_new_tab as tabbrowser
from PySide2.QtWidgets import QMessageBox
def msgbox(info, title="Command Bar"):
    msg = QMessageBox()
    msg.setStyleSheet("""
    QMessageBox {
        background-color: #222;
    }
    QLabel {
        color: #aaa;
    }"""
    )
    msg.setIcon(QMessageBox.Information)
    msg.setText(title)
    msg.setInformativeText(info)
    msg.setWindowTitle("Command Bar")
    msg.exec()


def startsSwitch(thevar, conditions):
    KEYS = []
    thevar = thevar.replace("/", "").replace(" ", "")
    for k,v in conditions.items():
        KEYS.append(k)
    for k,v in conditions.items():
        if thevar.startswith(k):
            v()
            if "msgbox" not in getsource(v):
                msgbox("Finished command!")
            return
    msgbox("Errored.")
def SavePath(location):
    try:
        ScopeAvoid.normalSavePath = location
    except:
        msgbox("Failed!")

def doCommand(inpvar):
    LST = inpvar.split("cmd")
    done = LST[1]
    del LST
    try:
        eval(done)
    except:
        msgbox("Failed")

def CallCode(code: str):
    exec(code)

def Execute(var):
    condition = {
    "help": lambda: msgbox("""
    1. `help' Displays help menu (this).
    2. `cmd <function_call>': `eval`s a function call.
    Available Functions:
    - `SavePath(location)': Modify the path in which saves are directed.
    Normally, this is done automatically when you save for the first time.
    - `CallCode(code: str)': Run some Python code. (can be done with exec too.)
    3. `wikibedrock': Opens up the 'wiki.bedrock.dev' wiki. (you may omit 'edrock')
    4. `tutorialbedrock': Opens up 'Commands Tutorial' on bedrock wiki. (you may omit 'edrock')
    5. `wikijava': Unavailable. I can't find, please create an issue or pull request if you find it. (may omit 'ava')
    6. `tutorialjava': Opens up 'https://www.digminecraft.com/game_commands/index.php'. 
    May be a low quality tutorial, if better found issue or pull request. (may omit 'ava')
    7. `repo': Opens up the mcfunction-editor repository on GitHub.
    """, "Help"),
    "cmd": lambda: doCommand(var),
    "wikib": lambda: tabbrowser("https://wiki.bedrock.dev"),
    "tutorialb": lambda: tabbrowser("https://wiki.bedrock.dev/tutorials/beginner-commands.html"),
    "repo": lambda: tabbrowser("https://github.com/VideoCarp/mcfunction-editor/blob/main/app/main.py")
    "tutorialj": lambda: tabbrowser("https://www.digminecraft.com/game_commands/index.php")
    }
    startsSwitch(var, condition)
