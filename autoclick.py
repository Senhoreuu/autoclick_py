import time 
import threading 
from pynput.mouse import Button, Controller 
from pynput.keyboard import Listener, KeyCode 
  
delay = 0.001
button = Button.left
start_key = 'Key.f2'  # Tecla F2 para iniciar
stop_key = 'Key.f4'   # Tecla F4 para parar

class ClickMouse(threading.Thread): 
    def __init__(self, delay, button): 
        super(ClickMouse, self).__init__() 
        self.delay = delay 
        self.button = button 
        self.running = False
        self.program_running = True
  
    def start_clicking(self): 
        self.running = True
  
    def stop_clicking(self): 
        self.running = False
  
    def exit(self): 
        self.stop_clicking() 
  
    def run(self): 
        while self.program_running: 
            while self.running: 
                mouse.click(self.button) 
                time.sleep(self.delay) 
            time.sleep(0.1) 
  
  
mouse = Controller() 
click_thread = ClickMouse(delay, button) 
click_thread.start() 
  
def on_press(key):
    global click_thread
    
    if str(key) == start_key:
        print('Click started')
        click_thread.start_clicking() 
    elif str(key) == stop_key:
        print('Click stopped')
        click_thread.exit() 
  
with Listener(on_press=on_press) as listener: 
    listener.join()
