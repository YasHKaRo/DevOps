import os
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def answer():
    print(find_host(), os.environ.get("AUTHOR", "AUTHOR-а нет, увы"))

def find_host():
    hostname = os.open("/etc/hostname", 0)
    return os.read(hostname, 256)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer()