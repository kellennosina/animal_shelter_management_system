# animal_shelter_management_system

Animal Shelter Management System

Overview

The Animal Shelter Management System is a database-driven application designed to streamline the management of animal shelters. It enables users to efficiently track animal records, adoption processes, medical history, and volunteer activities.

Features

Animal Records Management: Store and manage details of animals including breed, age, health status, and location.

Adoption Process Tracking: Maintain records of potential adopters and successful adoptions.

Medical Records Management: Keep track of medical treatments, vaccinations, and veterinary visits.

Volunteer & Staff Management: Register and manage volunteers and staff details.

Donation Tracking: Record donations and generate reports for transparency.

User Authentication: Secure login system for administrators, staff, and volunteers.

Technologies Used

Backend: MySQL (Database: animal_shelter_db)

Frontend: HTML, CSS, JavaScript (or any framework of choice)

Server-side: PHP/Python/Node.js (depending on implementation preference)

Authentication: JWT/OAuth for secure user login

Installation & Setup

Clone the Repository:

git clone https://github.com/your-repo/animal-shelter-management.git
cd animal-shelter-management

Database Setup:

Import the database schema (animal_shelter_db.sql) into MySQL.

Update the database credentials in the config file (config.php or .env).

DB_NAME=animal_shelter_db
DB_USER=root
DB_PASSWORD=kellen

Install Dependencies:

If using PHP:

composer install

If using Node.js:

npm install

Run the Application:

Start the server:

php -S localhost:8000  # For PHP
node server.js  # For Node.js

Open http://localhost:8000 in the browser.

Usage

Login: Admins, staff, and volunteers can log in with their credentials.

Manage Animals: Add, update, or delete animal records.

Process Adoptions: Register potential adopters and update adoption status.

Track Medical History: Add vaccination and treatment details for animals.

Manage Volunteers & Donations: Record volunteer information and track donations.

Contributing

If you wish to contribute, fork the repository and submit a pull request. Ensure to follow the project's coding guidelines.

License

This project is licensed under the MIT License.
