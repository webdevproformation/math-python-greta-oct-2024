# module 

- 3 types de module 
    1. buildin (directement livré avec Python)
        - builtins (print / range ...)
        - random 
        - datetime 
        - sys
        - ...

```py
import datetime
import sys

....
```


    2. fait maison (=> créer par le développeur)

```py
# lib.py
def a():
    pass
```

```py
# principal.py
import lib # syntaxe 1

lib.a()
```

```py
# principal.py
from lib import a # syntaxe 2

a()
```

    3. téléchargé depuis internet  (pypi.org)
        1. BeautifulSoap
        1. requests
        1. Flask
        1. panda 
        1. numpy 

ouvrir un terminal => `pip install <module>`