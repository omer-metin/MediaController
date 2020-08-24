# Windows Media Controller

Application for who does not have media short-cuts on the keyboard.

Short-Cuts:
    [fn] + [space]  : play-pause media
    [fn] + [right]  : next media
    [fn] + [left]   : previous media
    [fn] + [up]     : volume up
    [fn] + [down]   : volume down
    [fn] + ['m']    : mute-unmute volume

Application runs at background. 


If you want to run application at windows start-up you should follow below steps:
    
    - Create a short-cut of '.\build\exe.win-amd64-3.7\mediaController.exe'
    - copy/cut short-cut and paste it in '[X]:\Users\[user_name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

After this process, computer should be restarted.


If you want to build application your own you need follow below instructions:
    
    - You need cx_Freeze to build applticaiton. cx_Freeze can be downloaded by using 'pip install cx-Freeze' (https://cx-freeze.readthedocs.io/en/latest/)
    - Run 'python setup.py build' command on command-promt in directory where code is located.
