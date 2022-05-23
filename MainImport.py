"""
When we import a file, the whole file is executed. In order to avoid this and allow only execution
of particular parts of the file we use main.
"""

# Importing TestImport file

import TestImport

print(TestImport.sub(90, 45))
