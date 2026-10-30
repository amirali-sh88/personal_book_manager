# Personal Book Manager

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

A simple personal book management application built with Python. It allows users to add multiple books, view their books, and save book information for future use.

## Features

- Add multiple books
- Display all saved books
- Save book information in a JSON file
- Load previously saved books
- Admin Mode with password protection

## Requirements

- Python 3
- python-dotenv

## Installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a file named `.env` in the project folder.

The `.env.example` file is a template that shows which environment variable is required.

The project needs the following environment variable:

`BOOK_MANAGER_ADMIN_PASSWORD`

Add the following content to your `.env` file:

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own password.

**Important:** Never upload your `.env` file to GitHub. The `.env.example` file should be included in the repository, but the actual `.env` file must remain private.

## Run the Program

The main program is located in `main.py`.

Run the application using:

```bash
python main.py
```

## Screenshot

![Program Screenshot](images/screenshot.png)