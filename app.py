from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="12345",  # Replace with your MySQL password
    database="Desproj"
)

# Initialize cart in session
@app.before_request
def before_request():
    if 'cart' not in session:
        session['cart'] = []



# Route to handle user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email already registered! Please log in.')
            return redirect(url_for('login'))

        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        db.commit()
        cursor.close()

        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route to handle user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user_id'] = user[0]  # Store user ID in session (use the `id` column from users table)
            session['username'] = user[1]  # Store username in session
            flash('Login successful!')
            return redirect(url_for('index'))  # Redirect to home page after login
        else:
            flash('Invalid email or password!')

    return render_template('login.html')

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the product page
@app.route('/product')
def product():
    # Example product list. You may want to fetch this from the database.
    products = [
        {'name': 'Apples', 'price':100},
        {'name': 'Bananas', 'price':50},
        {'name': 'Cherries', 'price':200},
        {'name': 'Tomatoes', 'price':30},
        {'name': 'Potatoes', 'price':20},
        {'name': 'Onions', 'price':45},
        {'name': 'Alfalfa Sprouts', 'price':10},
        {'name': 'Seaweed', 'price':15},
    ]
    return render_template('product.html', products=products)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')  # Make sure you have a blog.html template

# Route to handle adding products to the cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = []  # Initialize cart if not exists

    product_name = request.form.get('product_name')
    price = float(request.form.get('price'))  # Convert price to float
    quantity = int(request.form.get('quantity'))  # Convert quantity to int

    # Check if product already exists in cart
    for item in session['cart']:
        if item['product_name'] == product_name:
            item['quantity'] += quantity  # Increase quantity if already exists
            break
    else:
        # Add new item if not found
        session['cart'].append({'product_name': product_name, 'price': price, 'quantity': quantity})

    session.modified = True  # Ensure session updates

    flash(f'Added {quantity} x {product_name}(s) to your cart.')
    return redirect(url_for('product'))

@app.route('/cart')
def cart():
    return render_template('cart.html', cart=session['cart'])

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_age = request.form['user_age']
        user_phone = request.form['user_phone']
        user_address = request.form['user_address']
        user_email = request.form['user_email']
        
        insert_order(user_name, user_age, user_phone, user_address, user_email, session['cart'])
        session.pop('cart')  # Clear the cart after checkout
        return render_template('index.html', order_success=True)  # ✅ Pass variable to trigger alert
    return render_template('checkout.html', cart=session.get('cart', []))

def insert_order(user_name, user_age, user_phone, user_address, user_email, cart_items):
    cursor = db.cursor()
    
    for item in cart_items:
        cursor.execute(
            "INSERT INTO products (product_name, quantity, user_name, user_age, user_phone, user_address, user_email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (item['product_name'], item['quantity'], user_name, user_age, user_phone, user_address, user_email)
        )
    
    db.commit()
    cursor.close()

# Route to log out
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
