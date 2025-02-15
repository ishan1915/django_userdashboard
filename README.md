# django_userdashboard
# Django User Authentication Project

## Overview
This Django application provides a user authentication system with email or username and password. The project includes pages for login, signup, forgot password, change password, dashboard, and profile. Access to specific pages is restricted based on authentication status.

## Features
- User authentication with email or username and password.
- Secure password reset functionality via email.
- Access control for authenticated users.
- User profile management.

## Requirements

### 1. Login Page
- Fields: Username/Email and Password.
- Links to Sign Up and Forgot Password pages.

### 2. Sign Up Page
- Fields: Username, Email, Password, and Confirm Password.
- Link to return to the Login page.

### 3. Forgot Password Page
- Field: Email.
- Button to send password reset instructions via email.

### 4. Change Password Page
- Requires authentication.
- Fields: Old Password, New Password, and Confirm Password.
- Link to return to the Dashboard.

### 5. Dashboard
- Accessible only to authenticated users.
- Displays a personalized greeting message.
- Links to Profile and Change Password pages.
- Logout option.

### 6. Profile Page
- Displays user details: Username, Email, Date Joined, and Last Updated.
- Link to return to the Dashboard.
- Logout option.

## Installation & Setup

1. **Clone the Repository:**
```sh
$ git clone https://github.com/yourusername/django_userdashboard.git
$ cd django_userdashboard
```

2. **Create a Virtual Environment & Activate it:**
```sh
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```sh
$ pip install -r requirements.txt
```

4. **Apply Migrations:**
```sh
$ python manage.py migrate
```

5. **Create a Superuser (Optional):**
```sh
$ python manage.py createsuperuser
```

6. **Run the Development Server:**
```sh
$ python manage.py runserver
```

7. **Access the Application:**
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Configuration
### Email Settings (For Password Reset)
Modify `settings.py` to configure email sending:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```
**Note:** Use an App Password instead of your actual email password.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

---
For any issues or improvements, please open an [issue](https://github.com/yourusername/django_userdashboard/issues).

