# Tweeter

A modern Twitter-like social media platform built with Python and Django.

## Features

- User authentication and authorization
- Tweet creation, editing, and deletion
- Like and comment functionality
- Responsive design with Tailwind CSS

## Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript, Tailwind CSS, Bootstrap
- Database: SQLite
- Authentication: Django Authentication System
- Forms: Django Forms
- Database ORM: Django ORM
- Additional Features: Django Browser Reload, Widget Tweaks

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jenilsoni01/Tweeter
cd tweeter
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Project Structure

```
tweeter/
├── .venv/                  # Virtual environment
├── authentication/         # Custom authentication app
├── tweet/                  # Main app for tweets
├── theme/                  # Tailwind theme app
├── templates/             # Global templates
├── static/                # Static files
├── media/                 # User uploaded files
├── tweeter/              # Project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Project Link: [Link](https://github.com/jenilsoni01/Tweeter) 