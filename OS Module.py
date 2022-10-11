"""
                                           OS module in Python
"""

import os
# Print current directory path:
print("Current Directory:", os.getcwd())
# change current directory path:
# os.chdir("C:/")
print("Changed Directory:", os.getcwd())
# List All Directories
print(os.listdir("D:/Python"))
# Renaming a File:
# os.rename("Pattern Problems.py", "Pattern Problems In Python.py")
# Check if path exists
print(os.path.exists("H:/"))
# Check if the file exists:
print(os.path.isfile("Recursion.py"))
# Joining two path. It helps in removing any trailing //
print(os.path.join("D://", "/Python"))
