import pyautogui as ag
import time
import os

WIDTH, HEIGHT = ag.size()
TEMPLATE_WIDTH = 2560
TEMPLATE_HEIGHT = 1440
NEXT_STEP_DURATION = 2
RETRY_DURATION = 2
DETECT_RETRY = 5
WAIT_TURN_DURATION = 10
CONFIDENCE = 0.9
TARGET_IMAGE_PATH = os.path.join("MD-autoplay", "target_image")

def click(target):
    while ag.position() != target:
        ag.moveTo(x=target[0], y=target[1])
    ag.click()

def detect_and_click(target_image, click_target=True):
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, target_image), confidence=CONFIDENCE)
    times = 0
    while not target and times < DETECT_RETRY:
        if click_target:
            print("Warning: {0} detect fail, try again after {1} seconds...".format(target_image, RETRY_DURATION))
        times = times + 1
        time.sleep(RETRY_DURATION)
        target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, target_image), confidence=CONFIDENCE)
    if click_target:
        time.sleep(NEXT_STEP_DURATION)
        click(target)
        time.sleep(NEXT_STEP_DURATION)
    else:
        return target

def drop_card():
    target = detect_and_click("drop_card.jpg", click_target=False)
    if not target:
        print("INFO: No card to drop.")
    else:
        click((target[0], target[1] + 250 / TEMPLATE_HEIGHT * HEIGHT))
        time.sleep(NEXT_STEP_DURATION)
        click((target[0], target[1] + 450 / TEMPLATE_HEIGHT * HEIGHT))

STATUS_LIST = [
    ("detect_lose", "lose"), 
    ("detect_continue_main", "continue_main"), # not necessary
    ("main1", "main"), 
    ("draw", "draw"), # not necessary
    ("opponent_turn", "opponent"), # not necessary
    ("detect_server_error", "error")
]
def detect_duel_status():
    for image, return_value in STATUS_LIST:
        target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, image + ".jpg"), confidence=CONFIDENCE)
        if target:
            return return_value

def play():
    try:
        while (True):
            status = detect_duel_status()
            if status == "main":
                detect_and_click("main1.jpg")
                detect_and_click("select_phase.jpg")
                drop_card()
            elif status == "draw":
                click((WIDTH / 2, HEIGHT / 2))
                time.sleep(NEXT_STEP_DURATION)
                click((WIDTH / 2, HEIGHT / 2))
            elif status == "opponent":
                print("INFO: Not our turn, try again after {0} seconds...".format(WAIT_TURN_DURATION))
                time.sleep(WAIT_TURN_DURATION - RETRY_DURATION)
            elif status == "lose":
                detect_and_click("lose.jpg")
                detect_and_click("battle_pass.jpg")
                target = detect_and_click("madel_gain.jpg", click_target=False)
                if target:
                    detect_and_click("madel_gain.jpg")
                detect_and_click("duel_result.jpg")
                target = detect_and_click("detect_level_up.jpg", click_target=False)
                if target:
                    detect_and_click("level_up.jpg")
                detect_and_click("duel.jpg")
            elif status == "error":
                detect_and_click("server_error.jpg")
                detect_and_click("duel.jpg")
            elif status == "continue_main":
                detect_and_click("continue_main.jpg")
            else:
                print("Warning: Duel status detect fail, try again after {0} seconds...".format(RETRY_DURATION))
            time.sleep(RETRY_DURATION)
    except KeyboardInterrupt as e:
        print("INFO: User terminated")

if __name__ == '__main__':
    input("Warning: Please make sure your MD is on main monitor\nPress enter to continue...")
    print("INFO: Monitor size: {0}, {1}".format(WIDTH, HEIGHT))
    target = detect_and_click("duel.jpg", click_target=False)
    if not target:
        print("ERROR: Startup failed. Please check your screen is staying on event menu.")
    else:
        click(target)
        time.sleep(WAIT_TURN_DURATION)
        play()