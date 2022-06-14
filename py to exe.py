"""
Steps to convert .py file to .exe file
    1. install pyinstaller (pip install pyinstaller --user)
    2. convert the .py or any other extension with python code to .exe (pyinstaller <filename> )
    3. two folder will be generated build & dist
    4. dist will have the corresponding .exe file
    5. To generate only one file (pyinstaller  --onefile <filename>)
    Note: to avoid closing of the .exe terminal add a (a = input()) at the end of the code.
    This will make the code wait for an input from user hence it will not close instantly
"""