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
        locate_button_coords(to_battle_sign)
    else:
        to_battle_sign = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/to_battle.png', confidence=0.8)
        if to_battle_sign:
            locate_button_coords(to_battle_sign)


def skip_battle():
    time.sleep(3)
    skip_battle = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/skip.png', confidence=0.8)
    if skip_battle:
        locate_button_coords(skip_battle)
    else:
        skip_battle = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/to_battle.png', confidence=0.8)
        if skip_battle:
            locate_button_coords(skip_battle)

def click_on_buff():
    buff_tower = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/buffer_tower.png', confidence=0.8)
    if buff_tower:
        locate_button_coords(buff_tower)
    else:
        buff_tower = pyautogui.locateOnScreen('/home/bart/Pictures/hero_wars/buffer_tower.png', confidence=0.8)
        if buff_tower:
            locate_button_coords(buff_tower)
