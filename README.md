# Employee Management System with APIs & Visualization

A **Django-based Employee Management System** featuring REST APIs, PostgreSQL integration, and optional visual analytics using Chart.js. This project demonstrates a full-stack approach to managing employees, departments, attendance, and performance, complete with API documentation via Swagger and a modular Django structure.

---

## Features

- **Employee Management:** CRUD operations for employee data  
- **Department Management:** Track employee departments  
- **Attendance Tracking:** Record daily attendance (Present / Absent / Late)  
- **Performance Management:** Employee ratings and reviews  
- **REST APIs:** Built using Django REST Framework (DRF) with token-based authentication  
- **API Documentation:** Integrated Swagger UI for easy API exploration  
- **Database:** PostgreSQL as the backend database  
- **Data Seeding:** Generate 30–50 fake employee records using Faker  
- **Optional Visualizations:** Pie chart for employees per department, bar chart for monthly attendance  
- **Environment Variables:** Managed via `django-environ`  
- **Docker Support:** Optional Dockerfile and docker-compose setup for containerized deployment  

---

## Tech Stack

- **Backend:** Django 4.x, Django REST Framework  
- **Database:** PostgreSQL  
- **Authentication:** DRF Token Authentication / Simple JWT  
- **Visualization (Optional):** Chart.js  
- **Tools & Libraries:** drf-yasg, django-environ, Faker, django-filter, psycopg2-binary  

---

## Getting Started

1. Clone the repository:  
```bash
git clone https://github.com/<your-username>/employee-management-system.git
cd employee-management-system
