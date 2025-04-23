# Import libraries for GUI, hashing, regex, math, API requests, logging, and password generation
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import hashlib
import re
import math
import requests
import logging
import random
import string

# Configure logging to store events in a file named 'password_checker.log'
logging.basicConfig(filename="password_checker.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Calculate password entropy based on character diversity and length
def calculate_entropy(password):
    character_sets = [
        (r"[a-z]", 26),  # Lowercase letters
        (r"[A-Z]", 26),  # Uppercase letters
        (r"[0-9]", 10),  # Digits
        (r"[^a-zA-Z0-9]", 32)  # Special characters
    ]
    pool_size = sum(charset[1] for charset in character_sets if re.search(charset[0], password))
    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    return entropy

# Estimates the time it would take to crack the password using brute force
def estimate_password_crack_time(entropy):
    guesses_per_second = 1e10  # Approximate speed of modern GPU cracking
    seconds = 2 ** entropy / guesses_per_second # Estimate total time needed in seconds
    # Convert time from seconds to more readable time like years, days, hours, minutes, and seconds
    time_units = [("seconds", 60), ("minutes", 60), ("hours", 24), ("days", 365), ("years", 100)]
    for unit, factor in time_units:
        if seconds < factor:
            return f"Estimated crack time: {seconds:.2f} {unit}"
        seconds /= factor
    return f"Estimated crack time: {seconds:.2f} centuries"

# Uses Have I Been Pwned API to check if password has appeared in known breaches
def check_breached_password(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    try:
        # Sends the first 5 characters of the hash to the API
        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        # Checks if the suffix exists in the response
        if suffix in response.text:
            return "Warning: This password has been found in a data breach!"
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return "Error: Unable to check breached passwords."
    return "This password has not been found in known breaches."

# Evaluates the password strength by using entropy and breach status
def evaluate_password(password):
    entropy = calculate_entropy(password)
    crack_time = estimate_password_crack_time(entropy)
    breach_status = check_breached_password(password)

    # Decide how strong the password is based on entropy value
    if entropy > 80:
        strength = "Very Strong"
    elif entropy > 60:
        strength = "Strong"
    elif entropy > 40:
        strength = "Moderate"
    elif entropy > 25:
        strength = "Weak"
    else:
        strength = "Very Weak"
    return f"Password Strength: {strength}\n{crack_time}\n{breach_status}"

# Generates a strong random password using a mix of characters
def generate_strong_password():
    length = random.randint(12, 16)  # Random length between 12 and 16
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(characters, length)) # Randomly generate a password with unique characters
    return password

# Updates the feedback dynamically as user types
def update_feedback():
    password = entry.get()
    if password:
        feedback = evaluate_password(password)
        feedback_label.configure(text=feedback)
    else:
        feedback_label.configure(text="Enter a password to check its strength.")

# Displays an "About" popup with program description
def show_about():
    about_window = ttk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("400x200")
    ttk.Label(
        about_window, 
        text="Password Strength Checker\n\nThis tool evaluates password strength "
             "based on entropy, length, and diversity, providing practical feedback "
             "to improve security.",
        font=("Helvetica", 10),
        wraplength=380,
        justify="center"
    ).pack(pady=10)
    ttk.Button(about_window, text="Close", command=about_window.destroy, bootstyle=SECONDARY).pack(pady=10)

# Displays a generated password in a new window with copy feature
def show_generated_password():
    generated_password = generate_strong_password()
    password_window = ttk.Toplevel(root)
    password_window.title("Generated Password")
    password_window.geometry("400x200")

    # Display the generated password
    ttk.Label(password_window, text="Your Strong Password:", font=("Helvetica", 12, "bold")).pack(pady=10)
    password_label = ttk.Label(password_window, text=generated_password, font=("Helvetica", 12), foreground="green")
    password_label.pack(pady=5)

    # Copy generated password to clipboard
    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()
        logging.info("Password copied to clipboard.")

    # Add "Copy" button to copy password
    ttk.Button(password_window, text="Copy", command=copy_to_clipboard, bootstyle=SUCCESS).pack(pady=5)

    # Close button for the window
    ttk.Button(password_window, text="Close", command=password_window.destroy, bootstyle=SECONDARY).pack(pady=10)

# Set up and launch the main GUI window
def setup_gui():
    global root, entry, feedback_label
    root = ttk.Window(title="Password Strength Checker", themename="darkly", size=(600, 400))
    root.resizable(True, True) 

    # Application title and instructions
    ttk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold")).pack(pady=15)
    ttk.Label(
        root,
        text="Enter a password to check its strength. "
             "We evaluate length, character diversity, and patterns.",
        font=("Helvetica", 10),
        wraplength=450,
        justify="center"
    ).pack(pady=5)

    # Input field for password
    ttk.Label(root, text="Enter your password:", font=("Helvetica", 12)).pack(pady=5)
    entry = ttk.Entry(root, show="*", width=35)
    entry.pack(pady=5)
    entry.bind("<KeyRelease>", lambda event: update_feedback())

    # Label to dislay feedback
    feedback_label = ttk.Label(root, text="", font=("Helvetica", 10), wraplength=450, justify="left")
    feedback_label.pack(pady=10)

    # Buttons for password generation and program info
    ttk.Button(root, text="Generate Strong Password", command=show_generated_password, bootstyle=SUCCESS).pack(pady=5)
    ttk.Button(root, text="About", command=show_about, bootstyle=INFO).pack(pady=5)

    root.mainloop()

# Start the application
if __name__ == "__main__":
    setup_gui()
