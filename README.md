# Recani-M: Anime Recommendation System

Recani-M is a sophisticated web application designed to deliver personalized anime recommendations using a combination of content-based filtering and multi-armed bandit algorithms. This unique approach allows the system to continuously refine its suggestions based on user interactions, offering a more tailored and engaging experience over time.

## Table of Contents

- [Features](#features)
- [Concepts](#concepts)
  - [Content-Based Filtering](#content-based-filtering)
  - [Multi-Armed Bandit Algorithm](#multi-armed-bandit-algorithm)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User Authentication**: Secure user registration and login functionality to personalize the experience.
- **Extensive Anime Database**: Detailed information on a wide variety of anime titles, including genres, tags, and descriptions.
- **Personalized Recommendations**: Uses content-based filtering to suggest anime that align with user preferences.
- **Dynamic Refinement**: The multi-armed bandit algorithm refines recommendations by learning from user ratings and feedback.
- **Responsive Design**: User-friendly interface optimized for both desktop and mobile devices.

## Concepts

### Content-Based Filtering

Content-based filtering recommends items based on the attributes of the items and the preferences of the user. In Recani-M, each anime's attributes—such as genres, tags, and descriptions—are used to build a user profile. This profile helps predict which unseen anime the user might enjoy. The recommendation process involves:
- Extracting features from anime descriptions and metadata.
- Building a user preference model based on interactions with various anime.
- Matching user preferences with anime features to generate recommendations.

### Multi-Armed Bandit Algorithm

The multi-armed bandit algorithm is a powerful approach for balancing exploration (trying new items) and exploitation (recommending items known to be liked). This algorithm allows Recani-M to:
- Continuously learn from user interactions and ratings.
- Adjust recommendations dynamically to improve accuracy.
- Provide a mix of familiar and new anime to maintain user engagement.
The algorithm operates by treating each recommendation as a "bandit" and dynamically selecting which "bandit" to "pull" based on the user's feedback.

## Installation

To set up Recani-M locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/manoj-323/recani_m.git
   cd recani_m
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations to set up the database:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Project Structure

- **recani/**: Contains the main application code, including:
  - **models.py**: Defines the database models for anime and user interactions.
  - **views.py**: Handles the logic for rendering web pages and processing user requests.
  - **urls.py**: Maps URLs to views.
  - **templates/**: HTML templates for rendering the web pages.
  - **static/**: Static files (CSS, JavaScript, images).

- **recani_m/**: Contains project settings and configurations, including:
  - **settings.py**: Configuration for the Django project.
  - **urls.py**: Root URL configurations.

- **db.sqlite3**: SQLite database file used for development.
- **manage.py**: Command-line utility for administrative tasks.

## Usage

1. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

2. **Explore Anime:**
   Browse through the extensive anime database to discover detailed information on various titles.

3. **Receive Recommendations:**
   View personalized anime recommendations tailored to your preferences.

4. **Rate Anime:**
   Provide ratings for anime you have watched to help the system refine its recommendations.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code adheres to our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Django**: The web framework used to build the application.
- **Multi-Armed Bandit Algorithms**: For their contribution to dynamic recommendation refinement.
- **Anime Community**: For providing rich datasets and inspiration.

For any queries or issues, please contact [manoj-323](https://github.com/manoj-323).
