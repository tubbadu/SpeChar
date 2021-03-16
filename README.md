# SpeChar

easily paste special characters!

## requirements

>     python3
>     
>     PySimpleGUI
>     pyperclip
>     
>     os
>     subprocess
>     sys

## preparation
* download this project somewhere in your PC
* assign SpeChar.py to a hotkey (for example, Super+Insert)
* done!

## customization (optional)
the file SpeChar.config contains the list of special characters available, using this format: <br>

> `<character> <minus sign> <description>`<br>

no minus signs ("-") can be used, there must be just one for line, because the script splits in two searching for a minus sign.
you can add, edit or remove any character from this configuration file

## usage
now just press the hotkey whenever you want to insert a special character, type the name in the searchbar and select it with the arrows or clicking on it, and it will copy the character to your clipboard and paste it in your text!
