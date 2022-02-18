from typing import List
import requests
import sys


# vvv SET BITS IN COOKIE HERE vvv
bits_in_cookie = 0
# ^^^ SET BITS IN COOKIE HERE ^^^


debug = "--debug" in sys.argv
print("Welcome to anastarawneh's bit shop profit calculator script")
if bits_in_cookie == 0 or "--setbits" in sys.argv:
    bits_in_cookie = int(input("How many bits can you get per cookie: "))
    print(f"Set bits in cookie to {bits_in_cookie}. To avoid this prompt, open the python file in a text editor, and set the 'bits_in_cookie' variable to the specified amount.")
if debug: print("Sending request to get auction page count")
data: dict = requests.get("https://api.hypixel.net/skyblock/auctions").json()
pages: int = data["totalPages"]
if debug: print(f"Total auction pages: {pages}")

if debug: print("Sending request to get bazaar price for booster cookies")
cookie: dict = requests.get("https://api.hypixel.net/skyblock/bazaar").json()["products"]["BOOSTER_COOKIE"]
cookie_sell_price = cookie["sell_summary"][0]["pricePerUnit"]
if debug: print(f"Cookie price: {cookie_sell_price}")

if debug: print("Starting request loop to get all auction house pages")
auctions: List = []
for i in range(pages):
    json = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={i}").json()
    try:
        page = json["auctions"]
    except:
        print(f"Page {i}: {json}")
    for item in page: auctions.append(item)
    print(f"Added page {i+1}/{pages} - " + str(int((i+1)/pages*100)) + "%   \r", end="")
print("")

bins: List = []
for auction in auctions:
    if "bin" in auction: bins.append(auction)

if debug: print(f"{len(auctions)} total auctions")
if debug: print(f"{len(bins)} bin auctions")

bit_shop_bins: dict = {
    "god_potion": [],
    "kat_flower": [],
    "heat_core": [],
    "hyper_catalyst_upgrade": [],
    "ultimate_carrot_candy_upgrade": [],
    "colossal_experience_bottle_upgrade": [],
    "jumbo_backpack_upgrade": [],
    "minion_storage_x-pender": [],
    "hologram": [],
    "builder's_wand": [],
    "block_zapper": [],
    "bits_talisman": [],
    "autopet_rules_2-pack": [],
    "kismet_feather": []
}

for bin in bins:
    if bin["item_name"] == "God Potion": bit_shop_bins["god_potion"].append(bin)
    if bin["item_name"] == "Kat Flower": bit_shop_bins["kat_flower"].append(bin)
    if bin["item_name"] == "Heat Core": bit_shop_bins["heat_core"].append(bin)
    if bin["item_name"] == "Hyper Catalyst Upgrade": bit_shop_bins["hyper_catalyst_upgrade"].append(bin)
    if bin["item_name"] == "Ultimate Carrot Candy Upgrade": bit_shop_bins["ultimate_carrot_candy_upgrade"].append(bin)
    if bin["item_name"] == "Colossal Experience Bottle Upgrade": bit_shop_bins["colossal_experience_bottle_upgrade"].append(bin)
    if bin["item_name"] == "Jumbo Backpack Upgrade": bit_shop_bins["jumbo_backpack_upgrade"].append(bin)
    if bin["item_name"] == "Minion Storage X-pender": bit_shop_bins["minion_storage_x-pender"].append(bin)
    if bin["item_name"] == "Hologram": bit_shop_bins["hologram"].append(bin)
    if bin["item_name"] == "Builder's Wand": bit_shop_bins["builder's_wand"].append(bin)
    if bin["item_name"] == "Block Zapper": bit_shop_bins["block_zapper"].append(bin)
    if bin["item_name"] == "Bits Talisman": bit_shop_bins["bits_talisman"].append(bin)
    if bin["item_name"] == "Autopet Rules 2-Pack": bit_shop_bins["autopet_rules_2-pack"].append(bin)
    if bin["item_name"] == "Kismet Feather": bit_shop_bins["kismet_feather"].append(bin)

bin_values: dict = {
    "god_potion": [bin["starting_bid"] for bin in bit_shop_bins["god_potion"]],
    "kat_flower": [bin["starting_bid"] for bin in bit_shop_bins["kat_flower"]],
    "heat_core": [bin["starting_bid"] for bin in bit_shop_bins["heat_core"]],
    "hyper_catalyst_upgrade": [bin["starting_bid"] for bin in bit_shop_bins["hyper_catalyst_upgrade"]],
    "ultimate_carrot_candy_upgrade": [bin["starting_bid"] for bin in bit_shop_bins["ultimate_carrot_candy_upgrade"]],
    "colossal_experience_bottle_upgrade": [bin["starting_bid"] for bin in bit_shop_bins["colossal_experience_bottle_upgrade"]],
    "jumbo_backpack_upgrade": [bin["starting_bid"] for bin in bit_shop_bins["jumbo_backpack_upgrade"]],
    "minion_storage_x-pender": [bin["starting_bid"] for bin in bit_shop_bins["minion_storage_x-pender"]],
    "hologram": [bin["starting_bid"] for bin in bit_shop_bins["hologram"]],
    "builder's_wand": [bin["starting_bid"] for bin in bit_shop_bins["builder's_wand"]],
    "block_zapper": [bin["starting_bid"] for bin in bit_shop_bins["block_zapper"]],
    "bits_talisman": [bin["starting_bid"] for bin in bit_shop_bins["bits_talisman"]],
    "autopet_rules_2-pack": [bin["starting_bid"] for bin in bit_shop_bins["autopet_rules_2-pack"]],
    "kismet_feather": [bin["starting_bid"] for bin in bit_shop_bins["kismet_feather"]]
}

