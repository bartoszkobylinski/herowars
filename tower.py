import pyautogui
import time

from detailed_jobs import locate_button_coords

def go_to_tower():
    time.sleep(3)
    tower_sign = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/tower.png', confidence=0.7)
    if tower_sign:
        locate_button_coords(tower_sign)
    else:
        tower_sign = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/tower.png', confidence=0.8)
        if tower_sign:
            locate_button_coords(tower_sign)

def to_battle():
    time.sleep(3)
    to_battle_sign = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/to_battle.png', confidence=0.8)
    if to_battle_sign:
        middle_X = to_battle_sign.left + 15
        middle_Y = to_battle_sign.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
    else:
        to_battle_sign = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/to_battle.png', confidence=0.8)
        if to_battle_sign:
            middle_X = to_battle_sign.left + 15
            middle_Y = to_battle_sign.top + 15
            try:
                pyautogui.click(x=middle_X, y=middle_Y)
            except AttributeError:
                pass            


def skip_battle():
    time.sleep(3)
    skip_battle = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/skip.png', confidence=0.8)
    if skip_battle:
        middle_X = skip_battle.left + 15
        middle_Y = skip_battle.top + 15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
    else:
        skip_battle = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/to_battle.png', confidence=0.8)
        if skip_battle:
            middle_X = skip_battle.left + 15
            middle_Y = skip_battle.top + 15
            try:
                pyautogui.click(x=middle_X, y=middle_Y)
            except AttributeError:
                pass 

def click_on_buff():
    buff_tower = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/buffer_tower.png', confidence=0.8)
    if buff_tower:
        middle_X = buff_tower.left + 15
        middle_Y = buff_tower.top +15
        try:
            pyautogui.click(x=middle_X, y=middle_Y)
        except AttributeError:
            pass
    else:
        buff_tower = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/buffer_tower.png', confidence=0.8)
        if buff_tower:
            middle_X = buff_tower.left + 15
            middle_Y = buff_tower.top +15
            try:
                pyautogui.click(x=middle_X, y=middle_Y)
            except AttributeError:
                pass
