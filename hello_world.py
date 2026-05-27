import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello World")
window.geometry("300x100")
window.tk_setPalette(background="red")  # Set the theme to 'clam' for a modern look

# Add a label with the message
label = tk.Label(window, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Start the GUI event loop
window.mainloop()