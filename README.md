# Flask Application with SSL and nginx Proxy

## Overview

This project implements a Flask web application with SSL support and an nginx reverse proxy. The application allows users to submit messages which are stored in a JSON file and displayed on the home page.

## Features

- **Flask Web Application**: Handles user messages and stores them in a JSON file.
- **SSL/TLS Encryption**: Ensures secure communication.
- **nginx Reverse Proxy**: Forwards requests to the Flask application.

## Requirements

- Python 3.x
- `Flask` library
- `nginx` web server

## Installation

### Python and Flask

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/your_flask_app.git
    cd your_flask_app
    ```

2. **Create and Activate a Virtual Environment**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

### nginx

1. **Install nginx**
    ```sh
    sudo apt-get update
    sudo apt-get install nginx
    ```

2. **Configure nginx**

    Create a configuration file for your Flask app:

    ```sh
    sudo nano /etc/nginx/sites-available/your_flask_app
    ```

    Add the following content:

    ```nginx
    server {
        listen 80;
        server_name yourdomain.com;

        location / {
            proxy_pass https://IP_ADRESS;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    ```

3. **Enable the Site**

    Create a symbolic link to enable the site:

    ```sh
    sudo ln -s /etc/nginx/sites-available/your_flask_app /etc/nginx/sites-enabled/
    ```

4. **Test nginx Configuration**

    ```sh
    sudo nginx -t
    ```

5. **Restart nginx**

    ```sh
    sudo systemctl restart nginx
    ```

## Running the Flask Application

1. **Start the Flask App**
    ```sh
    python app.py
    ```

    Ensure the Flask application is set to run with SSL:

    ```python
    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=('certB.pem', 'keyB.pem'))
    ```
    Create the certificates with the following command:
   ```sh
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
   ```

## File Structure

```plaintext
your_flask_app/
│
├── app.py
├── user_data.json
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

