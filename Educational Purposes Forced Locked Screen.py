import tkinter as tk
import ctypes
import os
import sys
import time
import threading

#Disable Windows Key and Block Taskbar
def block_windows_key():
    ctypes.windll.user32.RegisterHotKey(None, 1, 0, 0x5B)  # Disable Left Windows key
    ctypes.windll.user32.RegisterHotKey(None, 2, 0, 0x5C)  # Disable Right Windows key

#Disable Task Manager, Ctrl+Alt+Delete, and shortcuts to get out
def disable_system_shortcuts():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, 0, 0)  # Disable Taskbar
    ctypes.windll.user32.RegisterHotKey(None, 3, 0, 0x11)  # Disable Ctrl
    ctypes.windll.user32.RegisterHotKey(None, 4, 0, 0x1B)  # Disable Escape
    ctypes.windll.user32.RegisterHotKey(None, 5, 0, 0x2F)  # Disable F1-F12
    ctypes.windll.user32.RegisterHotKey(None, 6, 0, 0x2E)  # Disable Delete key

#Block input and stop access to shutdown and restart
def block_shutdown():
    ctypes.windll.user32.BlockInput(True)  # Disable mouse and keyboard interaction with the system

#locked screen
def create_locked_screen():
    root = tk.Tk()
    root.title("Locked Screen")

    #make it fullscreen
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    label = tk.Label(root, text="Enter password to unlock.\nTo get password call- jk type 'hackaclub' ", fg="white", bg="black", font=("Arial", 40))
    label.pack(pady=100)

    password_entry = tk.Entry(root, show="*", font=("Arial", 30))
    password_entry.pack(pady=20)

    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(root, password_entry), font=("Arial", 30))
    submit_button.pack(pady=20)

    return root, password_entry

#check the password entered
def check_password(password_entry):
    input_password = password_entry.get()
    return input_password == "hackaclub"

#submit password function
def on_submit(root, password_entry):
    if check_password(password_entry):
        root.quit()  # Close the locked screen if the password is correct

#disable closing the window
def disable_closing(root):
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button

#lock screen and block taskbar, windows key, shutdown and restart
def lock_screen():
    block_windows_key()  # Disable Windows key
    block_shutdown()  # Disable shutdown/restart
    disable_system_shortcuts()  # Disable system shortcuts (Ctrl+Alt+Delete)
    root, password_entry = create_locked_screen()
    disable_closing(root)
    root.mainloop()

#run the program
def main():
    lock_screen()

main()
