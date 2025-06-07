# 🏋️‍♀️ Fitness Booking API

A RESTful API built using **Django REST Framework** to manage fitness class listings and bookings with timezone support.

---

## 📦 Features

- List available fitness classes (with timezone-aware times)
- Create bookings for classes with slot availability validation
- Retrieve bookings by client email

---

## ⚙️ Installation & Setup

###  Clone the Repository

```bash
git clone https://github.com/athulrajk/fitness_booking_api.git
cd fitness_booking_api

API Endpoints & Examples
GET /classes?tz=Asia/Kolkata
[
  {
    "id": 1,
    "name": "Yoga",
    "start_time": "2025-06-07T07:30:30Z",
    "instructor": "Hari",
    "total_slots": 100,
    "available_slots": 66,
    "active": true
  },
  {
    "id": 2,
    "name": "Zoomba",
    "start_time": "2025-06-07T07:31:06Z",
    "instructor": "Athul Raj",
    "total_slots": 80,
    "available_slots": 1,
    "active": true
  },
  {
    "id": 3,
    "name": "HIIT",
    "start_time": "2025-06-07T07:31:24Z",
    "instructor": "Anshad",
    "total_slots": 30,
    "available_slots": 30,
    "active": true
  }
]

POST /book
{
  "class_id": 1,
  "client_name": "Ansil K",
  "client_email": "ansil@gmail.com"
}


GET /bookings/list?client_email=ansil@gmail.com
[
  {
    "id": 3,
    "client_name": "Ansil K",
    "client_email": "ansil@gmail.com",
    "booked_at": "2025-06-07T08:03:28.851627Z",
    "fitness_class": 1
  },
  {
    "id": 4,
    "client_name": "Ansil K",
    "client_email": "ansil@gmail.com",
    "booked_at": "2025-06-07T08:04:08.667160Z",
    "fitness_class": 2
  },
  {
    "id": 5,
    "client_name": "Ansil K",
    "client_email": "ansil@gmail.com",
    "booked_at": "2025-06-07T08:05:11.434008Z",
    "fitness_class": 1
  }
]

requirements.txt
Django==4.2.4
djangorestframework==3.14.0
pytz==2024.1
