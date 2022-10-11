"""
Import function allows us to use user-defined and in-built modules and their functions
"""

import sys
# python interpreter follows this path hierarchy to search for a module
print(sys.path)

"""
Note: its a good practice not to name any python file with a package name,as the interpreter
will search in the same directory for the package to be imported.
"""

# Importing from a user-defined file:

import TestImport
print(TestImport.add(78, 78))

