# THC Event Management Web App

A Flask-based web application for creating, listing, and managing group events (e.g., hiking, social gatherings). Users can view events, create new ones, and contact organizers.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Running the App](#running-the-app)
- [Database](#database)
- [Adding/Editing Events](#addingediting-events)
- [File Uploads](#file-uploads)
- [Customizing the App](#customizing-the-app)
- [Static Assets](#static-assets)
- [Templates](#templates)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- List all events on the homepage and a dedicated page
- Create new events with image uploads
- Contact form for inquiries
- Uses SQLite for event storage
- Flash messages for user feedback
- Static assets for images, CSS, and JS

---

## Project Structure

```
THC/
│
├── db.py                # Database helper functions
├── events.db            # SQLite database file
├── main.py              # Main Flask application
├── readme.md            # Project documentation
│
├── static/
│   ├── assets/          # Images and icons
│   ├── css/             # Stylesheets
│   ├── event_images/    # Uploaded event images
│   └── js/              # JavaScript files
│
└── templates/
    ├── *.html           # Jinja2 HTML templates
    └── subpages/        # Additional HTML subpages
```

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd THC
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask werkzeug
   ```

4. **(Optional) Install other dependencies:**
   - If you add more packages, update a `requirements.txt` file.

---

## Running the App

1. **Initialize the database:**
   - The database is initialized automatically when you run the app.

2. **Run the Flask server:**
   ```bash
   python main.py
   ```
   - The app runs on `https://localhost:3000` with SSL (see `main.py` for certificate paths).

3. **Access the app:**
   - Open your browser and go to: [https://localhost:3000](https://localhost:3000)

---

## Database

- SQLite database: `events.db`
- Schema is initialized via `init_db()` in `main.py` (see `db.py` for details).
- Events are stored in the `events` table.

---

## Adding/Editing Events

- **To add an event:**  
  Go to `/create-event` and fill out the form. Required fields: event name, date, time, location, organizer name.
- **To view all events:**  
  Go to `/all-events`.
- **To edit event logic or fields:**  
  Update the form in `templates/create-event.html` and the handling logic in `main.py` (`create_event` route).
- **To change event display:**  
  Edit `templates/show-events.html` or `templates/index.html` for homepage events.
- **To modify event storage:**  
  Update the schema in `db.py` and the insert logic in `main.py`.

---

## File Uploads

- Uploaded event images are stored in `static/event_images/`.
- Allowed file types: `png`, `jpg`, `jpeg`, `gif`.
- File upload logic is in `main.py` (`create_event` route).
- To change allowed types, update the `ALLOWED_EXTENSIONS` set in `main.py`.

---

## Customizing the App

- **Change homepage events:**  
  Edit the `all_events` list in `main.py` or connect the homepage to the database.
- **Modify event fields:**  
  Update the event form, database schema, and event display templates.
- **Change styles:**  
  Edit CSS files in `static/css/`.
- **Add new pages:**  
  Create new HTML files in `templates/` and add new routes in `main.py`.
- **Change city/country defaults:**  
  Update the `CITIES` and `COUNTRIES` lists in `main.py`.
- **Change SSL/port:**  
  Edit the `app.run()` parameters in `main.py`.

---

## Static Assets

- **Images:**  
  Place in `static/assets/img/` or `static/event_images/` (for uploads).
- **CSS:**  
  Place in `static/css/`.
- **JavaScript:**  
  Place in `static/js/`.

---

## Templates

- All HTML templates are in the `templates/` directory.
- Use Jinja2 templating for dynamic content.
- Common templates: `index.html`, `show-events.html`, `create-event.html`, `contact.html`.
- For layout changes, edit `header.html`, `footer.html`, and `navbar.html`.

---

## Troubleshooting

- **SSL Errors:**  
  Ensure the certificate paths in `main.py` are correct or remove `ssl_context` for HTTP.
- **Database Issues:**  
  Delete `events.db` to reset, or check `db.py` for schema problems.
- **File Upload Errors:**  
  Ensure `static/event_images/` exists and is writable.
- **Template Not Found:**  
  Make sure the template file exists in `templates/` and is referenced correctly in `main.py`.

---

## License

MIT License (or specify your own).

---

**Feel free to update this README as your project evolves!**

