# BookStore CLI

Simple command-line application for managing a book catalog.

## Features

- Add book
- List books
- Get book by id
- Delete book
- Save/load data to JSON

## Tech Stack

- Python 3
- JSON file storage

## Run

```bash
python3 Books_HH.py

Example usage

> add
Title: Dune
Author: Frank Herbert
Year: 1965

> list
1. "Dune" — Frank Herbert (1965)

> get
Book id: 1
Found: {'id': 1, 'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965}
