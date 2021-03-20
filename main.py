import pyautogui
import webbrowser
import time

from tower import go_to_tower, to_battle, skip_battle

def open_daily_quests():
    time.sleep(5)

    daily_quests_image = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/daily_quest.png', confidence=0.8)

    if daily_quests_image:
        middle_X = daily_quests_image.left + 20
        middle_Y = daily_quests_image.top + 15
        pyautogui.click(x=middle_X, y=middle_Y)   
    else:
        daily_quests_image = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/daily_quest.png', confidence=0.8)
        middle_X = daily_quests_image.left + 20
        middle_Y = daily_quests_check.top + 15
        pyautogui.click(x=middle_X, y=middle_Y)

def complete_daily_quests():
    time.sleep(3)

    complete = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/complete.png', confidence=0.8)
    if complete:
        middle_X = complete.left + 15
        middle_Y = complete.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
    else:
        complete = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/complete.png', confidence=0.8)
        if complete:
            middle_X = complete.left + 15
            middle_Y = complete.top + 15
            try:
                pyautogui.click(x=middle_X, y=middle_Y)
            except AttributeError:
                pass
    
chrome = webbrowser.open('www.facebook.com')

def click_into_hero_wars_logo():
    time.sleep(5)

    hero_wars_logo = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/hero_wars_logo.png', confidence=0.8)
    if hero_wars_logo:
        middle_X = hero_wars_logo.left + 50
        middle_Y = hero_wars_logo.top + 50
        pyautogui.click(x=middle_X, y=middle_Y)
        
    else:
        herowarslogo = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/hero_wars_logo.png', confidence=0.8)
        if herowarslogo:
            print("finnaly found")
        hero_wars_logo = herowarslogo
        middle_X = hero_wars_logo.left + 50
        middle_Y = hero_wars_logo.top + 50
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass

def click_into_close_button():
    button_x = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/x-button.png', confidence=0.8)
    if button_x:
        print("I'm closing ads")

        middle_X = button_x.left + 15
        middle_Y = button_x.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
    else:
        pyautogui.hotkey('f5')
        time.sleep(20)
        middle_X = button_x.left + 15
        middle_Y = button_x.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
        print("I have not found it")

def check_mail_box():
    mail_button = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/mail.png', confidence=0.8)
    if mail_button:
        middle_X = mail_button.left + 15
        middle_Y = mail_button.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
    else:
        time.sleep(3)
        mail_button = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/mail.png', confidence=0.8)
        middle_X = mail_button.left + 15
        middle_Y = mail_button.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass    

def collect_all_mail():
    time.sleep(3)
    collect_all = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
    if collect_all:
        print('I have found collect all')
        middle_X = collect_all.left + 15
        middle_Y = collect_all.top +15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass  
        collect_all = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
        if collect_all:
            middle_X = collect_all.left + 15
            middle_Y = collect_all.top +15
            try:
                pyautogui.click(x=middle_X, y=middle_Y)
            except AttributeError:
                pass  
    else:
        print("I have not found collect all")
        time.sleep(3)
        collect_all = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
        if collect_all:
            middle_X = collect_all.left + 15
            middle_Y = collect_all.top +15
            try:
                pyautogui.click(x=middle_X, y=middle_Y)
            except AttributeError:
                pass  
            collect_all = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
            if collect_all:
                middle_X = collect_all.left + 15
                middle_Y = collect_all.top +15
                try:
                    pyautogui.click(x=middle_X, y=middle_Y)
                except AttributeError:
                    pass  


click_into_hero_wars_logo()

print("I'm here")


# Close the ads panel
time.sleep(20)

click_into_close_button()

# daily questsprin
'''
open_daily_quests()
complete_daily_quests()
click_into_close_button()
check_mail_box()
collect_all_mail()
click_into_close_button()
'''
go_to_tower()
to_battle()
skip_battle()
