from selenium import webdriver
from parkour import SickMoves
from PIL import ImageGrab
import numpy as np
import pyautogui
import time

game_on = True
URL = "https://tuckercraig.com/dino/"
chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(URL)
driver.maximize_window()
time.sleep(1)
pyautogui.press('space')

score_list = []
rex = SickMoves()
while game_on:
    score = time.time() - rex.start_time
    rex.increase_gnarly(score)
    jump = ImageGrab.grab((740, 405, rex.timing, 410))
    duck = ImageGrab.grab((750, 345, rex.timing, 363))
    jump_n = np.array(jump)
    duck_n = np.array(duck)
    if 83 in jump_n:
        rex.air_time()
    if 83 in duck_n:
        rex.hang_low()
    game_over = ImageGrab.grab((900, 300, 1000, 330))
    game_over_array = np.array(game_over)
    if 83 in game_over_array:
        score_list .append(round(score))
        print(score_list)
        rex.timing = 765
        rex.start_time = time.time()
        time.sleep(1)
        pyautogui.press('space')
