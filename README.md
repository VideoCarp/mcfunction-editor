# MCFunction Editor

<div align="center">
  <img src="https://raw.githubusercontent.com/VideoCarp/mcfunction-editor/main/repo/42F1B69E-6C0E-4E06-903C-E609D94D9245.png" height=200 width=200>
  <br>
  <a href="https://discord.gg/sTUFucA5xU">Discord Server</a>
</div>
<br>

This is a ready-to-use but being worked on text editor for Minecraft commands.<br>
It's currently aimed at Minecraft Bedrock Edition ***and*** Java Edition.<br>
See [CONTRIBUTING.md](https://github.com/VideoCarp/mcfunction-editor/blob/main/CONTRIBUTING.md) for contributions
and/or feature requests.
# Features:
* __Syntax Highlighting__<br>
This editor has proper syntax highlighting for commands.
* __Performance__<br>
Although it's written in Python, this editor still only uses ~15 mb of memory a second after being opened.<br>
Comparing this to your average Electron hello world, it's ~10x more performant on the memory side.<br>
If enough people want better performance, I can/may write this in C++, meaning it will have much better performance.
* __Small__<br>
The text editor is relatively small compared to any others. The download size is very small and its lightweight.
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
