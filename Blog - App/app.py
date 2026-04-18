from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

class Note(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    notes = Note.query.order_by(Note.created.desc()).all()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        note = Note(title=request.form['title'],
                    content=request.form['content'])
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/view/<int:id>')
def view(id):
    note = Note.query.get_or_404(id)
    return render_template('view.html', note=note)

@app.route('/delete/<int:id>')
def delete(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)