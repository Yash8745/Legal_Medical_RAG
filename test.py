import os
from rich import print 

# Option 1: Print as a dictionary
# print(dict(os.environ))

# Option 2: Loop through each environment variable and print key and value
for key, value in os.environ.items():
    print(f"{key}: {value}")