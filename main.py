import tkinter as tk
import pyautogui

def update_mouse_position():
    x, y = pyautogui.position()
    mouse_position_label.config(text=f"Current mouse position: ({x}, {y})")
    root.after(100, update_mouse_position)

root = tk.Tk()
root.title("position")

mouse_position_label = tk.Label(root, text="Current mouse position: (0, 0)")
mouse_position_label.pack()

update_mouse_position()

root.mainloop()