lowest_bins: dict = {
    "god_potion": min(bin_values["god_potion"]),
    "kat_flower": min(bin_values["kat_flower"]),
    "heat_core": min(bin_values["heat_core"]),
    "hyper_catalyst_upgrade": min(bin_values["hyper_catalyst_upgrade"]),
    "ultimate_carrot_candy_upgrade": min(bin_values["ultimate_carrot_candy_upgrade"]),
    "colossal_experience_bottle_upgrade": min(bin_values["colossal_experience_bottle_upgrade"]),
    "jumbo_backpack_upgrade": min(bin_values["jumbo_backpack_upgrade"]),
    "minion_storage_x-pender": min(bin_values["minion_storage_x-pender"]),
    "hologram": min(bin_values["hologram"]),
    "builder's_wand": min(bin_values["builder's_wand"]),
    "block_zapper": min(bin_values["block_zapper"]),
    "bits_talisman": min(bin_values["bits_talisman"]),
    "autopet_rules_2-pack": min(bin_values["autopet_rules_2-pack"]),
    "kismet_feather": min(bin_values["kismet_feather"])
}

prices_in_bits: dict = {
    "god_potion": 1500,
    "kat_flower": 500,
    "heat_core": 3000,
    "hyper_catalyst_upgrade": 300,
    "ultimate_carrot_candy_upgrade": 8000,
    "colossal_experience_bottle_upgrade": 1200,
    "jumbo_backpack_upgrade": 4000,
    "minion_storage_x-pender": 1500,
    "hologram": 2000,
    "builder's_wand": 12000,
    "block_zapper": 5000,
    "bits_talisman": 15000,
    "autopet_rules_2-pack": 21000,
    "kismet_feather": 1350
}

prices_in_coins: dict = {
    "god_potion": bits_in_cookie * lowest_bins["god_potion"] / prices_in_bits["god_potion"],
    "kat_flower": bits_in_cookie * lowest_bins["kat_flower"] / prices_in_bits["kat_flower"],
    "heat_core": bits_in_cookie * lowest_bins["heat_core"] / prices_in_bits["heat_core"],
    "hyper_catalyst_upgrade": bits_in_cookie * lowest_bins["hyper_catalyst_upgrade"] / prices_in_bits["hyper_catalyst_upgrade"],
    "ultimate_carrot_candy_upgrade": bits_in_cookie * lowest_bins["ultimate_carrot_candy_upgrade"] / prices_in_bits["ultimate_carrot_candy_upgrade"],
    "colossal_experience_bottle_upgrade": bits_in_cookie * lowest_bins["colossal_experience_bottle_upgrade"] / prices_in_bits["colossal_experience_bottle_upgrade"],
    "jumbo_backpack_upgrade": bits_in_cookie * lowest_bins["jumbo_backpack_upgrade"] / prices_in_bits["jumbo_backpack_upgrade"],
    "minion_storage_x-pender": bits_in_cookie * lowest_bins["minion_storage_x-pender"] / prices_in_bits["minion_storage_x-pender"],
    "hologram": bits_in_cookie * lowest_bins["hologram"] / prices_in_bits["hologram"],
    "builder's_wand": bits_in_cookie * lowest_bins["builder's_wand"] / prices_in_bits["builder's_wand"],
    "block_zapper": bits_in_cookie * lowest_bins["block_zapper"] / prices_in_bits["block_zapper"],
    "bits_talisman": bits_in_cookie * lowest_bins["bits_talisman"] / prices_in_bits["bits_talisman"],
    "autopet_rules_2-pack": bits_in_cookie * lowest_bins["autopet_rules_2-pack"] / prices_in_bits["autopet_rules_2-pack"],
    "kismet_feather": bits_in_cookie * lowest_bins["kismet_feather"] / prices_in_bits["kismet_feather"]
}

profit: dict = {
    "god_potion": prices_in_coins["god_potion"] - cookie_sell_price,
    "kat_flower": prices_in_coins["kat_flower"] - cookie_sell_price,
    "heat_core": prices_in_coins["heat_core"] - cookie_sell_price,
    "hyper_catalyst_upgrade": prices_in_coins["hyper_catalyst_upgrade"] - cookie_sell_price,
    "ultimate_carrot_candy_upgrade": prices_in_coins["ultimate_carrot_candy_upgrade"] - cookie_sell_price,
    "colossal_experience_bottle_upgrade": prices_in_coins["colossal_experience_bottle_upgrade"] - cookie_sell_price,
    "jumbo_backpack_upgrade": prices_in_coins["jumbo_backpack_upgrade"] - cookie_sell_price,
    "minion_storage_x-pender": prices_in_coins["minion_storage_x-pender"] - cookie_sell_price,
    "hologram": prices_in_coins["hologram"] - cookie_sell_price,
    "builder's_wand": prices_in_coins["builder's_wand"] - cookie_sell_price,
    "block_zapper": prices_in_coins["block_zapper"] - cookie_sell_price,
    "bits_talisman": prices_in_coins["bits_talisman"] - cookie_sell_price,
    "autopet_rules_2-pack": prices_in_coins["autopet_rules_2-pack"] - cookie_sell_price,
    "kismet_feather": prices_in_coins["kismet_feather"] - cookie_sell_price
}

print(dict(sorted(profit.items(), key=lambda item: item[1], reverse=True)))
best_item = max(profit, key=profit.get)
print(f"The best item to sell right now is {best_item}, with a profit of {profit[best_item]} per cookie.")