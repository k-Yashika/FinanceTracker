# Personal Finance Tracker

A web application to track personal finances, manage transactions, and visualize spending over time. Built using Flask, Flask-SQLAlchemy, Flask-Login, and Plotly for data visualization.

## Features

- User authentication (registration, login and logout)
- Add, view, and manage financial transactions
- Visualize spending over time

## Tech Stack

**Backend:** Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Werkzeug

**Frontend:** HTML, CSS, Jinja2

**Data Visualization:** Pandas, Plotly

## Prerequisites

    - Python 3.10+
    - Virutal Environment
    
## Installation

    1. Clone the repository

```bash
git clone https://github.com/yourusername/personal_finance_tracker.git
cd personal_finance_tracker
```

    2. Create the Virtual Envrionment

```bash
python -m venv venv
source venv\Scripts\activate
```

    3. Install the dependencies

```bash
pip install -r requirements.txt
```

    4. Initialize the database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

    5. Run the application

```bash
flask run
```

## Author

- Github [@k-Yashika](https://www.github.com/k-Yashika)
- Linkedin [@k-yashika](https://www.linkedin.com/in/k-yashika/)

