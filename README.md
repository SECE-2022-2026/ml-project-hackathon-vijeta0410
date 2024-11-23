[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KPIpT6T5)
🌤️ Weather Forecast Notifier
=============================

About
-----

The **Weather Forecast Notifier** is a Streamlit-based web application that allows users to subscribe to personalized weather updates. Users can enter their details, select notification preferences, and receive regular weather updates via email.

Features
--------

*   **User-friendly Interface**: Intuitive form for user registration and preferences.
    
*   **Weather Data**: Fetches real-time weather data using the OpenWeather API.
    
*   **Email Notifications**: Sends weather updates directly to the user’s email.
    
*   **Custom Scheduling**: Users can select daily or weekly updates at their preferred time.
    
*   **Multi-Language Support**: Notifications available in various languages.
    

Tech Stack
----------

*   **Frontend**: [Streamlit](https://streamlit.io/)
    
*   **Backend**: Python, SQLite
    
*   **APIs**:
    
    *   [OpenWeather API](https://openweathermap.org/) for weather data
        
    *   [LangChain](https://www.langchain.com/) for generating personalized messages
        
*   **Email Service**: SMTP with Gmail
    

Setup Instructions
------------------

Follow these steps to set up the project locally:

### Prerequisites

*   Python 3.7+
    
*   API key from OpenWeather
    
*   SMTP email credentials (Gmail recommended)
    

### Installation

1.  bashCopy codegit clone https://github.com/your-username/weather-forecast-notifier.gitcd weather-forecast-notifier
    
2.  bashCopy codepython -m venv venvsource venv/bin/activate # On Windows: venv\\Scripts\\activate
    
3.  bashCopy codepip install -r requirements.txt
    
4.  makefileCopy codeEMAIL=PASSWORD=OPENWEATHER\_API\_KEY=
    
5.  bashCopy codepython -c "from database import init\_db; init\_db()"
    
6.  bashCopy codestreamlit run app.py
    
7.  Access the app at http://localhost:8501.
    

How It Works
------------

1.  Users fill out the form with their details, including email, location, frequency, and preferred notification time.
    
2.  Weather data is fetched using the OpenWeather API.
    
3.  Personalized messages are generated using LangChain and sent via email.
    
4.  Notifications are scheduled using APScheduler for automated delivery.
    

Screenshots
-----------
![Screenshot 2024-11-23 103009](https://github.com/user-attachments/assets/479fdf0f-c31a-4ee3-93e6-c50b8ac8f380)

![Screenshot 2024-11-23 101210](https://github.com/user-attachments/assets/12b7c769-03c8-4a71-824e-e116053b7685)

![Screenshot 2024-11-22 224042](https://github.com/user-attachments/assets/53eb6117-189d-49c4-9f70-7ce6fd1494ce)

![Screenshot 2024-11-23 101819](https://github.com/user-attachments/assets/e4be5056-26c6-44c8-838c-1db319a49a44)



Project Structure
-----------------

├── app.py               # Main Streamlit app  
├── database.py          # Database initialization and operations  
├── scheduler.py         # Notification scheduling logic  
├── emailer.py           # Email sending functionality  
├── llm.py               # Message generation using LangChain  
├── weather.py           # Fetch weather data from OpenWeather API  
├── requirements.txt     # Python dependencies  
├── .env                 # Environment variables (add this to .gitignore)  └── README.md            # Project documentation   `

Contributing
------------

Contributions are welcome! If you'd like to improve the project, feel free to fork the repository and submit a pull request.

1.  Fork the repository
    
2.  Create a new branch (git checkout -b feature-branch)
    
3.  Commit changes (git commit -m "Add a new feature")
    
4.  Push to the branch (git push origin feature-branch)
    
5.  Open a pull request
