# Weather Forecast App
------------------------------------------------

This project is a weather forcast application (based on https://open-meteo.com website),
that uses four Docker containers for a modular and scalable architecture:

1.  **Django Backend (API):** Exposes the application programming interfaces (APIs) for fetching and managing weather data.
2.  **Data Service (Django):** Fetches weather data from a source (<https://open-meteo.com> in this case), processes and aggregates it, and stores it in the database.
3.  **PostgreSQL Database:** Stores weather raw and sumarized data efficiently.
4.  **React Frontend (Material-UI):** Provides a user interface with options to display the weather raw data and the weather temprature aggrigations per day.

**Installation and Local Development**

1.  **Prerequisites:** Ensure you have Docker and Docker Compose installed on your system. Download instructions can be found at [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

2.  **Clone the Repository:** Clone this repository using Git:

    **Bash**

    git clone https://github.com/your-username/weather-app.git

3.  **Build Docker Images:** Navigate to the project directory and run the following command:

    **Bash**

    `docker-compose build`


    This will build Docker images for all four services.

4.  **Run the Application:** Start the application using:

    **Bash**

    `docker-compose up -d`

    The `-d` flag runs the containers in detached mode, allowing them to run in the background.

**Accessing the Application:**

-   **Frontend:** The React frontend application is accessible at http://localhost:3001/.
-   **Backend API:** The Django backend API is accessible at http://localhost:8000/.
    (you won't typically need to access it directly as the React frontend makes API calls).
-   **Data Service:** The Django Data Service backend API is accessible at http://localhost:8001/,
    **Note:** For this POC project we trigger the data fetch from the website by manual browsing the dedicated API:
    http://localhost:8001/api/fetch
    In real word we will implement an events which trigger this API, and it will be deployed as an cloud-function e.g. AWS lambda ans SQS.
    
-   **Database:** The PostgreSQL database is not directly accessible in this configuration. If you whish investigating the DB, use tools like pgAdmin or command-line tools to interact with it.
 

**APIs:**

-   **Django Backend (API):**
    -   `/api/get_all`: Fetches all raw weather data.
    -   `/api/get_all_sum`: Fetches all aggrigated weather data.
    -   `/api/query`: Queries weather data based on optional date range parameters (`start_date` and `end_date`) in the query string.
      e.g. 'api/query?start_date=2024-08-15&end_date=2024-08-19'
    -   `/api/query_sum`: Queries aggrigated weather data based on optional date range parameters (`start_date` and `end_date`) in the query string.
      e.g. 'api/query_sum?start_date=2024-08-15&end_date=2024-08-19'

-   **Data Service (Django):** 
    -   `/api/fetch`: Fetches data from https://open-meteo.com , Processes and aggregates raw data, and Stores aggregated data in the database.

**Notes:**

-   I assume you're using the default ports specified in `docker-compose.yml`. You can customize these ports if needed.
-   The provided Dockerfile for the React frontend uses `npm start` to run the application in development mode. For production, you should build the production-ready version using `npm run build` and serve the static files.
-   In real project we should use environment variables to store sensitive information like database credentials outside of your Dockerfile or code.

**Further Development:**

-   We need to improve application security practices, especially for production environments, e.g. manage IAM and Access Control.
-   We should consider using a container orchestration tool like Kubernetes for managing deployments at scale.

