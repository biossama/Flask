## Flask Todo App

This is a simple Flask application for managing todo tasks. Users can add, delete, and update tasks using the web interface provided by the application.

#### Installation

##### Clone the repository:

```bash
git clone https://github.com/biossama/Flask.git
```

##### Navigate to the project directory:


```bash
cd Flask/Todo-List_App
```

##### Install dependencies using [pip](https://pip.pypa.io/en/stable/):

```bash
    pip install -r requirements.txt
```

##### Project Structure

  *  app.py: Contains the Flask application code including routes for handling task manipulation.
  *  templates/: Directory containing HTML templates for rendering the web interface.
       * index.html: Template for the main page displaying the list of tasks.
       * update.html: Template for updating a task.
  *  test.db: SQLite database file for storing tasks.
  *  requirements.txt: List of Python dependencies for the project.

##### Technologies Used

   flask: Python web framework for building the application. 
   SQLAlchemy: Python SQL toolkit and Object-Relational Mapping (ORM) library for interacting with the database.
   HTML/CSS: For creating the user interface of the application.
