# Event Management API

## Description
The Event Management API is a backend application built with Django and Django REST Framework.  
It allows users to browse upcoming events publicly, while authenticated users can create, update, and manage their own events securely using JWT authentication.

## Features
- Public event listing
- Upcoming events filtering
- User registration and authentication (JWT)
- Create, update, and delete events (authenticated users only)
- Permission control (only the event organizer can edit or delete their events)
- Event registration and unregistration
- Pagination and search support

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development)

## How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/Jo7eph/event-management-api
cd event_api