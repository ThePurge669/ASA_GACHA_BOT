import utils
import time
import template
import ark
import windows
import variables
import json
import settings
import discordbot

def load_resolution_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def open_crystals():
    count = 0
    while template.check_template("crystal_in_hotbar",0.7) and count < 350: # count is alittle higher incase while pressing the button it doesnt triger
        for x in range(10):
            utils.press_key(f"UseItem{x+1}")
            count += 1

def dedi_deposit(height):
    if height == 3:
        utils.turn_up(15)
        utils.turn_left(10)
        time.sleep(0.3)
        utils.press_key("Use")
        time.sleep(0.3)
        utils.turn_right(40)
        time.sleep(0.3)
        utils.press_key("Use")
        time.sleep(0.3)
        utils.turn_left(30)
        utils.turn_down(15)

    utils.turn_left(10)
    utils.press_key("Crouch")
    time.sleep(0.3)
    utils.press_key("Use")
    time.sleep(0.3)
    utils.turn_right(40)
    time.sleep(0.3)
    utils.press_key("Use")
    time.sleep(0.3)
    utils.turn_down(30)
    time.sleep(0.3)
    utils.press_key("Use")
    time.sleep(0.3)
    utils.turn_left(40)
    time.sleep(0.3)
    utils.press_key("Use")
    time.sleep(0.3)
    utils.press_key("Run")
    utils.turn_up(30)
    utils.turn_right(10)

def vault_deposit(items, metadata):
    side = metadata.side
    if side == "left":
        utils.turn_left(90)
    else:
        utils.turn_right(90)
    time.sleep(0.5)
    ark.open_structure()
    if template.template_sleep("vault",0.7,1) == False:
        ark.close_inventory()
        utils.pitch_zero()  # changed & added by purge
        utils.set_yaw(metadata.yaw)  # changed & added by purge
        if side == "left":
            utils.turn_left(90)
        else:
            utils.turn_right(90)
        time.sleep(0.5)
        ark.open_structure()
    if template.template_sleep("inventory",0.7,2):
        for x in range(len(items)):
            ark.search_in_inventory(items[x])
            ark.transfer_all_inventory()
            time.sleep(0.4)
        ark.close_inventory()
        time.sleep(0.5)
    if side == "left":
        utils.turn_right(90)
    else:
        utils.turn_left(90)
    time.sleep(0.5)

def drop_useless():
    # discordbot.logger("dropping all useless things")
    # utils.press_key("ShowMyInventory")
    #
    # if template.template_sleep("inventory",0.7,2):
    #     ark.drop_all_inv()
    #     time.sleep(0.4)
    #     ark.close_inventory()
    # time.sleep(0.5)
    # utils.turn_down(80)
    # time.sleep(0.5)
    #the above is the code just drop all items and not keep berryes.

    discordbot.logger("dropping all useless things")
    time.sleep(0.5)
    utils.press_key("Crouch")
    time.sleep(0.3)
    utils.press_key("ShowMyInventory")

    if template.template_sleep("inventory", 0.7, 2):
        ark.search_in_inventory(settings.berry_type)
        ark.drop_all_inv()
        time.sleep(0.4)
        ark.close_inventory()
    time.sleep(0.5)
    utils.press_key("Run")
    time.sleep(0.5)
    utils.press_key("ShowMyInventory")

    if template.template_sleep("inventory", 0.7, 2):
        ark.drop_all_inv()
        time.sleep(0.4)
        ark.close_inventory()
    time.sleep(0.5)
    utils.turn_down(80)
    time.sleep(0.5)
    ark.open_structure()
    if template.template_sleep("inventory", 0.7, 1):
        ark.transfer_all_from()  # dont need a close as a bag will disapear
        ark.close_inventory()
    else:
        discordbot.logger("no bag dropped")
    utils.press_key("Run")
    time.sleep(0.8)

