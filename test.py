import os
print(os.environ["PUBLIC_KEY"])

with open("test", "wb") as file:
  file.write(os.environ["PUBLIC_KEY"])
