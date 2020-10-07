import cx_Freeze
import pynput
import queue

executables = [cx_Freeze.Executable("mediaController.py", base="Win32GUI")]

cx_Freeze.setup(
    name="Windows Media Controller",
    options={'build_exe': {"packages": ["pynput", "queue"]}},
    version="0.03",
    executables=executables
)
