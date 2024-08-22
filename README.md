### **Flashcard Learning App**

## **Project Overview**

This project is a **Flashcard Learning Application** designed to help users learn words in a desired language along with their English translations. The application displays words in the desired language on flashcards, which the user attempts to translate within a time limit. After the time expires, the card flips to show the English translation. The user can mark words as "learned," and these words are saved and removed from the deck to avoid repetition.

## **Prerequisites**

Before running the project, ensure that you have the following installed:
- **Python 3.x**: The programming language used for this project.
- **Tkinter**: Python's standard GUI package.
- **Pandas**: A library used for data manipulation and analysis.

To install Pandas, use:
```bash
pip install pandas
```

## **Project Setup**

### **1. Project Directory Structure**

The project should have the following directory structure:
```
FlashcardApp/
│
├── data/
│   ├── desired_language_words.csv
│   ├── words_learned.csv (This file is created during runtime)
│   └── words_to_learn.csv (This file is created during runtime)
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
├── main.py
└── README.md
```

### **2. Data Files**

- **`desired_language_english_words.csv`**: This file contains words in the desired language and their English translations. Ensure it is placed inside the `data/` directory.
- **`words_learned.csv`** and **`words_to_learn.csv`**: These files will be automatically generated during runtime. They track the user's progress by storing learned words and the remaining words to learn.

## **How to Run the Project**

### **1. Running the Application**

1. Ensure that all prerequisites are installed and that the directory structure is correctly set up.
2. Navigate to the project directory using the terminal.
3. Run the application using the following command:
    ```bash
    python main.py
    ```
4. The application window will open, displaying a flashcard with a word in the desired language.

### **2. Using the Application**

- **Flipping the Card**: The card will automatically flip after 3 seconds, revealing the English translation.
- **Correct Button**: Clicking this button saves the word as "learned" and store it to a words_learned.csv file and shows the next card.
- **Wrong Button**: Clicking this button skips the word and store it to a words_to_learn.csv and shows the next card.


## **Troubleshooting**

### **1. Common Issues**
- **FileNotFoundError**: Ensure that the `desired_language_english_words.csv` file is in the correct directory.
- **GUI Not Displaying**: Check the images' paths and ensure they are in the `images/` directory.

### **2. Logs and Errors**
If you encounter any issues or errors, ensure that:
- All file paths are correct.
- Required libraries are installed.

---

## **Extending the Project**

### **1. Adding More Words**

To add more words to the flashcards:
1. Open the `desired_language_english_words.csv` file in a text editor or spreadsheet.
2. Add new rows with the word in the desired language in the first column and the English translation in the second column.
3. Save the file.

### **2. Customizing the UI**

- **Changing the Background Color**: Modify the `BACKGROUND_COLOR` variable.
- **Updating the Font Style**: Customize the fonts used in `card_title` and `card_word` in the `Canvas` widget.

### **3. Enhancing Functionality**
- **Add a Score Counter**: Track the number of correct and incorrect responses.
- **Implement Difficulty Levels**: Allow users to choose between different difficulty levels (e.g., Easy, Medium, Hard) based on the frequency of word occurrence.

---

## **Conclusion**

This Flashcard Learning Application is a simple yet powerful tool for language learning. By extending and customizing it, you can create a more personalized learning experience. The application uses Python’s Tkinter library for the graphical interface and Pandas for efficient data handling, making it both user-friendly and easy to maintain.
