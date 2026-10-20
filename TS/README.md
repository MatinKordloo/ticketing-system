# Ticket Management System

A web-based ticket management system built with Django and PostgreSQL.

## Features

- User registration, login, and logout
- Create, view, edit, and delete tickets
- Ticket priorities: Low, Medium, and High
- Ticket statuses: Open, In Progress, and Closed
- Filter tickets by status and priority
- Sort tickets by date and priority
- Responsive interface using Bootstrap 5
- User-specific ticket management
- Admin-only ticket status management

## Technologies

- Python 3.14
- Django 6.1.2
- PostgreSQL
- Bootstrap 5
- python-dotenv

## Requirements

- Python 3.14
- PostgreSQL
- pip

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/MatinKordloo/ticketing-system.git
cd ticketing-system
```

### 2. Create and activate a virtual environment

Run these commands in PowerShell from the repository root:

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

### 3. Install the dependencies

```powershell
python -m pip install -r TS/requirements.txt
```

### 4. Create a PostgreSQL database and user

Create a PostgreSQL database named `ticketing_db` and a database user named `ticketing_user`. Grant the database user the required permissions to access the database.

### 5. Configure environment variables

Create a `.env` file in the repository root directory, alongside `.gitignore`.

Add the following variables:

```dotenv
SECRET_KEY=your_generated_secret_key
DB_NAME=ticketing_db
DB_USER=ticketing_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

Replace `your_generated_secret_key` with a newly generated Django secret key. You can generate one by running:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key into the `.env` file.

Replace `your_database_password` with the password configured for your PostgreSQL database user.

**Important:** The values above are examples. Generate your own secret key and use your actual database credentials. Never share or commit your `.env` file.

### 6. Navigate to the Django project directory

```powershell
cd TS
```

### 7. Apply database migrations

```powershell
python manage.py migrate
```

### 8. Create an administrator account

```powershell
python manage.py createsuperuser
```

### 9. Start the development server

```powershell
python manage.py runserver
```

### 10. Open the application

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Admin Panel

Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and sign in with your superuser account.

Administrators can manage tickets and update their statuses through the admin panel.

## Security

- Secret keys and database credentials are stored in a local `.env` file.
- Never commit `.env` or other files containing secrets to version control.
- Keep `.env` in the repository root directory.
- Use a unique secret key and secure database password for each deployment.
