import pyautogui as ag
import time
import os

WIDTH, HEIGHT = ag.size()
TEMPLATE_WIDTH = 2560
TEMPLATE_HEIGHT = 1440
NEXT_STEP_DURATION = 2
RETRY_DURATION = 2
DETECT_RETRY = 3
WAIT_TURN_DURATION = 10
CONFIDENCE = 0.9
TARGET_IMAGE_PATH = "target_image"

def click(target):
    while ag.position() != target:
        ag.click(x=target[0], y=target[1])

def detect_and_click(target_image):
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, target_image), confidence=CONFIDENCE)
    while not target:
        print("Warning: {0} detect fail, try again after {1} seconds...".format(target_image, RETRY_DURATION))
        time.sleep(RETRY_DURATION)
        target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, target_image), confidence=CONFIDENCE)
    time.sleep(NEXT_STEP_DURATION)
    click(target)
    time.sleep(NEXT_STEP_DURATION)

def detect_with_retry(target_image):
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, target_image), confidence=CONFIDENCE)
    times = 0
    while not target and times < DETECT_RETRY:
        times = times + 1
        time.sleep(RETRY_DURATION)
        target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, target_image), confidence=CONFIDENCE)
    return target

def drop_card():
    target = detect_with_retry("drop_card.jpg")
    if not target:
        print("INFO: No card to drop.")
    else:
        while ag.position() != target:
            ag.moveTo(x=target[0], y=target[1])
        click((target[0], target[1] + 250 / TEMPLATE_HEIGHT * HEIGHT))
        time.sleep(NEXT_STEP_DURATION)
        click((target[0], target[1] + 200 / TEMPLATE_HEIGHT * HEIGHT))

def detect_duel_status():
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, "detect_lose.jpg"), confidence=CONFIDENCE)
    if target:
        return "lose"
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, "main1.jpg"), confidence=CONFIDENCE)
    if target:
        return "main"
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, "draw.jpg"), confidence=CONFIDENCE)
    if target:
        return "draw"
    target = ag.locateCenterOnScreen(os.path.join(TARGET_IMAGE_PATH, "opponent_turn.jpg"), confidence=CONFIDENCE)
    if target:
        return "opponent"

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
                detect_and_click("madel_gain.jpg")
                detect_and_click("duel_result.jpg")
                target = detect_with_retry("detect_level_up.jpg")
                if target:
                    detect_and_click("level_up.jpg")
                detect_and_click("duel.jpg")
            else:
                print("Warning: Duel status detect fail, try again after {0} seconds...".format(RETRY_DURATION))
            time.sleep(RETRY_DURATION)
    except KeyboardInterrupt as e:
        print("INFO: User terminated")

if __name__ == '__main__':
    # input("Warning: Please make sure your MD is on main monitor\nPress enter to continue...")
    print("INFO: Monitor size: {0}, {1}".format(WIDTH, HEIGHT))
    target = detect_with_retry("duel.jpg")
    if not target:
        print("ERROR: Startup failed. Please check your screen is staying on event menu.")
    else:
        click(target)
        time.sleep(WAIT_TURN_DURATION)
        play()