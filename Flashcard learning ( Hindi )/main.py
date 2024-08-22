from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE = "data/Hindi_english_words.csv"
WORDS_LEARNED = "data/words_learned.csv"
WORDS_TO_LEARN = "data/words_to_learn.csv"

try:
    data = pd.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    data = pd.read_csv(DATA_FILE)

data_dictionary = data.to_dict("records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    if not data_dictionary:  # Check if there are no words left
        canvas.itemconfig(canvas_img, image=card_front)
        canvas.itemconfig(card_title, text="Completed", fill="black")
        canvas.itemconfig(card_word, text="", fill="black")
    else:
        current_card = random.choice(data_dictionary)
        canvas.itemconfig(canvas_img, image=card_front)
        canvas.itemconfig(card_title, text="Hindi", fill="black")
        canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
        flip_timer = window.after(3000, func=flipping)


def flipping():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def words_learned():
    # Wrap the current_card dictionary in a list to create a DataFrame with a single row.
    learned_words = pd.DataFrame([current_card])

    # Check if the CSV file for learned words already exists.
    file_exists = os.path.isfile(WORDS_LEARNED)

    # Append the current learned word to the CSV file. If the file doesn't exist, create it.
    # The 'header=not file_exists' ensures the header is written only when the file is created.
    learned_words.to_csv(WORDS_LEARNED, mode='a', header=not file_exists, index=False)

    # Remove the current card from the data_dictionary, so it doesn't appear again.
    data_dictionary.remove(current_card)

    # Convert the updated data_dictionary to a DataFrame (words yet to learn).
    words_to_learn = pd.DataFrame(data_dictionary)

    # Save the updated words_to_learn list to a CSV file, overwriting the previous one.
    # so that the already known words won't appear again
    words_to_learn.to_csv(WORDS_TO_LEARN, index=False)

    next_card()


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.resizable(False, False)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

flip_timer = window.after(3000, func=flipping)

correct_img = PhotoImage(file="images/right.png")
button_correct = Button(image=correct_img, highlightthickness=0, relief=FLAT, command=words_learned)
button_correct.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, relief=FLAT, command=next_card)
button_wrong.grid(row=1, column=1)

next_card()

window.mainloop()

