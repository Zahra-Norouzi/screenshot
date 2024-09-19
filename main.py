from PIL import ImageGrab
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  
path = filedialog.asksaveasfilename(title="Choose a save location", 
                                    defaultextension=".png",
                                    filetypes=[("PNG Image", "*.png")])
if path:
    screenshot = ImageGrab.grab()
    screenshot.save(path)
    screenshot.close()
else:
    print("Operation cancelled")
