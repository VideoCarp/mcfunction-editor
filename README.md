# MCFunction Editor

<div align="center">
  <img src="https://raw.githubusercontent.com/VideoCarp/mcfunction-editor/main/repo/42F1B69E-6C0E-4E06-903C-E609D94D9245.png" height=200 width=200>
  <br>
  <a href="https://discord.gg/sTUFucA5xU">Discord Server</a>
</div>
<br>

![image](https://user-images.githubusercontent.com/66365570/164748718-18647bd9-ab9a-40b1-84b8-cea4576833ce.png)


This is a ready-to-use but being worked on text editor for Minecraft commands.<br>
It's currently aimed at Minecraft Bedrock Edition ***and*** Java Edition.<br>
See [CONTRIBUTING.md](https://github.com/VideoCarp/mcfunction-editor/blob/main/CONTRIBUTING.md) for contributions
and/or feature requests.
# Features:
* __Syntax Highlighting__<br>
This editor has proper syntax highlighting for commands.
* __Performance__<br>
Although it's written in Python, this editor is _way_ more efficient than performance intensive editors like VSCode.
It uses at least 10 times less ram. And on my 1.8 GHz (very bad) CPU, CPU usage is around 0-2% while writing!

![image](https://user-images.githubusercontent.com/66365570/164748899-40c48b7b-cdf5-4ef2-b8c9-8ba7eed47397.png)

* __Small__<br>
The text editor is relatively small compared to any others. The download size is very small and it's lightweight.
* __Easy Manipulation__<br>
You can *easily* manipulate parts of the text editor by just configuring variables.
* __Aimed at Commands__<br>
This editor is aimed specifically for commands and mcfunction, nothing else meaning it's the main focus and will be richest.
* __Command Bar__<br>
*Does not refer to CLI*<br>
The editor has a small command bar which you can run Python, some editor methods, or get documentation from.<br>
* __In-editor Python__<br>
*Available only in beta.*<br>
Allows you to run Python to assist yourself with certain tasks, such as folder setup.<br>
It also **allows libraries** to be used while running Python on the MCFunction editor.<br>
This also means you can *easily* extend the exitor
# Screenshots:

<img src="https://github.com/VideoCarp/mcfunction-editor/blob/main/repo/img.png?raw=true">

# Changelog
Recent changes, whether or not in the current latest tag.<br>
If you would like to test things **before** the tag is released, just manually copy each file **OR** clone/download the repo.
* Add support for Python to be ran in the editor.
* Fix bug of save shortcut that removes the need of save as every time using invalid file path if none is provided.
# Installation:
For the **latest release**, simply follow the instructions on the release. Releases are also called 'tags'.<br>
For **latest working beta**:
* Install Python 3.9+ (make ***sure to tick environment variable***)
* Run `pip install PySide6`, if it fails try `pip3 install PySide6` on Command Prompt/Terminal.
* Download the repository

<div align="center">
    <img src="https://raw.githubusercontent.com/VideoCarp/mcfunction-editor/main/repo/6B35181E-CBCF-43CC-A4A9-BA08CCF4D083.jpeg" width=300 height=200>
</div>

* Go to the 'app' directory, go to `main.py`, read through the first comment.
* Run `main.py` and you're done.
I recommend you make a shortcut to `main.py`.
If there are any problems, get the path to your installation of MCFunction-Editor. Copy it.
Go to Command Prompt and run `cd <path>`.
Then, do `py main.py`.

To make a shortcut, create a batch file. Put the following contents in it:
```batch
cd <path to mcfunction editor>
py main.py
```

`pip is not recognized` well if `pip3` doesn't work either, search up how to add python to your environment path variable. You did not install Python
with the same instructions here, fortunately it can be fixed. Same goes if any command won't work.

