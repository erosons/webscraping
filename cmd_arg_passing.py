from selenium import webdriver
import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from Command line when the file is run
    address = ','.join(sys.argv[1:])
    print(address)
else:
    # Get address from Clipboard , if you are using Mac simply CMD C or CTRL+C in windows
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


# Alternatively


browser = webdriver.Chrome()

browser.get('https://www.google.com/maps/place/' + address)
