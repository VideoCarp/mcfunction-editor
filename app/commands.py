# Manages commands.
from inspect import getsource
from PyQt5.QtWidgets import QMessageBox
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


def Execute(var):
    condition = {
    "help": lambda: msgbox("Help:\n1. `cmd setPath(path)' for non-as saving. Usually automatic.", "Help"),
    "cmd": lambda: doCommand(var)
    }
    startsSwitch(var, condition)
