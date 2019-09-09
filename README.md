# Python Unused Function Scanner

This python script takes another python script as an argument like so:
```
python scan.py path/to/some/script.py
```
<br>
In this case, it will search bad.py for functions in the script, and check if any are defined but not used.
<br>
If this is the case for any function, it will show a warning that the function is unused, like the following:
```
Warning, 'foo' is an unused function!
```
<br>
Otherwise it will give a confirmation message saying that the script is ok:
```
No problems in 'path/to/some/script.py' , all defined functions are used.
```
<br>

# License

This project is licensed under GPLv3 - see [LICENSE.txt](LICENSE.txt)
<br />