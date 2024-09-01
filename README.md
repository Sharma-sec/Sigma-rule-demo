# Sigma Rule Demo

## Overview

The Sigma Rule Demo is a web application that showcases SQL injection vulnerabilities and Sigma rule implementation using Flask. It includes a login page to demonstrate secure and vulnerable SQL query handling.

## Usage

1. **Run the Application:**
   - Start the Flask server by running the `app.py` script.
   - Access the application at `http://127.0.0.1:5000/` in your web browser.

2. **Login:**
   - Enter a username and password into the form and click "Login" to test query execution.

3. **Toggle Sigma Rule:**
   - Click "Toggle Sigma Rule" to switch between secure (parameterized) and vulnerable (SQL injection) query modes.
   - The button will update to show the current status.

4. **Default Credentials:**
   - Click "Default Credentials" to automatically fill the form with the username `admin` and password `password123`.

5. **SQL Injection:**
   - Click "SQL Injection" to autofill the form with an SQL injection payload (`' OR '1'='1`) to demonstrate the vulnerability.

## Important Notes

- **Educational Use:** This demo is for educational purposes to highlight the risks of SQL injection and the importance of secure query practices.
- **Database:** An SQLite database (`users.db`) is created automatically with a default user for testing.

## License

This project is licensed under the MIT License.