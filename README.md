# Wallpaper4u

Wallpaper4u is a Django-based web application for sharing and managing wallpapers.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the Repository:

    ```bash
    git clone https://github.com/Afshinfathi21/Wallpaper4u.git
    cd wallpaper4u
    ```


2. Build and Run the Docker Containers:

    ```bash
    docker-compose up --build
    ```

    Visit [http://localhost:8000/](http://localhost:8000/) in your web browser to access the Wallpaper4u application.

3. Apply Migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Create a Superuser (Optional):

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

## Usage

- Access the application at [http://localhost:8000/](http://localhost:8000/).
- Register or log in.
- Update your profile, upload wallpapers, like, and manage posts.
- Confirm your email address after registration.

## Docker Commands

- Stop the containers:

    ```bash
    docker-compose down
    ```

- View container logs:

    ```bash
    docker-compose logs
    ```

## Contributing

Feel free to contribute to this project. Create a pull request or open an issue for bugs or suggestions.

