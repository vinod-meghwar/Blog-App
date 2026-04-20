from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

NOTES_DIR = 'saved_notes'
os.makedirs(NOTES_DIR, exist_ok=True)

def safe_filename(title):
    """Title se safe filename banao"""
    name = re.sub(r'[^\w\s-]', '', title).strip()
    name = re.sub(r'[\s]+', '_', name)
    return name[:50] if name else 'note'

def save_note_to_file(note):
    """Note ko .txt aur .json dono formats mein save karo"""
    base = f"{note.id}_{safe_filename(note.title)}"
    
    # Plain text file
    txt_path = os.path.join(NOTES_DIR, base + '.txt')
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(f"Title  : {note.title}\n")
        f.write(f"Created: {note.created.strftime('%d %B %Y, %I:%M %p')}\n")
        f.write("-" * 40 + "\n\n")
        f.write(note.content)
    
    # JSON file
    json_path = os.path.join(NOTES_DIR, base + '.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'id'     : note.id,
            'title'  : note.title,
            'content': note.content,
            'created': note.created.strftime('%Y-%m-%d %H:%M:%S')
        }, f, ensure_ascii=False, indent=2)

def delete_note_files(note):
    """Note ki files delete karo"""
    base = f"{note.id}_{safe_filename(note.title)}"
    for ext in ('.txt', '.json'):
        path = os.path.join(NOTES_DIR, base + ext)
        if os.path.exists(path):
            os.remove(path)

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
        save_note_to_file(note)   # ← file bhi save karo
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/view/<int:id>')
def view(id):
    note = Note.query.get_or_404(id)
    return render_template('view.html', note=note)

@app.route('/delete/<int:id>')
def delete(id):
    note = Note.query.get_or_404(id)
    delete_note_files(note)       # ← files bhi delete karo
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)