# Windows Media Controller

**Background media short-cut application for who does not have media short-cuts on the keyboard**

## Usage
You can run application in two ways:
 - Running MediaController.exe file which is located `.\dist`.
 - Running mediaController.py file as python file.

Short-Cuts:
 * **pause/break**              : play-pause media
 * **fn + right**               : next media
 * **fn + left**                : previous media
 * **fn + up or fn + '+'**      : volume up
 * **fn + down or fn + '-'**    : volume down
 * **fn + '0'**                 : mute-unmute volume

## Installation

### Run at Windows start-up
If you want to run application at windows start-up you should follow below steps:

 - Copy(or cut) MediaController.exe file from `./dist` and paste it in `[X]:\Users\\[user_name]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

After this process, computer should be restarted.

### Build your own
If you want to build application your own you need follow below instructions:
    
#### Dependencies
 - You need [pynput 1.6.8](https://pypi.org/project/pynput/1.6.8/). Other versions of pynput unfortunately does not work with pyinstaller. To get pynput 1.6.8 you can use following command
    ```bash
        pip install pynput==1.6.8
    ```

#### Building
 - You need pyinstaller to build applticaiton. pyinstaller can be downloaded by using [pip](https://pypi.org/project/pyinstaller/)
    ```bash
        pip install pyinstaller
    ```
 - To build, run setup_onefile.bat file or following command on command-promt in directory where code is located.
    ```bash
        pyinstaller --onefile --noconsole mediaContolelr.py
    ```
