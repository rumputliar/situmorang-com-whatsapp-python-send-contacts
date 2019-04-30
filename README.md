# whatsapp-python-send-contacts
This will automate sending messages to several contacts in WhatsApp using Python

Step 1: Install Selenium 
```sh
$ pip3 install selenium
```

UPDATED: Steps 2, 3 & 4 no longer required

Step 2: Selenium requires a driver to interface with the chosen browser.
[Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
[FireFox](https://github.com/mozilla/geckodriver/releases)
[safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)

Step 3: Extract the downloaded driver onto a folder

Step 4: Set path variable to the environment. Paste this command to the terminal
```sh
$ export PATH=$PATH:/home/pathofthedriverfolder/
Eg: $ export PATH=$PATH:/home/situmorang/Download/WhatsappSend
```
Step 5: run whatsapp.py using Python3
```sh
$ python3 whatsapp.py
