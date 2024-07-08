import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Function to speak the entered text
def speak():
    text = text_entry.get("1.0", "end-1c")
    engine.say(text)
    engine.runAndWait()

# Function to save speech as audio file
def save_as_audio():
    text = text_entry.get("1.0", "end-1c")
    file_path = "output.mp3"  # Example: Use file dialog for user to choose file path
    engine.save_to_file(text, file_path)
    engine.runAndWait()

# Function to change the selected voice
def change_voice(event):
    selected_voice = voice_dropdown.get()
    for voice in voices:
        if voice.name == selected_voice:
            engine.setProperty('voice', voice.id)
            break

# Function to set volume based on slider
def set_volume(val):
    volume = int(val) / 100  # Convert scale value (0-100) to float (0.0-1.0)
    engine.setProperty('volume', volume)

# Function to set speech rate based on slider
def set_rate(val):
    rate = int(val)
    engine.setProperty('rate', rate)

# Function to show error messages
def show_error(message):
    messagebox.showerror("Error", message)

# Create main application window
root = tk.Tk()
root.title("Text-to-Speech Application")

# Text Entry
text_label = tk.Label(root, text="Enter text:")
text_label.grid(row=0, column=0, padx=10, pady=10)

text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

# Voice Selection
language_label = tk.Label(root, text="Select Voice:")
language_label.grid(row=1, column=0, padx=10, pady=10)

voices_list = [voice.name for voice in voices]
voice_var = tk.StringVar(root)
voice_dropdown = ttk.Combobox(root, textvariable=voice_var, values=voices_list, state='readonly')
voice_dropdown.grid(row=1, column=1, padx=10, pady=10)
voice_dropdown.current(0)  # Default selection

voice_dropdown.bind("<<ComboboxSelected>>", change_voice)

# Speech Parameters
rate_label = tk.Label(root, text="Rate:")
rate_label.grid(row=2, column=0, padx=10, pady=10)

rate_slider = tk.Scale(root, from_=50, to=200, orient=tk.HORIZONTAL, command=set_rate)
rate_slider.grid(row=2, column=1, padx=10, pady=10)
rate_slider.set(100)  # Default rate

volume_label = tk.Label(root, text="Volume:")
volume_label.grid(row=2, column=2, padx=10, pady=10)

volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_slider.grid(row=2, column=3, padx=10, pady=10)
volume_slider.set(50)  # Default volume

# Buttons
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.grid(row=3, column=0, padx=10, pady=10)

save_button = tk.Button(root, text="Save as Audio", command=save_as_audio)
save_button.grid(row=3, column=1, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=3, column=2, padx=10, pady=10)


root.mainloop()
