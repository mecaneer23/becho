# Big Echo

Becho (or big echo) is a simple python script which utilizes [pyfiglet](https://github.com/pwaller/pyfiglet) to simplify command line printing

If you get a ModuleNotFoundError when running any of the included scripts, make sure to `pip install -r requirements.txt`

## Usage examples

### Becho

```bash
./becho This is example text
```

### Count down from (python)

```bash
count_down_from_ 10
```

### Count down from (tkinter)

Uses a tkinter gui instead of pyfiglet

```bash
./tk_count_down.py 10
```

### Count down from (bash)

Opens a new alacritty window but otherwise uses the python version

```bash
count_down_from.sh 10
```
