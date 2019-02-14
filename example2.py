#!/usr/bin/python3

import os

uname = os.uname()

print("Hi, I am Linux") if uname.sysname == "Linux" else print("Hi, I am another operating system")
