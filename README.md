# KARTING-ACADEMY

Welcome to the KARTING-ACADEMY project. This project is designed to help manage and organize karting activities. Follow the instructions below to set up and run the project on your local machine.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

## Description

Welcome to the KARTING-ACADEMY project. This project is designed to create a platform for managing and organizing karting activities. Whether you're a karting enthusiast, an instructor, or a track owner, KARTING-ACADEMY aims to streamline the management of karting events, memberships, and more.

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone this repository to your computer:**
   ```sh
   git clone https://github.com/Maksim-Volosh/KARTING-ACADEMY.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd KARTING-ACADEMY
   ```

3. **Create a virtual environment:**
   ```sh
   python -m venv .venv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

5. **Install the requirements:**
   ```sh
   pip install -r requirements.txt
   ```

6. **Make migrations and migrate the database:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## Usage

Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000` to view the application.

---

By following the above instructions, you should be able to set up and run the KARTING-ACADEMY project on your local machine. If you encounter any issues or have any questions, please feel free to open an issue in the repository. Happy karting!
