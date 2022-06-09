"""
Write a code to extract all emails for any given string
"""


import re
strg = """My Name is puja. email is pujachatterjee@gmail.com
1730107@kiit.ac.in
pujach@yahoo.com, kp@msi.comTata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
+91 929241-7327
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii"""

pattern = re.compile(r'\w+[@]\w+')
match = pattern.finditer(strg)
for matches in match:
    print(matches)