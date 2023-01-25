import tkinter as tk
import speech_recognition as sr
import pyttsx3
import kanat
import kanatinit



root = tk.Tk()
root.title("Voice Assistant")
root.geometry("300x100")

def closeWindow():
    root.destroy()

# Create a top panel
top_panel = tk.Frame(root, bg='white', width=400, height=50)
top_panel.pack(side=tk.TOP, fill=tk.X)

# Create a label in top panel
label = tk.Label(top_panel, text="Voice Assistant", font=("Arial", 16), fg='black', bg='white')
label.pack(padx=10, pady=10)

# Create a button
button = tk.Button(root, text="Listen", command=kanat.on_submit)
button.pack(padx=10, pady=10)

kanat.speak("Hello, how can I help you?")
print("Hello, how can I help you?")
root.mainloop()