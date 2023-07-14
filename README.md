# blogging-website-BE
This repository is the backend for the Blogging Website that uses Django framework, utilizes PostgreSQL as the database and is containerized using Docker.

## Prerequisites

Before running the web app, ensure that you have the following dependencies installed on your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

## Getting Started

To run the Django web app locally with Docker, follow these steps:

1. Clone the repository:

    ```shell
    git clone https://github.com/web-information-system-2022-2/blogging-website-BE
    ```
2. Go to the repository:

    ```shell
    cd blogging-website-BE
    ```

    Create a virtual environment and activate it:

    ```shell
    python -m venv venv
    source venv/bin/activate
    ```

    Create a `.env` file. The content might look like this:
    ```
    DB_NAME=blog_db
    DB_USER=admin
    DB_PASSWORD=admin
    DB_HOST=db
    DB_PORT=5432
    DJANGO_SECRET_KEY=django-insecure-irn-y9t^gt_)h9@hk!^@=%f77fu8$p_@@*w2fh&%&g4s3)(70y
    DJANGO_DEBUG=True
    ```

    Remove all the containers and images that are related to this project. This is to ensure that the containers are created from scratch and there is no conflict with the previous containers. To do that, run:

    ```
    docker container rm <container_id>
    docker image rm <image_id>
    ```

    Create a `data/db` directory inside the project directory. This is to ensure that the database is persisted even after the containers are removed. To do that, run:

    ```
    sudo chown $USER:$USER data/db
    ```

3. Start the containers:

    ```shell
    docker compose up
    ```

    In the first run, it might not work as the database is not yet created. If you run til the end and see the following message:

    ```
    PostgreSQL is ready to accept connections
    ```

    Create database for our project:

    ```
    docker exec -it "blogging-website-be-db-1" psql -U admin -c "CREATE DATABASE <database_name>"
    ```

    Migrate the database:

    ```
    docker exec -it "blogging-website-be-app-1" python manage.py migrate
    ```

    Auto create superuser and some initializations for OAuth2 with Google:

    ```
    docker exec -it "blogging-website-be-app-1" python init.py
    ```

    Then restart the containers by running the previous command again and it will work.

4. Access the web app in your browser:

    ```
    http://0.0.0.0:8000
    ```
