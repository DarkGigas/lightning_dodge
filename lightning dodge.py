import mss
import numpy as np
import pydirectinput
import time

monitor_index = 1

region = {'top': 500, 'left': 800, 'width': 300, 'height': 200}

flash_threshold = 120
press_delay = 0.05
cooldown_time = 0.5
last_flash_time = 0

print("Available monitors:")
with mss.mss() as sct:
    for i, monitor in enumerate(sct.monitors):
        print(f"Monitor {i}: {monitor}")

    monitor = sct.monitors[monitor_index]
    region['left'] += monitor['left']
    region['top'] += monitor['top']

    print(f"\nCapturing from Monitor {monitor_index} in region {region}")
    print("Watching for lightning flashes...")

    while True:
        screenshot = np.array(sct.grab(region))[:, :, :3]
        brightness = np.mean(screenshot)
        
        if brightness > flash_threshold:
            current_time = time.time()
            if current_time - last_flash_time > cooldown_time:
                print(f"⚡ Lightning detected! Waiting {press_delay} seconds before pressing the key...") # noqa
                time.sleep(press_delay)
                
                # Send the 'C' key using pyDirectInput
                pydirectinput.press('c')  # pyDirectInput handles DirectInput
                print(f"🎮 'C' key pressed!")
                
                last_flash_time = current_time

        time.sleep(0.01)
