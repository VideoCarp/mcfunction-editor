# Manages commands.
from inspect import getsource
from PySide2.QtWidgets import QMessageBox
from search import searcher
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
    3. `search': Prompts CLI search for information.
    Available Functions:
    - `SavePath(location)': Modify the path in which saves are directed.
    Normally, this is done automatically when you save for the first time.
    - `CallCode(code: str)': Run some Python code. (can be done with exec too.)
    """, "Help"),
    "cmd": lambda: doCommand(var),
    "searc": searcher.do_search
    }
    startsSwitch(var, condition)
