# KARTING-ACADEMY

Welcome to the KARTING-ACADEMY project. This project is designed to help manage and organize karting activities. Follow the instructions below to set up and run the project on your local machine.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [For Front-end Developers](#for-front-end-developers)

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
   
6. **Create config file - `config.py` in main directory**
   
   And in this file add:
   ```python
   SECRET_KEY = "ANY SECRET KEY"
   ```
   
   * Your secret key can be any characters, for example - 'slgsldfkwhiutyfwbx3-=^%#*c3487'

     
7. **Make migrations and migrate the database:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## Usage

Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000` to view the application.

How to add events or players?? 
1. **Create an superuser 'Admin user'**
   ```sh
   python manage.py createsuperuser
   ```

2. **Run the server:**
   ```sh
   python manage.py runserver
   ```

3. **Go to `http://127.0.0.1:8000/admin`**
   * And login using a previously registered user
     
   Congratulations!! You have successfully getting permission to access the admin panel

## For Front-End Developers

If you are working on the front-end part of the project, here's where you'll find the relevant files:

- **HTML Templates:** Front-end HTML files are located in the `templates` directory.
- **JavaScript Files:** Front-end JavaScript files can be found in the `static/js` directory.
- **CSS Stylesheets:** Front-end CSS files are located in the `static/css` directory.
- **Images and Assets:** Images and other static assets are stored in the `static/img` directory.

Make sure to coordinate with the back-end developers regarding any dynamic content or data integration needed in your HTML templates.

---

By following the above instructions, you should be able to set up and run the KARTING-ACADEMY project on your local machine. If you encounter any issues or have any questions, please feel free to open an issue in the repository. Happy karting!
