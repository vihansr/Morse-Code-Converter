import tkinter as tk

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}


def morse_converter():
    morse = ''
    user_entry = entry.get()
    for alphabet in user_entry.upper():
        for letter in morse_code_dict:
            if alphabet == letter:
                morse += morse_code_dict[letter]
    result_label.config(text=f"Your Morse Code is : {morse}")


# Create main window
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# Title Label
title_label = tk.Label(root, text="Morse Code Converter", font=("Arial", 16, "bold"), bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=10)

# Input Box
entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief=tk.GROOVE)
entry.pack(pady=10)

# Convert Button
submit_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", padx=10, pady=5,command=morse_converter)
submit_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#2C3E50", fg="#F1C40F")
result_label.pack(pady=10)

root.mainloop()
