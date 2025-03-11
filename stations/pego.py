import utils
import time
import template
import windows
import ark
import variables
import settings
import discordbot

def pego_pickup(metadata):
    utils.turn_up(15)
    time.sleep(0.5)
    ark.open_structure()
    count_p = 0

    while template.template_sleep("inventory",0.7,1) == False and count_p < 3: #changed & added by purge
        count_p += 1
        discordbot.logger(f"Could not access Pego INV. Attempt: {count_p}/3")
        utils.pitch_zero()  #changed & added by purge
        utils.set_yaw(metadata.yaw) #changed & added by purge
        #utils.set_yaw(settings.station_yaw) #changed & added by purge
        utils.press_key("Run")
        utils.turn_up(15)
        time.sleep(0.5)
        ark.open_structure()

    count_p = 0
    time.sleep(0.5)

    if template.check_template("inventory",0.7):
        #ark.drop_all_inv()
        ark.search_in_inventory("pell")#will drop pellets instead instead of all the inv
        ark.drop_all_inv()
        time.sleep(0.2)
        ark.transfer_all_from()
        time.sleep(0.2)
        ark.close_inventory() # prevents pego being FLUNG
        
    time.sleep(0.5)
    utils.turn_down(utils.current_pitch)
    time.sleep(0.2)