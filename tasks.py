from robocorp.tasks import task
from robocorp import windows
import json

# Opens JSON file that contains locators
with open('locators.json','r') as file:
    data = json.load(file)

desktop = windows.Desktop()

@task
def desktop_automation():
    """ Original Hello World Code: Using RPA.Desktop"""

    """ Using robocop-windows"""
    desktop.windows_run("notepad.exe")

    notepad = windows.find_window(data["subname"], wait_time=1)
    notepad.send_keys('{CTRL}a{DELETE}', wait_time= 1)  # Deletes any current text in the editor, before sending text to it
    notepad.send_keys(f'{data["message"]}')     # Sends new message to the text editor
    # notepad.find(f'{data["name"]}').click()     # Clicks 'File' 
    notepad.screenshot('test-run.png')

    # Closes Notepad application
    notepad.close_window()
