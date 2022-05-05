import pyautogui
import time


class SickMoves:
    def __init__(self):
        self.start_time = time.time()
        self.timing = 765

    def increase_gnarly(self, score):
        if 15 < score < 20:
            self.timing = 785
        elif 20 < score < 30:
            self.timing = 805
        elif 30 < score < 40:
            self.timing = 825
        elif 40 < score < 50:
            self.timing = 840
        elif 60 < score < 80:
            self.timing = 860
        elif 80 < score < 100:
            self.timing = 900
        elif score > 100:
            self.timing = 940

    def air_time(self):
        pyautogui.press('space')

    def hang_low(self):
        pyautogui.keyDown('down')
        time.sleep(0.2)
        pyautogui.keyUp('down')
