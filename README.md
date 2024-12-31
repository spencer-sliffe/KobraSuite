# Kobra Suite Django Backend

## Install and Run

1. **Clone the Repo**: Download and install Repository from [here](https://github.com/spencer-sliffe/KobraSuite).
   - **macOS/Linux**: 
     ```bash
     git clone https://github.com/spencer-sliffe/KobraSuite.git
     cd KobraSuite/kobrasuitecore
     ```
   - **Windows**:
     ```bash
     git clone https://github.com/spencer-sliffe/KobraSuite.git
     cd KobraSuite\kobrasuitecore
     ```

2. **Start Venv**:
   - **macOS/Linux**: 
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:
   - **macOS/Linux**: 
     ```bash
     pip install -r requirements.txt
     ```
   - **Windows**:
     ```bash
     pip install -r requirements.txt
     ```

4. **Setup .env**:
   - **macOS/Linux**: 
     - Create a `.env` file in the `kobrasuitecore` directory.
     - Use the following template and replace placeholders as needed:
       ```plaintext
       SECRET_KEY=your_secret_key
       DEBUG=False
       ALLOWED_HOSTS=localhost 127.0.0.1
       CSRF_TRUSTED_ORIGINS=https://127.0.0.1 
       SECURE_SSL_REDIRECT=0
       DBNAME=kobrasuite
       DBHOST=localhost
       DBUSER=your_db_user
       DBPASS=your_db_password
       ```
   - **Windows**: 
     - Same steps as macOS/Linux.

5. **Run Django Project**:
   - **macOS/Linux**: 
     ```bash
     python3 manage.py runserver
     ```
   - **Windows**:
     ```bash
     python manage.py runserver
     ```
