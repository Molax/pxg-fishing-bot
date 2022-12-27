from time import sleep
import winsound
import pyautogui
import keyboard
import button

COUNTER=0

def atack_scizor():
  keyboard.press(button.key['F1'])
  sleep(0.4)
  keyboard.press(button.key['F2'])
  sleep(0.5)
  keyboard.press(button.key['F3'])

def atack_nine():
  keyboard.press(button.key['F4'])
  keyboard.press(button.key['F5'])
  keyboard.press(button.key['F6'])
  keyboard.press(button.key['F8'])
  keyboard.press(button.key['F9'])

def pesca():
  keyboard.press(button.key['CAPS'])

def saque():
  keyboard.press(button.key['F12'])

def pokebola(pokemon):
  keyboard.press(button.key['NUNLOCK'])
  position_x, position_y = pyautogui.center(pokemon)
  pyautogui.moveTo(position_x, position_y, 0.5)
  sleep(1)
  pyautogui.click()

while True:
  if COUNTER == 0:
    COUNTER = 1
    print('bot is running')
  bolhas = pyautogui.locateOnScreen("bolhas.PNG", confidence=0.75 , region=(1451,587,102,100))
  if bolhas != None:
    print('bot found fishing')
    x_bolhas, y_bolhas = pyautogui.center(bolhas)
    pyautogui.moveTo(x_bolhas, y_bolhas, 0.2)
    pyautogui.click()
    pesca()

    sleep(1)
    atack_scizor()
    # saque()
    print('bot finished fishing, setting rod again, fishing counter: ',COUNTER)
    pyautogui.moveTo(x_bolhas, y_bolhas, 0.5)
    pyautogui.click()
    pesca()
    pyautogui.click()
    COUNTER=COUNTER+1
  # tenta = pyautogui.locateOnScreen("tenta.PNG", confidence=0.75)
  # if tenta != None:
  #   pokebola(tenta)
  #   winsound.Beep(440, 500)