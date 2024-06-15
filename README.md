# Recani_M

Recani_M is a Django-based web application for managing and recommending anime shows. It allows users to sign up, log in, view anime details, and rate them.

## Features

- **User Authentication**: Sign up, log in, and log out functionalities.
- **Anime Details**: View detailed information about anime shows, including genres, demographics, and ratings.
- **User Ratings**: Users can rate anime shows and view their ratings.

## Technologies Used

- **Backend**: Django, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: GitHub, local development

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/manoj-323/recani_m.git
    cd recani_m
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:8000`.

## Usage

1. **Sign Up**: Create a new account.
2. **Log In**: Log into your account.
3. **Browse Anime**: View the list of anime shows.
4. **Rate Anime**: Provide your ratings for the anime shows.
5. **View Details**: Click on the "More Details" button to see detailed information about the anime.

## Project Structure

```
recani_m/
├── recani/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── recani_m/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── README.md
```

## Contributing

1. **Fork the Repository**
2. **Create a Feature Branch**
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit Your Changes**
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the Branch**
    ```bash
    git push origin feature-branch
    ```
5. **Create a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
