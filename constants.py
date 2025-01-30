import pyautogui as ui

DIRECTORY = __file__.replace("/constants.py", "")

SCREEN_WIDTH, SCREEN_HEIGHT = ui.size()
SCREEN_CENTER_X = int(SCREEN_WIDTH / 2)
SCREEN_CENTER_Y = int(SCREEN_HEIGHT / 2)
SCREEN_CENTER = (SCREEN_CENTER_X, SCREEN_CENTER_Y)

GAME_WIDTH = 788
GAME_HEIGHT = 1052
GAME_X = SCREEN_CENTER_X - 392
GAME_Y = SCREEN_CENTER_Y - 490
GAME_CENTER_X = int(GAME_WIDTH / 2)
GAME_CENTER_Y = int(GAME_HEIGHT / 2)
GAME_REGION = (GAME_X, GAME_Y, GAME_WIDTH, GAME_HEIGHT)

CATEGORIES = ("Attack", "Defence", "Utility")
UPGRADES = (
    (
        "Damage",
        "Attack Speed",
        "Critical Chance",
        "Critical Factor",
        "Range",
        "Damage Per Meter",
        "Multishot Chance",
        "Multishot Targets",
        "Rapid Fire Chance",
        "Rapid Fire Duration",
        "Bounce Shot Chance",
        "Bounce Shot Targets",
        "Bounce Shot Range",
    ),
    (
        "Health",
        "Health Regen",
        "Defence Percentage",
        "Defence Absolute",
        "Thorn Damage",
        "Lifesteal",
        "Knockback Chance",
        "Knockback Force",
        "Orb Speed",
        "Orbs",
        "Shockwave Size",
        "Shockwave Frequency",
        "Land Mine Chance",
        "Land Mine Damage",
        "Land Mine Radius",
    ),
    (
        "Cash Bonus",
        "Cash Per Wave",
        "Coins Per Kill Bonus",
        "Coins Per Wave",
        "Free Attack Upgrade",
        "Free Defence Upgrade",
        "Free Utility Upgrade",
        "Interest Per Wave",
        "Recovery Amount",
        "Max Recovery",
        "Package Chance",
    )
)
