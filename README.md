# SpeChar

Easily type special characters!

## Requirements

> ```bash
> #python interpreter
> python3
> #this is needed to type the chosen character
> xdotool
> #python libraries, installed from pip
> PyQt6
>  # OR #
> PyQt5
> #those should already be installed 
> os
> subprocess
> sys
> ```
> 
> Tested succesfully on Linux, don't know on Windows and MacOs (surely won't work, but perhaps changing xdotool with something equivalent will)

## Preparation

* download this project somewhere in your PC
* make sure it has execution permission: `chmod +x /path/to/SpeChar.py`
* assign `/path/to/SpeChar.py` to a hotkey (for example, Super+Ins)
* done!

## Language and Qt version

* the default language is English and the default Qt version is PyQt5, if you wish to change those values run the script with those arguments:
  
  ```bash
  /path/to/speChar.py -l it -v 6 
  ```

* replacing `it` and `6` with desired language and version

* currently only English and Italian languages are supported, you can help adding your language! Just pull a request with the new `speChar_<your language>.config` and I'll add it quickly!

## Customization (optional)

the file SpeChar_XX.config contains the list of special characters available, using this format:

> `<character> <minus sign> <description>`

* no minus signs ("`-`") can be used, there must be just one for line, because the script splits in two searching for a minus sign. (There are better ways but I'm lazy and don't want to change the code lol)

* you can add, edit or remove any character from this configuration file

## Usage

now just press the hotkey whenever you want to insert a special character, type the name in the searchbar and select it with the arrows or clicking on it, and it will type it in your text!

## TODO

+ change font using a "math font"
+ ~~get screen size automatically~~
+ tidy up
+ ~~change scrollbar to native~~ (Qt5 supports themes better than Qt6)
* add more languages support
