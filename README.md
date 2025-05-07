# StudyBuddy Matching Platform

**StudyBuddy** is a web application for University of Birmingham students. It helps you find study partners by using a matching algorithm based on your preferences. Once matched, you can chat with your study buddies directly in the app and then book available study rooms on campus to collaborate effectively. This platform streamlines the process of connecting with peers and finding suitable study environments.

## Purpose

This project aims to combat academic isolation and improve access to study spaces for University of Birmingham students. Many students experience loneliness and struggle to find suitable, uncrowded study areas. StudyBuddy addresses this by connecting students with similar academic interests and study habits, fostering a supportive community. This encourages collaborative study, which can lead to better networking, reduced procrastination, increased confidence, improved mental well-being, and enhanced learning. The app provides an efficient way to find partners, message them, and reserve study spaces, making campus study more accessible and engaging.

## Demo Video

https://drive.google.com/file/d/1hV3pGF2VtVBRJC9huCyye070WN4Flee6/view?usp=share_link

## How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    It's assumed there's a `requirements.txt` file. If not, you'll need to create one based on the imports. A typical command would be:
    ```bash
    pip install -r requirements.txt
    ```
    Key dependencies include Flask, Flask-SQLAlchemy, Flask-Migrate. (A `requirements.txt` should be generated for the project).

4.  **Initialize the database (if running for the first time):**
    The application uses Flask-Migrate.
    ```bash
    flask db init  # If migrations folder doesn't exist
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
    Alternatively, the project includes a `reset_db` utility. You might be able to initialize or reset the database using a Flask shell command:
    ```python
    # from flask shell
    # from app.debug_utils import reset_db
    # reset_db()
    ```

5.  **Set up environment variables:**
    The `.flaskenv` file should be present with the following:
    ```
    FLASK_APP=run.py
    FLASK_ENV=development
    FLASK_DEBUG=1
    ```
    Ensure `config.py` has a `SECRET_KEY` and the `SQLALCHEMY_DATABASE_URI` is correctly set (defaults to `sqlite:///app/data/data.sqlite`).

6.  **Run the application:**
    ```bash
    flask run
    ```
    The application will typically be available at `http://127.0.0.1:5000/`.

## Technologies Used

*   **Programming Language:** Python
*   **Web Framework:** Flask
*   **Database:** SQLite (via Flask-SQLAlchemy)
*   **Database Migrations:** Flask-Migrate
*   **Templating:** Jinja2
*   **Frontend:** HTML, CSS, JavaScript

## Implemented Functionalities

*   **User Management:**
    *   User signup and login
    *   User logout
*   **Validation:**
    * To Register a new user onto StudyBuddy, any input address in the Email field must end with "@student.bham.ac.uk".
    * Password in Registration must be typed twice in respective fields for confirmation.
*   **Profile & Preferences:**
    *   Editing and updating user profiles with study preferences (subjects, availability, preferred gender, location details).
*   **Matching System:**
    *   Finds top study matches by converting user preference data from the preference form into vectors.
    *   Calculates similarity between users by employing the cosine similarity mathematical method.
*   **Communication:**
    *   Real-time messaging between matched users.
*   **Booking System:**
    *   Users can send, accept, decline, and cancel study session invitations.
    *   Book available rooms for study sessions.
*   **Error Handling:**
    *   Custom error pages for 403, 404, 413, and 500 errors.
*   **Database Utilities:**
    *   Shell context for accessing database models (`db`, `sa`, `so`).
    *   `reset_db` function for resetting database (likely for development/testing).


## Contributions

| Student Name & ID | Contribution (%) | Key Contributions / Tasks Completed                               |
|-------------------|------------------|-------------------------------------------------------------------|
| Shreyas [2746031] | [25%]            | Implemented the matching functionality using user preference data.|
|                   |                  | Set up the database.                                              |
|                   |                  | Designed the profile page.                                        |
|                   |                  | Set up the project structure.                                     |
|                   |                  | Compiled the README documentation.                                |
|Angel Yao [2753805]| [25%]            | Coded the messaging feature and set up the corresponding database.|
|                   |                  | Merged Angel branch with main and sorted out conflicts.           |
|                   |                  | Compiled and edited video.                                        |
|Amal      [2877627]| [25%]            | Implemented the study preferences update feature                  |
|                   |                  | Wrote unit tests to validate preferences update functionality     |
|                   |                  | Contributed feature updates and worked with Git version control   |
|Eliot      [2468876]| [25%]           | Implemented the registration and login features for StudyBuddy    |
|                   |                  | Implemented UoB email validation check for registration           |
|                   |                  | Added a debug feature to the code                                 |
