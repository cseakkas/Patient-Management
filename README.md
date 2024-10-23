# Paperless Patient Management System

## Overview
The **Paperless Patient Management System** is a web-based application designed to facilitate the management of patient data and interactions with healthcare professionals. Built using Django (Python), MySQL, and HTML/CSS/JavaScript, this system provides a seamless experience for patients, doctors, pathologists, and pharmacists through dedicated modules.

## Features
- **Patient Module**:
  - Online registration and login.
  - Access to personal profile, doctor lists, appointment history, and test/medicine records.

- **Doctor Module**:
  - Online registration and login.
  - Manage patient lists, upcoming and past appointments, and view patient test/medicine history.

- **Pathology Module**:
  - Login access for pathologists.
  - Retrieve patient history using Token ID and track tests performed.

- **Pharmacy Module**:
  - Login access for pharmacists.
  - View patient history using Token ID and see prescribed medications.

## Technologies Used
- **Backend**: Django (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript

## Installation
To set up the project locally, follow these steps:

### Create a virtual environment:
- python -m venv venv
### Activate the virtual environment:
- venv\Scripts\activate

 ### Install the required packages:
 - pip install -r requirements.txt


## Database Configuration
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'paperless_patient_management',
        'USER': 'username',  # Replace with your MySQL username
        'PASSWORD': 'password',  # Replace with your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',  # Default MySQL port
    }
}


1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/paperless-patient-management-system.git
