Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> WARNING: The system preference "Prefer tabs when opening documents" is set to
"Always". This will cause various problems with IDLE. For the best experience,
change this setting when running IDLE (via System Preferences -> Dock).

SyntaxError: invalid syntax
>>> #leap year function
>>> 
>>> def leap_year():
...     year = int (input('enter the year:'))
...     
...     if year % 4 is 0 and year % 100 is not 0:
...         print (True)
... 
...     elif year % 400 is 0 and year % 100 is 0:
...         print (True)
...                 
...     else:
...         print (False)
... 
...         
>>> 
>>> leap_year()
enter the year:1900
False
