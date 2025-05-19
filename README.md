# pharmacy_app

A simple Flask-based Pharmacy Inventory management web application.  
Track medicines, quantities, pricing, search, update stock levels, and delete entries through a clean Bootstrap UI.

## Features

- List all medicines with quantity, unit price, line‐total, and grand total value  
- Search by medicine name or generic name  
- Add new medicine records  
- Update existing stock entries  
- Delete medicines with confirmation prompt  
- View “Need Restock” report (low stock threshold)  

## Prerequisites

- Python 3.8+  
- Git  

## Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/YourUsername/pharmacy_app.git
   cd pharmacy_app
   ```
2. Create and activate a virtual environment  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) configure environment  
   ```bash
   set FLASK_APP=app.py
   set FLASK_ENV=development
   ```

## Usage

1. Initialize or upgrade the database (SQLite by default)  
   ```bash
   flask db init    # if using Flask-Migrate
   flask db migrate
   flask db upgrade
   ```
   > If you aren’t using migrations, the app will auto-create `instance/pharmacy.db` on first run.

2. Start the development server  
   ```bash
   flask run
   ```
3. Open `http://127.0.0.1:5000/` in your browser.

## URL Endpoints

- `/`           – Index/List view, optional `?q=search_term`  
- `/add`        – Form to add a new medicine  
- `/update/<id>` – Form to edit an existing record  
- `/delete/<id>` – POST route to remove a record  
- `/restock`    – View low-quantity medicines  

## Project Structure

```
pharmacy_app/
├─ app.py
│  medicine.db
├─ templates/
│  ├─ index.html
│  ├─ add_medicine.html
│  ├─ restock.html
│  └─ update.html
└─ static/
   └─ (optional css/js)
```

## Contributing

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -am 'Add foo'`)  
4. Push to the branch (`git push origin feature/foo`)  
5. Open a Pull Request
