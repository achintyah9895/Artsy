# Artsy API – Django REST Art Marketplace

Artsy API is a backend REST API built with Django and Django REST Framework for an online art marketplace.  
Users can register, log in using JWT authentication, upload artwork, and place bids on available art pieces.

---

## Features

- User registration
- JWT authentication (login / logout)
- Upload and manage artwork
- View all artworks
- Place bids on artworks
- View artworks uploaded by the logged-in user
- Permission-based access control

---

## Tech Stack

Backend
- Python
- Django
- Django REST Framework

Authentication
- JWT (SimpleJWT)

Database
- SQLite 

---

## API Endpoints

### Authentication

POST `/register/`  
Create a new user account.

POST `/login/`  
Login and receive access and refresh tokens.

POST `/logout/`  
Logout and blacklist refresh token.

---

### Art

GET `/arts/`  
Retrieve all art items.

POST `/arts/`  
Create a new art listing (authenticated users only).

GET `/arts/my_art/`  
Get artworks uploaded by the logged-in user.

---

### Bidding

POST `/bid/`  
Place a bid on an artwork.

When a bid is placed:
- If bid is from same user of art ,error.
- The bid amount checked, if higher than previous bid
- The bid is saved
- The artwork price updates to the new bid amount

---

## Installation



```bash
git clone https://github.com/achintyah9895/Artsy.git
cd artsy-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
