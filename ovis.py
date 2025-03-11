import pyautogui
import numpy as np
import time
#from win32comext.axdebug.debugger import Break
import ark
import screen
import discordbot
import variables
import settings
import utils
import win32clipboard
import windows
import template
import time
from ark import open_inventory, search_in_inventory, close_inventory


def main():
    print("You have 5 seconds to change to the game window.")
    #discordbot.logger("You have 5 seconds to change to the game window.")
    time.sleep(3)
    start()

    farm = True
    start_time = time.time()  # Track the time when farming starts
    capped_time = 20  # Time threshold in seconds (30) | this timers is set for small tribes with event RATES = 4.5
    press_keys_timer = time.time()  # Timer to track when to press keys 2 and 3
    press_keys_interval = 20 * 60  # 20 minutes in seconds
    retry = 0
    
    while True:
        current_time = time.time()
        # Check if we have passed 20 seconds and it's not capped
        if time.time() - start_time > capped_time and not template.template_sleep_no_bounds("slot_capped", 0.7, 0.6):
            retry += 1
            print(f"No cap detected after 20 seconds. BRING MORE OVIS ASAP !. Retrying to farm in 4 minutes. ATTEMPT: {retry}/5.")
            time.sleep(0.2)
            pyautogui.mouseUp()
            utils.press_key("Enter")
            time.sleep(0.2)
            pyautogui.write(f"Yo bring me more ovis right now!!!")
            #pyautogui.write(f"No cap detected after 20 seconds. BRING MORE OVIS ASAP !. Retrying to farm in 1 minute. ATTEMPT: {retry}/5")
            time.sleep(0.2)
            utils.press_key("Enter")# Stop the mouse press
            time.sleep(60)
            if retry < 6:
                time.sleep(0.2)
                start()
                start_time = time.time()
                pyautogui.mouseDown()
                continue
            else:
                time.sleep(0.2)
                deposit()
                time.sleep(0.2)
                drop()
                time.sleep(0.2)
                utils.press_key("Enter")
                time.sleep(0.2)
                pyautogui.write("I'm going to stop farming the ovises bro, i'm tired xd")
                #pyautogui.write(f"Stopping Ovis Farm. There were no more ovis provided to farm. FINAL ATTEMPT: {retry}/5")
                time.sleep(0.2)
                utils.press_key("Enter")
                print(f"Stopping Ovis Farm. There were no more ovis provided to farm. FINAL ATTEMPT: {retry}/5")
                break


        if not template.template_sleep_no_bounds("slot_capped", 0.7, 0.6):
            if farm:
                print("STARTING FARMING")
                pyautogui.mouseDown()  # Simulate pressing the left mouse button
                start_time = time.time()  # Reset the timer when farming starts
                farm = False
                time.sleep(0.5)  # Delay to ensure things settle down
                retry = 0  # resets the retry count once is able to get capped again
            continue  # Keep checking the cap status

        if template.template_sleep_no_bounds("slot_capped", 0.7, 0.6):
            print("We are capped.")
            time.sleep(0.2)
            pyautogui.mouseUp()  # Stop the mouse press
            time.sleep(0.2)
            if current_time - press_keys_timer > press_keys_interval:
                print("Eating Food & Water")
                utils.press_key("2")
                time.sleep(0.2)  # Small delay to simulate human behavior
                utils.press_key("3")
                print("Pressed keys 2 and 3 after 20 minutes to Replenish Food.")
                press_keys_timer = current_time  # Reset the timer for the next 20 minutes
            # utils.turn_up(15) #corrects the camera after it gets capped
            time.sleep(0.2)
            deposit()
            time.sleep(0.2)
            farm = True
            if template.template_sleep_no_bounds("slot_capped", 0.7, 0.8):
                print("Program Stopped - Slot Capped & DEDIS FULL (EMPTY THEM ASAP!).")
                break  # Stop the program when the slot is capped
            drop()
            start()
            start_time = time.time()


def start():
    time.sleep(0.5)
    utils.pitch_zero()  # changed & added by purge
    utils.set_yaw(settings.station_yaw)  # changed & added by purge
    utils.press_key('Run')
    time.sleep(0.3)
    utils.press_key("Crouch")
    time.sleep(0.3)
    utils.turn_down(15)


def drop():
    open_inventory()
    time.sleep(0.3)
    search_in_inventory('mutt')
    ark.drop_all_inv()
    search_in_inventory('pelt')
    time.sleep(0.2)
    ark.drop_all_inv()
    time.sleep(0.2)
    ark.close_inventory()
    time.sleep(0.6)

    # utils.zero()  # added by purge
    # utils.set_yaw(settings.station_yaw)# added by purge
    # time.sleep(0.3)
    # utils.press_key("Crouch")
    # time.sleep(0.3)
    # utils.turn_down(15)
    # time.sleep(0.3)


def deposit():
    time.sleep(0.3)
    utils.turn_right(90)
    time.sleep(0.3)
    utils.press_key("Use")  # row 1 bottom dedi
    time.sleep(0.3)
    utils.turn_up(15)
    utils.press_key('Run')
    time.sleep(0.3)
    utils.press_key("Use")  # row 1 middle dedi
    time.sleep(0.3)
    utils.turn_up(30)
    time.sleep(0.3)
    utils.press_key("Use")  # row 1 top dedi
    time.sleep(0.3)
    utils.turn_right(60)
    time.sleep(0.3)
    utils.press_key("Use")  # row 2 top dedi
    time.sleep(0.3)
    utils.turn_down(30)
    time.sleep(0.3)
    utils.press_key("Use")  # row 2 middle dedi
    time.sleep(0.3)
    utils.press_key("Crouch")
    utils.turn_down(15)
    time.sleep(0.3)
    utils.press_key("Use")  # row 2 bottom dedi
    time.sleep(0.3)
    utils.turn_right(60)
    time.sleep(0.3)
    utils.press_key("Use")  # row 3 bottom dedi
    time.sleep(0.3)
    utils.turn_up(15)
    utils.press_key('Run')
    time.sleep(0.3)
    utils.press_key("Use")  # row 3 middle dedi
    time.sleep(0.3)
    utils.turn_up(30)
    time.sleep(0.3)
    utils.press_key("Use")  # row 3 top dedi
    time.sleep(0.3)
    utils.turn_right(60)
    time.sleep(0.3)
    utils.press_key("Use")  # row 4 top dedi
    time.sleep(0.3)
    utils.turn_down(30)
    time.sleep(0.3)
    utils.press_key("Use")  # row 4 middle dedi
    time.sleep(0.3)
    utils.press_key("Crouch")
    utils.turn_down(15)
    time.sleep(0.3)
    utils.press_key("Use")  # row 4 bottom dedi


if __name__ == '__main__':
    main()
    # start()
    # deposit()
    # drop()

