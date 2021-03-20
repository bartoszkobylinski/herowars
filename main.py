import pyautogui
import webbrowser
import time

from tower import go_to_tower, to_battle, skip_battle
from detailed_jobs import locate_button_coords


def open_daily_quests():
    time.sleep(5)

    daily_quests_image = pyautogui.locateOnScreen(
        '/home/bart/Pictures/hero_wars/daily_quest.png', confidence=0.8)

    if daily_quests_image:
        locate_button_coords(daily_quests_image)
    else:
        daily_quests_image = pyautogui.locateOnScreen(
            '/home/bart/Pictures/hero_wars/daily_quest.png', confidence=0.8)
        locate_button_coords(daily_quests_image)


def complete_daily_quests():
    time.sleep(3)

    complete = pyautogui.locateOnScreen(
        '/home/bart/Pictures/hero_wars/complete.png', confidence=0.8)
    if complete:
        locate_button_coords(complete)
    else:
        complete = pyautogui.locateOnScreen(
            '/home/bart/Pictures/hero_wars/complete.png', confidence=0.8)
        if complete:
            locate_button_coords(complete)


chrome = webbrowser.open('www.facebook.com')


def click_into_hero_wars_logo():
    time.sleep(5)

    hero_wars_logo = pyautogui.locateOnScreen(
        '/home/bart/Pictures/hero_wars/hero_wars_logo.png', confidence=0.8)
    if hero_wars_logo:
        locate_button_coords(hero_wars_logo)

    else:
        herowarslogo = pyautogui.locateOnScreen(
            '/home/bart/Pictures/hero_wars/hero_wars_logo.png', confidence=0.8)
        if herowarslogo:
            locate_button_coords(herowarslogo)


def click_into_close_button():
    button_x = pyautogui.locateOnScreen(
        '/home/bart/Pictures/hero_wars/x-button.png', confidence=0.8)
    if button_x:
        locate_button_coords(button_x)
        print("I'm closing ads")
    else:
        pyautogui.hotkey('f5')
        time.sleep(20)
        locate_button_coords(button_x)


def check_mail_box():
    mail_button = pyautogui.locateOnScreen(
        '/home/bart/Pictures/hero_wars/mail.png', confidence=0.8)
    if mail_button:
        locate_button_coords(mail_button)
    else:
        time.sleep(3)
        mail_button = pyautogui.locateOnScreen(
            '/home/bart/Pictures/hero_wars/mail.png', confidence=0.8)
        locate_button_coords(mail_button)


def collect_all_mail():
    time.sleep(3)
    collect_all = pyautogui.locateOnScreen(
        '/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
    if collect_all:
        print('I have found collect all')
        locate_button_coords(collect_all)
        collect_all = pyautogui.locateOnScreen(
            '/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
        if collect_all:
            locate_button_coords(collect_all)
    else:
        print("I have not found collect all")
        time.sleep(3)
        collect_all = pyautogui.locateOnScreen(
            '/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
        if collect_all:
            locate_button_coords(collect_all)
            collect_all = pyautogui.locateOnScreen(
                '/home/bart/Pictures/hero_wars/collect_all.png', confidence=0.8)
            if collect_all:
                locate_button_coords(collect_all)


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
