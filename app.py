from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'pharmacy_secret_key'

def get_db_connection():
    conn = sqlite3.connect('medicine.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    search = request.args.get('q', '').strip()
    conn = get_db_connection()
    if search:
        like = f"%{search}%"
        medicines = conn.execute(
            'SELECT * FROM medicine WHERE name LIKE ? OR generic_name LIKE ?',
            (like, like)
        ).fetchall()
    else:
        medicines = conn.execute('SELECT * FROM medicine').fetchall()
    conn.close()

    grand_total = sum(m['quantity'] * m['price'] for m in medicines)
    return render_template('index.html',
                           medicines=medicines,
                           grand_total=grand_total,
                           search=search)

@app.route('/add', methods=('GET','POST'))
def add():
    if request.method=='POST':
        name     = request.form['name']
        generic  = request.form['generic_name']
        quantity = int(request.form['quantity'])
        price    = float(request.form['price'])

        conn = get_db_connection()
        # check for existing
        exists = conn.execute(
            'SELECT 1 FROM medicine WHERE name = ? AND generic_name = ?',
            (name, generic)
        ).fetchone()
        if exists:
            conn.close()
            flash('Medicine “%s” already exists!' % name, 'danger')
            return render_template('add_medicine.html')

        conn.execute(
            'INSERT INTO medicine (name, generic_name, quantity, price) VALUES (?,?,?,?)',
            (name, generic, quantity, price)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_medicine.html')

@app.route('/update/<int:id>', methods=('GET','POST'))
def update(id):
    conn = get_db_connection()
    med = conn.execute('SELECT * FROM medicine WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        action = request.form['action']
        amount = int(request.form['amount'])
        new_qty = med['quantity'] + ( -amount if action=='sold' else amount )

        if new_qty < 0:
            conn.close()
            flash('Error: resulting quantity cannot be negative.', 'danger')
            return render_template('update.html', med=med)

        conn.execute('UPDATE medicine SET quantity = ? WHERE id = ?', (new_qty, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('update.html', med=med)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM medicine WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/restock')
def restock():
    conn = get_db_connection()
    meds = conn.execute('SELECT * FROM medicine WHERE quantity = 0').fetchall()
    conn.close()
    return render_template('restock.html', medicines=meds)

if __name__ == '__main__':
    app.run(debug=True)
