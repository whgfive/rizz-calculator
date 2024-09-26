# Rizz Calculator

Rizz Calculator is a fun web application that calculates a person's "Rizz Level" based on their name. It uses Flask for the backend, Redis for caching, and a modern, animated frontend.

## Features

- Calculate Rizz Level based on name input
- Animated result display
- Caching of results using Redis
- Configurable Rizz labels
- Dockerized for easy deployment

## Prerequisites

To run this application, you need to have the following installed:

- Docker
- Docker Compose

## Running the Application

### Using Docker Compose (Recommended)

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/rizz-calculator.git
   cd rizz-calculator
   ```

2. Build and run the containers:
   ```
   docker-compose up --build
   ```

3. Access the application in your web browser at `http://localhost`

4. To stop the application, press `Ctrl+C` in the terminal or run:
   ```
   docker-compose down
   ```

### Running Locally (Without Docker)

If you prefer to run the application without Docker, follow these steps:

1. Ensure you have Python 3.9+ and Redis installed on your system.

2. Clone the repository as described above.

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Start a Redis server locally.

6. Run the Flask application:
   ```
   python app.py
   ```

7. Access the application in your web browser at `http://localhost:5000`

## Configuration

You can modify the Rizz labels and their corresponding levels by editing the `rizz_config.json` file:

```
{
  "rizz_labels": [
    {"max": 20, "label": "Low Rizz"},
    {"max": 40, "label": "Mild Rizz"},
    {"max": 60, "label": "Moderate Rizz"},
    {"max": 80, "label": "High Rizz"},
    {"max": 100, "label": "God-tier Rizz"}
  ]
}
```

## Project Structure

- `app.py`: The main Flask application
- `input.html`: The HTML template for the web interface
- `rizz_config.json`: Configuration file for Rizz labels
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Defines and runs the multi-container Docker application
- `nginx.conf`: Configuration for the Nginx reverse proxy
- `requirements.txt`: List of Python package dependencies

## Development

To make changes to the application:

1. Modify the files as needed.
2. If you're using Docker Compose, the changes will be reflected immediately for Python files. For HTML changes, you may need to refresh your browser.
3. If you add new dependencies, update the `requirements.txt` file and rebuild the Docker image:
   ```
   docker-compose up --build
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).