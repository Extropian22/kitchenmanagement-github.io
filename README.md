# Kitchen Manager Pro

A comprehensive restaurant management system that handles recipe costing, nutrition analysis, labeling, inventory control, and menu engineering.

## Features

- Recipe Management and Costing
- Nutrition Analysis and Label Generation
- Inventory Control System
- Menu Engineering and Analysis
- User Authentication and Role Management

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env` file
5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
6. Run the application:
   ```
   flask run
   ```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///kitchen_manager.db
```

## Usage

Visit `http://localhost:5000` after starting the application to access the web interface.
