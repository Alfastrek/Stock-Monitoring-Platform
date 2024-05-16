# Stock Monitoring Platform 

Welcome to the Stock Monitoring Platform documentation. This platform allows users to create and manage watchlists of stock symbols and monitor the latest stock values.

## Getting Started

To get started with the Stock Monitoring Platform, follow the steps below:

1. Clone the repository from GitHub.
2. Install the required dependencies by running the following command:

   ```bash
   npm install
   ```

3. Run the frontend development server:

   ```bash
   npm start
   ```

4. Run the backend server:

   ```bash
   python manage.py runserver
   ```

5. Access the platform at [http://127.0.0.1:8000] in your web browser.

## User Authentication

### Registration

To register a new user, send a POST request to the following endpoint:

```
POST /auth/register/
```

Include the following JSON payload in the request body:

```json
{
  "username": "example_username",
  "email": "example@example.com",
  "password": "example_password"
}
```

### Login

To log in, send a POST request to the following endpoint:

```
POST /auth/login/
```

Include the following JSON payload in the request body:

```json
{
  "username": "example_username",
  "email": "example@example.com",
  "password": "example_password"
}
```

Upon successful login, you will receive an authentication token.

## Dashboard

### Watchlist

The dashboard displays the user's watchlist of stock symbols. To access the dashboard, log in to the platform and navigate to the dashboard page.

### Stock Prices

The dashboard also provides real-time stock prices for the symbols in the user's watchlist. Stock prices are retrieved from the Alpha Vantage API.

## API Endpoints

### Authentication Endpoints

- `POST /auth/register/`: Register a new user.
- `POST /auth/login/`: Log in with username and password.

### Watchlist Endpoints

- `GET /api/watchlist/`: Retrieve the user's watchlist.
- `POST /api/watchlist/`: Add a new stock symbol to the user's watchlist.
- `DELETE /api/watchlist/{id}/`: Delete a stock symbol from the user's watchlist.

### Stock Info Endpoint

- `GET /api/stock/{symbol}/`: Retrieve the latest stock price for a given symbol.

## Technologies Used

- Frontend:
  - React.js
  - TypeScript
  - Material UI

- Backend:
  - Django (Python)
  - PostgreSQL

Project Development Report-

1) Backend Functionality Working Perfectly with authentication and Stock price Fetching.
2) Frontend still Requires some work but will be improved in coming time.
