#!/usr/bin/python3

import random

# Print HTTP headers
print("Content-type: text/html\n")

# List of random colors
colors = ["#FF5733", "#33FF57", "#3357FF", "#F4A460", "#8A2BE2", "#20B2AA"]
bg_color = random.choice(colors)

# HTML Output
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dynamic Color Changer</title>
    <style>
        body {{
            text-align: center;
            background-color: {bg_color};
            font-family: Arial, sans-serif;
        }}
        button {{
            padding: 10px 15px;
            font-size: 16px;
            border: none;
            background-color: #000;
            color: white;
            cursor: pointer;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <h1>Background Color Changed!</h1>
    <form action="/cgi-bin/change.py" method="post">
        <button type="submit">Change Again</button>
    </form>
</body>
</html>
""")
