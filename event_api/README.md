# Event Management API

## Project Overview
The Event Management API is a backend service built using **Django** and **Django REST Framework**.  
It allows users to browse events publicly while authenticated users can create, manage, and register for events.

Authentication is implemented using **JWT (JSON Web Tokens)** and the API supports filtering, searching, and event registration.

---

# Key Features

### Public Access
- View all events
- View event details
- Filter upcoming events

### Authentication
- User registration
- JWT login authentication

### Event Management
- Create events (authenticated users)
- Update events (organizer only)
- Delete events (organizer only)

### Event Registration
- Register for events
- Unregister from events

---

# Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite

---

# Installation

Clone the repository

```bash
git clone https://github.com/Jo7eph/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/event_api