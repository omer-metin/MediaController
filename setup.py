import cx_Freeze
import pynput

executables = [cx_Freeze.Executable("mediaController.py", base="Win32GUI")]

cx_Freeze.setup(
    name="Windows Media Controller",
    options={'build_exe': {"packages": ["pynput"]}},
    version="0.01",
    executables=executables
)
