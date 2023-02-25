# Colorum

Colorum is a simple terminal output colorizer for Python. Colorum supports both Python 2 and Python 3 and is available on PyPI. Once installed, you can use Colorum by importing it and then color text by calling to the color you want to use from the classes. This package can color text and the background of the console; it can also style these strings after they are printed. Colorum is a standalone file; it does not require anything to run except os and sys; the file simply floats around in your site-packages directory. Colorum is also very quick; this is because it uses system commands to re-color the terminal.

**Compatibility**
This package is compatible with Python 3 and windows 10 on linux the terminal does not recognize the "Color" command that the windows terminal uses to switch colors. I will add linux compatibility tomorrow and include it in 0.6 release soon after, dont forget to use the `pip install colorum --upgrade` command to upgrade your existing installation of colorum. This file version is also compatible with Windows 10 although this is how every other package does it so for now I will stick to the unique way.

### Examples

Coloring the console's text, replace the "Red" with any color like "Blue" this works for every class/function.
```python
from colorum import text

print(text.Red() + "Stay hydrated")
```

Changing the hue of console background is simple, replace the "Red" with any color like "Blue" this works for every class.
```python
from colorum import background

print(background.Red() + "Pizza is good")
```

Styling the outputted text on the console, this can be placed in front of any colorum statment.
```python
from colorum import style

print(style.Bright() + "I like coffee")
```


## Guide

To install Colorum, simply use pip (assuming Python is installed)  
```python
pip install colorum
```

**Functions**
```
text.Black()         background.Black()         style.Bright()
text.Blue()          background.Blue()          style.Dim()
text.Green()         background.Green()         style.ResetAll()
text.Aqua()          background.Aqua()
text.Red()           background.Red()
text.Purple()        background.Purple()
text.Yellow()        background.Yellow()
text.White()         background.White()
text.Gray()          background.Gray()
text.Lightblue()     background.Lightblue()
text.Lightgreen()    background.Lightgreen()
text.Lightaqua()     background.Lightaqua()
text.Lightred()      background.Lightred()
text.Lightpurple()   background.Lightpurple()
text.Lightyellow()   background.Lightyellow()
text.Brightwhite()   background.Brightwhite()

text.Reset()         background.Reset()
text.clear()         background.clear()
```

### License & Source
This project(Colorum) is licensed under the MIT license. The source code is available on [GitHub](https://github.com/itzCozi/Colorum) along with the [license](https://github.com/itzCozi/Colorum/blob/main/ignore/LICENSE) as this code is open source contributions are welcome and appreciated, if you have any issues please make a [ticket](https://github.com/itzCozi/Colorum/issues/new) or contact me.

## Extra
[Package on PyPi](https://pypi.org/project/Data-Extract/)  
[Latest Release](https://github.com/itzCozi/Data-Extraction/releases)  
[Quickstart Guide](https://github.com/itzCozi/Data-Extraction/wiki/Quickstart-Guide)

Contact Me
---------------------------------
discord: BadDevoleper#4200                                                                                                                                             
Email: Cooperransom08@outlook.com                                                                                                                                      
[Replit](https://replit.com/@cozi08) | 
[Twitter](https://twitter.com/ransom_cooper)
