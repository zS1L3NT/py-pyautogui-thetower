from constants import *
import pyautogui as ui

def switch_to_game():
    ui.keyDown("command")
    ui.press("tab")
    coords = ui.locate(
        "app.png",
        ui.screenshot(region=(0, SCREEN_CENTER_Y - 90, SCREEN_WIDTH, 180)),
        grayscale=True,
        confidence=0.8,
    )
    ui.leftClick(coords.left + coords.width / 2, SCREEN_CENTER_Y)
    ui.keyUp("command")

def center_game():
    ui.keyDown("command")   
    ui.press("space")
    ui.keyUp("command")
    ui.typewrite("center")
    ui.press("enter")