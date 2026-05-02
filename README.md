# 📝 NoteVault

A clean, dark-themed personal notes web app built with **Flask** and **SQLite**. Save your thoughts, ideas, and tasks — and automatically get them exported as `.txt` and `.json` files too.

---

## ✨ Features

- 📌 Create, view, and delete notes
- 💾 Auto-saves every note as `.txt` and `.json` file on disk
- 🗃️ SQLite database via Flask-SQLAlchemy
- 🎨 Sleek dark UI with gradient design
- 📱 Fully responsive layout
- 🐳 Docker-ready for easy deployment

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Database | SQLite (via Flask-SQLAlchemy) |
| Frontend | HTML, CSS (custom dark theme) |
| Deployment | Docker |

---

## 📁 Project Structure

```
NoteVault/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── templates/
│   ├── index.html          # Notes list page
│   ├── add.html            # Add new note page
│   └── view.html           # View single note page
└── saved_notes/            # Auto-generated folder for .txt & .json exports
```

---

## 🚀 Getting Started

### Option 1 — Run Locally (Python)

**1. Clone the repository**
```bash
git clone https://github.com//vinod-meghwar/NoteVault.git
cd NoteVault
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

### Option 2 — Run with Docker 🐳

**1. Build the Docker image**
```bash
docker build -t notevault .
```

**2. Run the container**
```bash
docker run -p 5000:5000 notevault
```

**3. Open in browser**
```
http://localhost:5000
```

---

## 📸 Screenshots

| Page | Description |
|------|-------------|
| **Home** | Displays all notes in a card grid with date and preview |
| **Add Note** | Clean form with character counter |
| **View Note** | Full note with metadata badges |

---

## 🗂️ How File Export Works

Every time you save a note, NoteVault automatically creates two files inside the `saved_notes/` folder:

- **`{id}_{title}.txt`** — Human-readable plain text format
- **`{id}_{title}.json`** — Structured JSON for programmatic use

When a note is deleted, its files are removed too. ✅

**Example `.json` export:**
```json
{
  "id": 4,
  "title": "The Role of Mindset in Achieving Goals",
  "content": "A positive and growth-oriented mindset...",
  "created": "2026-04-20 10:54:35"
}
```

---

## 📦 Dependencies

```
flask
flask-sqlalchemy
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with ❤️ using Flask & Python
