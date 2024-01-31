from pynput.keyboard import Listener, Key, Controller
import pyautogui
import yaml
import pystray
import PIL.Image
import sys


def setup():
    """ Reads the configuration YAML file and returns the list of matches. """
    try:
        with open('config/config.yaml', 'r') as f:
            configuration = yaml.safe_load(f)
        return configuration.get('matches')
    except FileNotFoundError:
        print("Configuration file not found!")
        return None


def collect_trigger():
    """ Finds the last occurence of the semi-colon character and collects the word that follows it.
        If this word is within the matches from the YAML file then it will replace what the user typed. """
    
    start_index = len(keylog) - 1 - keylog[::-1].index(';')
    trigger_word = ''.join(keylog[start_index::])
    for word in configuration:
        if word['trigger'] == trigger_word:
            replace_value = ''.join(word.get('replace'))
            pyautogui.press('backspace', presses=len(trigger_word)+1)
            pyautogui.write(replace_value)

            # Clear list for next entry
            keylog.clear()


def on_press(key):
    """ Collects all the words that are typed but specifically looking for a semi-colon character and space bar
        entry to trigger the collect_trigger function. We want to try and keep the keylog as short as possible and clear it after
        each time we collect a word and replace it. """

    try:
        if len(keylog) > 0 and keylog[0] == ';' and key == Key.space:
            collect_trigger()
        elif key == Key.backspace:
            if len(keylog) > 0:  # Remove the last character from keylog list
                keylog.pop()
        elif key.char == ';':
            keylog.append(key.char)
        elif len(keylog) > 0 and keylog[0] == ';':
            keylog.append(key.char)
    except AttributeError:
        pass


def exit_program(icon, item):
    """ Exits the program and stops the icon from running. """
    icon.stop()
    sys.exit()


def create_system_tray_icon():
    """ Tray icon is created with an Exit button to easily get out of the program. """

    image = PIL.Image.open("config/icon.png")
    tray = pystray.Icon("Tray", image, menu=pystray.Menu(
        pystray.MenuItem("Exit", exit_program)))
    return tray


if __name__ == '__main__':
    configuration = setup()
    keylog = []
    tray = create_system_tray_icon()

    with Listener(on_press=on_press) as listener:
        tray.run()
        listener.join()
