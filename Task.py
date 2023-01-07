Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> WARNING: The system preference "Prefer tabs when opening documents" is set to
"Always". This will cause various problems with IDLE. For the best experience,
change this setting when running IDLE (via System Preferences -> Dock).

SyntaxError: invalid syntax
>>> WARNING: The system preference "Prefer tabs when opening documents" is set to
>>> # a code to replace a char in a string.
>>> def replacer():
...     string= input('enter the string:')
...     position= int (input ('enter the position of the char:'))
...     char= input ('enter the new:')
...     string= string[:position]+char+string[position+1:]
...     print (string)
... 
...     
>>> 
>>> 
>>> # another approach
>>> 
... def replacer(string,position,char):
...     l=list(string)
...     l[position]=char
