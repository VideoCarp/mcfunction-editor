# Manages commands.
from inspect import getsource
from PySide6.QtWidgets import QMessageBox


class ScopeAvoid:
    current = "dark"
    normal_save_path = None


def msgbox(info, title="Command Bar"):
    msg = QMessageBox()
    msg.setStyleSheet(
        """
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


def start_switch(thevar, conditions):
    thevar = thevar.replace("/", "").replace(" ", "")
    KEYS = [k for k, v in conditions.items()]
    for k, v in conditions.items():
        if thevar.startswith(k):
            v()
            if "msgbox" not in getsource(v):
                msgbox("Finished command!")
            return
    msgbox("Errored.")


def save_path(location):
    try:
        ScopeAvoid.normal_save_path = location
    except Exception:
        msgbox("Failed!")


def do_command(inpvar):
    LST = inpvar.split("cmd")
    done = LST[1]
    del LST
    try:
        eval(done)
    except Exception:
        msgbox("Failed")


def call_code(code: str):
    exec(code)


def Execute(var):
    condition = {
        "help": lambda: msgbox(
            """
    1. `help' Displays help menu (this).
    2. `cmd <function_call>': `eval`s a function call.
    Available Functions:
    - `save_path(location)': Modify the path in which saves are directed.
    Normally, this is done automatically when you save for the first time.
    - `call_code(code: str)': Run some Python code. (can be done with exec too.)
    """,
            "Help",
        ),
        "cmd": lambda: do_command(var),
    }
    start_switch(var, condition)
