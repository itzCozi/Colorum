# Colorum

Colorum is a simple terminal output colorizer for Python, Colorum supports both Python 2 and Python 3 and is available on PyPI. Once installed, you can use Colorum by importing it and then color text by calling to the color you want to use from the classes.

### Examples

Coloring the text, replace the "Red" with any color like "Blue" this works for every class.
```
from colorum import text

print(text.Red() + "Stay hydrated")
```

Changing the color of console background, replace the "Red" with any color like "Blue" this works for every class.
```
from colorum import background

print(background.Red() + "Pizza is good")
```

Styling the outputted text, this can be placed in front of any color statment.
```
from colorum import style

print(style.Bright() + "I like coffee")
```

