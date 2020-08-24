# Windows Media Controller

**Background media short-cut application for who does not have media short-cuts on the keyboard**

## Usage
You can run application in two ways:
 - Running mediaController.exe file which is located `.\build\exe.win-amd64-3.7`.
 - Running mediaController.py file as python file.

Short-Cuts:
 * **fn + space**  : play-pause media
 * **fn + right**  : next media
 * **fn + left**   : previous media
 * **fn + up**     : volume up
 * **fn + down**   : volume down
 * **fn + 'm'**    : mute-unmute volume

## Installation

### Run at Windows start-up
If you want to run application at windows start-up you should follow below steps:
    
 - Create a short-cut of `.\build\exe.win-amd64-3.7\mediaController.exe`
 - Copy(or cut) created short-cut and paste it in `[X]:\Users\\[user_name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

After this process, computer should be restarted.

### Build your own
If you want to build application your own you need follow below instructions:
    
 - You need cx_Freeze to build applticaiton. cx_Freeze can be downloaded by using [pip](https://cx-freeze.readthedocs.io/en/latest/)
    ```bash
        pip install cx-Freeze
    ```
 - To build run following command on command-promt in directory where code is located.
    ```bash
        python setup.py build
    ```
