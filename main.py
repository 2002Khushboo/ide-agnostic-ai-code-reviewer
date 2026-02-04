import pyperclip
import keyboard
import threading
import time

from ui import FloatingWindow
from ai_client import get_ai_suggestion

window = FloatingWindow()

def looks_like_c_code(code: str) -> bool:
    c_keywords = [";", "{", "}", "HAL_", "uint", "#include"]
    return any(k in code for k in c_keywords)

def analyze_clipboard():
    keyboard.send("ctrl+c")
    time.sleep(0.1)
    code = pyperclip.paste()

    print("===== CLIPBOARD START =====")
    print(code)
    print("===== CLIPBOARD END =====")

    if not looks_like_c_code(code):
        window.show_message(
            "Clipboard does not look like embedded C code.\n\n"
            "Please copy C code and try again."
        )
        return
    
    result = get_ai_suggestion(code)

    # Schedule UI update safely in Tkinter thread
    window.root.after(0, window.show_message, result)

def start_hotkey_listener():
    keyboard.add_hotkey("ctrl+shift+a", analyze_clipboard)
    keyboard.wait()  # keeps listener alive

# Run keyboard listener in background thread
threading.Thread(target=start_hotkey_listener, daemon=True).start()

# Start UI loop (must be on main thread)
window.run()