def depo_grinder(metadata):
    utils.turn_right(180)
    time.sleep(0.5)
    ark.open_structure()
    time.sleep(0.4)
    count_a = 0
    while template.template_sleep("grinder",0.7,1) == False and count_a < 3:
        ark.close_inventory()
        utils.pitch_zero()  # changed & added by purge
        utils.set_yaw(metadata.yaw)  # changed & added by purge
        utils.turn_right(180)
        time.sleep(0.5)
        ark.open_structure()
        count_a += 1
        discordbot.logger(f"Failed to Deposit in grinder inv attempt: {count_a}/3")
    count_a = 0
    if template.template_sleep("inventory",0.7,2) == False:
        time.sleep(2)
        ark.open_structure()
        time.sleep(0.4)

    if template.check_template("inventory",0.7):
        ark.transfer_all_inventory()
        time.sleep(0.5)
        windows.click(variables.get_pixel_loc("dedi_withdraw_x"),variables.get_pixel_loc("dedi_withdraw_y"))
        time.sleep(0.4)
        ark.close_inventory()
    time.sleep(0.6)
    utils.turn_right(180)
    time.sleep(0.2)
    utils.press_key("Run")

def collect_grindables(metadata):
    time.sleep(0.4)
    utils.press_key("Run")
    utils.turn_right(90)
    time.sleep(0.8)
    ark.open_structure()
    time.sleep(0.4)
    count_b = 0
    while template.template_sleep("grinder",0.7,1) == False and count_b < 3:
        ark.close_inventory()
        utils.pitch_zero()  # changed & added by purge
        utils.set_yaw(metadata.yaw)  # changed & added by purge
        utils.turn_right(90)
        time.sleep(0.5)
        ark.open_structure()
        time.sleep(0.4)
        count_b += 1
        discordbot.logger(f"Failed Collecting from grinder inv attempt: {count_b}/3")
    count_b = 0
    if template.template_sleep("inventory",0.7,2) == False:
        time.sleep(2)
        ark.open_structure()
        time.sleep(0.4)
    if template.check_template("inventory",0.7):
        ark.transfer_all_from()
        time.sleep(0.2)
        ark.close_inventory()
    time.sleep(0.5)
    utils.turn_left(90)
    time.sleep(0.5) # stopping hitting E on the fabricator
    utils.pitch_zero()  # changed & added by purge
    utils.set_yaw(metadata.yaw)  # changed & added by purge
    time.sleep(0.5)
    dedi_deposit(settings.height_grind)
    time.sleep(0.2)

    #FROM HERE ADDED BY PURGE
    if settings.deposit_in_vault == False:
        utils.turn_left(90)
        utils.turn_up(15)
        time.sleep(0.3)
        utils.press_key("Use")
        time.sleep(0.3)
        utils.turn_down(15)
        time.sleep(0.3)
        utils.press_key("Use")
        time.sleep(0.3)
        utils.press_key("Crouch")
        utils.turn_down(20)
        time.sleep(0.3)
        utils.press_key("Use")
        time.sleep(0.3)
        utils.press_key("Run")
        utils.turn_up(20)
        utils.turn_right(90)
        time.sleep(0.2)
    #TILL HERE ADDED BY PURGE

    drop_useless()
    time.sleep(0.2)

def vaults(metadata):
    vaults_data = load_resolution_data("json_files/vaults.json")
    for entry_vaults in vaults_data:
        name = entry_vaults["name"]
        side = entry_vaults["side"]
        items = entry_vaults["items"]
        metadata.side = side
        discordbot.logger(f"openening up {name} on the {side} side to depo{items}")
        vault_deposit(items,metadata)

def deposit_all(metadata):
    time.sleep(0.5)
    utils.pitch_zero()  # changed & added by purge
    utils.set_yaw(metadata.yaw)  # changed & added by purge
    discordbot.logger("opening crystals")
    open_crystals()
    discordbot.logger("depositing in ele dedi")
    dedi_deposit(settings.height_ele)
    utils.press_key("Run")
    if settings.deposit_in_vault == True:
        vaults(metadata)
    if settings.height_grind != 0:
        discordbot.logger("depositing in grinder")
        time.sleep(0.3)
        depo_grinder(metadata)
        grindables_metadata = ark.get_station_metadata(settings.grindables)
        ark.teleport_not_default(grindables_metadata)
        discordbot.logger("collecting grindables")
        collect_grindables(grindables_metadata)
    else:
        drop_useless()

