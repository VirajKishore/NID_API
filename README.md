# Note It Down - Backend API

A FastAPI-based REST API for a simple note-taking application. This backend provides CRUD operations for managing notes with a SQLite database and proper migration handling using Alembic.

## 🚀 Features

- **RESTful API** with FastAPI framework
- **SQLite Database** with SQLAlchemy ORM
- **Database Migrations** using Alembic for version control
- **CORS Support** for frontend integration
- **Input Validation** using Pydantic schemas
- **Error Handling** with proper HTTP status codes
- **Auto-generated API Documentation** with Swagger UI

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - Python SQL toolkit and Object-Relational Mapping (ORM)
- **Alembic** - Database migration tool for SQLAlchemy
- **Pydantic** - Data validation using Python type annotations
- **SQLite** - Lightweight, serverless database
- **Uvicorn** - ASGI server for running FastAPI applications

## 📋 API Endpoints

| Method | Endpoint          | Description             |
| ------ | ----------------- | ----------------------- |
| GET    | `/notes`          | Retrieve all notes      |
| POST   | `/note`           | Create a new note       |
| PUT    | `/note/{note_id}` | Update an existing note |
| DELETE | `/note/{note_id}` | Delete a note           |

### Note Schema

```json
{
  "title": "string (required)",
  "body": "string (optional)"
}
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd NID_API
   ```

2. **Set up virtual environment**

   ```bash
   # Install virtualenvwrapper (if not already installed)
   pip install virtualenvwrapper

   # Create and activate virtual environment
   mkvirtualenv nid_api
   workon nid_api
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up database migrations**

   ```bash
   # Run migrations to create database tables
   alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`

### API Documentation

Once the server is running, visit:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 🗄️ Database Schema

### Notes Table

| Column       | Type     | Description                    |
| ------------ | -------- | ------------------------------ |
| id           | Integer  | Primary key, auto-increment    |
| title        | String   | Note title (indexed)           |
| body         | String   | Note content                   |
| last_updated | DateTime | Timestamp of last modification |

## 🔧 Development Experience

### Challenges Overcome

1. **Environment Setup Issues**

   - Struggled with virtualenvwrapper installation via Homebrew
   - Fixed `.zshrc` configuration error (missing double quote)
   - Successfully set up isolated Python environment

2. **Database Migration Learning**

   - Initially planned to use a simple database initialization approach
   - Decided to implement proper migration system using Alembic for production-ready code
   - Learned standard practices for database version control

3. **Git Configuration**

   - Switched from password-based to SSH authentication
   - Updated remote URL: `git remote set-url origin git@github.com:VirajKishore/NID_API.git`

4. **CORS Implementation**
   - Understood the need for Cross-Origin Resource Sharing when separating frontend and backend
   - Implemented proper CORS middleware for React frontend integration

### Key Learnings

- **SQLAlchemy ORM**: Learned to work with databases using Python objects instead of raw SQL
- **FastAPI Features**: Leveraged automatic API documentation, request validation, and error handling
- **Database Migrations**: Implemented proper version control for database schema changes
- **API Design**: Created RESTful endpoints following best practices
- **Error Handling**: Implemented comprehensive error handling with appropriate HTTP status codes

## 📁 Project Structure

```
NID_API/
├── alembic/                 # Database migration files
│   ├── versions/           # Migration scripts
│   ├── env.py             # Alembic environment configuration
│   └── script.py.mako     # Migration template
├── model/                  # Database models and configuration
│   ├── __init__.py
│   ├── database.py        # Database session management
│   └── models.py          # SQLAlchemy models
├── main.py                # FastAPI application entry point
├── schemas.py             # Pydantic schemas for request/response validation
├── requirements.txt       # Python dependencies
├── alembic.ini           # Alembic configuration
└── nid.db               # SQLite database file
```

## 🔄 Database Migrations

### Creating a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Applying migrations

```bash
alembic upgrade head
```

### Rolling back migrations

```bash
alembic downgrade -1
```

## 🌐 CORS Configuration

The API is configured to allow requests from:

- `http://localhost:5173` (React development server)

To add more origins, update the `origins` list in `main.py`.

## 📝 Requirements

See `requirements.txt` for the complete list of dependencies.
