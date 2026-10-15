import platform
from platform import python_version

print(f"Verzija Python-a koju koristim je {platform.python_version()}")

python_version = platform.python_version()

version = int(python_version[0])
version_v2 = platform.python_version_tuple()[0]


if version != 3:
    print("Imate instaliranu pogresku verziju pajtona")
else:
    print("Verzija je dobra")