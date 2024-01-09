import ctypes
from win10toast import ToastNotifier
import time

def check_caps_lock():
    """Check the state of the Caps Lock key."""
    # Get the state of the Caps Lock key (Bit 0 is set if Caps Lock is ON)
    return ctypes.windll.user32.GetKeyState(0x14) & 1 == 1

def main():
    toaster = ToastNotifier()
    last_state = check_caps_lock()  # Initial state
    
    while True:
        current_state = check_caps_lock()
        
        # Check if the state has changed
        if current_state != last_state:
            if current_state:  # Caps Lock is ON
                toaster.show_toast("Caps Lock", "Caps Lock is ON", duration=1)
            else:  # Caps Lock is OFF
                toaster.show_toast("Caps Lock", "Caps Lock is OFF", duration=1)
            
            # Update the last state
            last_state = current_state
        
        # Sleep for a short duration to prevent CPU hogging
        time.sleep(0.5)

if __name__ == "__main__":
    main()
