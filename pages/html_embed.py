import subprocess
import os
from pathlib import Path
import os.path
from os import path

# Vista riscorsiva della cartella corrente per individuare ogni file .tex
for cartella, sottocartelle, files in os.walk(os.path.dirname(os.getcwd())):
    print(cartella)
    print(sottocartelle)
    for file in files:
        print(file)