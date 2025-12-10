🍃 Online Farm Store – Full Stack Web Application
Flask • MySQL • HTML/CSS • Sessions • Cart System • User Auth
📌 Project Overview

The Online Farm Store is a full-stack web application that allows users to:

Register & log in

Browse products

Add items to cart

Checkout with user details

Save orders into a MySQL database

View responsive pages built with HTML & CSS

This project demonstrates backend development, database integration, session handling, and frontend UI design.

🚀 Tech Stack
Backend

Python

Flask Framework

Sessions & Flash Messaging

Database

MySQL

MySQL Connector for Python

Frontend

HTML5

CSS3 (stored in static/ folder)

Jinja2 Templating (Flask Templates)

App Structure
/templates
    index.html
    login.html
    register.html
    product.html
    cart.html
    checkout.html
    about.html
    blog.html

/static
    /css
        style.css
        product.css
        cart.css
        ...
    /images
        (product images, banners)

app.py (main Flask backend)
README.md

🗄️ Database Details

The project uses a MySQL database named Desproj.

Required Tables:
1. users table

Stores registered users.

id (INT, PK, AUTO_INCREMENT)
username (VARCHAR)
email (VARCHAR)
password (VARCHAR)

2. products table

Stores orders placed during checkout.

product_name (VARCHAR)
quantity (INT)
user_name (VARCHAR)
user_age (INT)
user_phone (VARCHAR)
user_address (TEXT)
user_email (VARCHAR)

🔐 User Authentication Features
✔ Register

Username

Email

Password

Duplicate emails prevented

✔ Login

Email + Password check

Session stores user information

✔ Logout

Clears session

Redirects to home page

🛒 Cart Functionality

The cart is stored in Flask session:

Add products

Increase quantity if item already in cart

View cart

Checkout and save to DB

Clear cart after order

Example cart object:

session['cart'] = [
  {'product_name': 'Apples', 'price': 100, 'quantity': 2},
  {'product_name': 'Bananas', 'price': 50, 'quantity': 1}
]

📦 Product Page

You can modify or load products dynamically.
Currently defined statically in product().

💾 Checkout Process

User enters:

Name

Age

Phone

Address

Email

Then all cart items are inserted into the database via:

insert_order()

▶️ How to Run the Project
1. Install Dependencies
pip install flask mysql-connector-python

2. Start MySQL & create database
CREATE DATABASE Desproj;

3. Create the required tables

(Use schema above)

4. Run the app
python app.py

5. Open in browser
http://127.0.0.1:5000/

📁 File Summary
File / Folder	Description
app.py	Main Flask backend
/templates	HTML views (Jinja2)
/static/css	Styling files
/static/images	Product / UI images
README.md	Project documentation
🎯 Features Implemented

Full user authentication system

Session-based cart

MySQL order storage

Clean frontend UI

Flash messages for user feedback

Modular template structure

Real-world full-stack flow

👨‍💻 Developer

Vallamsetti Srinivas
BTech CSE | Full Stack • AI/ML • Backend
Email: srinivasvallamsettis@gmail.com
