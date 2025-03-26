# BookBot

BookBot is a simple command-line tool that analyzes text files and provides word count and character frequency statistics.

## Description

BookBot is my first project from the [Boot.dev](https://www.boot.dev) curriculum. It's a Python program that reads text files (like books) and generates a report with:

- Total word count
- Character frequency count (alphabetic characters only, sorted by frequency)

## Features

- Count the total number of words in a text file
- Count and sort character frequencies
- Display a formatted report in the terminal
- Simple command-line interface

## Installation

Clone this repository to your local machine:

```bash
https://github.com/tutupharirabu/bookbot.git
cd bookbot
```

## Usage

Run the program by providing the path to the text file you want to analyze:

```bash
python main.py path/to/your/book.txt
```

### Example

```bash
python main.py books/frankenstein.txt
```

Output:
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20818
h: 19725
l: 12739
d: 12624
... (more characters)
============= END ===============
```

## Project Structure

- `main.py`: Entry point of the application
- `stats.py`: Contains functions for counting words and characters

## Dependencies

This project uses only Python standard libraries:
- sys
