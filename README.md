# SpeChar

easily paste special characters!

## Requirements
>     #python interpreter
>     python3
>     #python libraries, installed from pip
>     PySimpleGUI
>     pyperclip
>     #those should already be installed 
>     os
>     subprocess
>     sys
> 
> Tested succesfully on Linux, don't know on Windows MacOs

## Preparation
* download this project somewhere in your PC
* assign SpeChar.py to a hotkey (for example, Super+Insert)
* done!

## Customization (optional)
the file SpeChar.config contains the list of special characters available, using this format: <br>

> `<character> <minus sign> <description>`<br>

no minus signs ("`-`") can be used, there must be just one for line, because the script splits in two searching for a minus sign.
you can add, edit or remove any character from this configuration file

## Usage
now just press the hotkey whenever you want to insert a special character, type the name in the searchbar and select it with the arrows or clicking on it, and it will copy the character to your clipboard and paste it in your text!

## TODO
change the icon