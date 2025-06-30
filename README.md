# 📚 FlashcardApp — Learn Faster, Remember Longer

A simple yet powerful flashcard application built with Python and Tkinter to help you learn any language or vocabulary efficiently. This app mimics physical flashcards and adapts as you learn by tracking which words you've mastered and which you still need to review.

---

## 🖼️ Preview

> *\[Include a small demo GIF or screenshots here if available — showing a word flipping to its meaning after a few seconds, with buttons for correct/incorrect answers.]*

---

## 🚀 Features

* ⏱️ Automatically flips the card after a short delay to show the meaning.
* ✅ Tracks your progress — learned words are saved and won't appear again.
* 📁 Works with **any language or vocabulary CSV** (just two columns).
* 💾 Saves both **words you've learned** and **words still to learn**.
* 🖼️ Clean UI with visual feedback using card images and icons.

---

## 📁 Project Structure

```
FlashcardApp/
│
├── data/
│   ├── desired_language_words.csv        # Your source word list (rename as needed)
│   ├── words_learned.csv                 # Created during runtime
│   └── words_to_learn.csv                # Created during runtime
│
├── images/
│   ├── card_front.png                    # Flashcard front image
│   ├── card_back.png                     # Flashcard back image
│   ├── right.png                         # Tick/check icon
│   └── wrong.png                         # Cross icon
│
└── main.py                               # Main Python script
```

---

## 📄 Data Format

Your word list should be in a CSV file (like `Sanskrit.csv`) with **exactly two columns**:

```
Word,Meaning
नमस्ते,Hello
पुस्तक,Book
...
```

* The **first column** is shown first.
* After a short delay, the card **flips to reveal the second column**.

---

## 🔧 How to Run

1. **Clone the repository** or download the files.

2. Make sure you have **Python 3.x** installed.

3. Install **pandas** if not already:

   ```bash
   pip install pandas
   ```

4. Place your `desired_language_words.csv` file inside the `data/` folder.

   * Rename it to `Sanskrit.csv` or change the filename in `main.py`.

5. Run the app:

   ```bash
   python main.py
   ```

---

## 🎯 How It Works

* The app loads words from `words_to_learn.csv` if it exists; else, it falls back to the original data file.
* Each flashcard:

  * Shows the word (front side).
  * After 3 seconds, flips to show the meaning (back side).
* If you click ✅ (Right), the word is saved to `words_learned.csv` and removed from the learning pool.
* If you click ❌ (Wrong), it stays in the pool for future review.
* Once you learn all words, it shows a **"Completed"** message.

---

## 💡 Customize It

You can customize:

* **CSV Filename**: Change `DATA_FILE` in `main.py`.
* **Images**: Replace any image inside `/images` with your own designs.
* **Flip Delay**: Change the `3000` ms value to something faster/slower in:

  ```python
  flip_timer = window.after(3000, func=flipping)
  ```

---

## 🧠 Ideal For

* Language learners (Sanskrit, Hindi, Japanese, etc.)
* Vocabulary building
* Educational games
* Personal spaced repetition tools

---

## 📌 Dependencies

* `tkinter` (comes with Python)
* `pandas`

---

Built by Hari with ❤️ for learners.
