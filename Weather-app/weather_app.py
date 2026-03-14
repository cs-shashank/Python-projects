# Import the requests library
# This library is used to send HTTP requests to the weather API
import requests


# Function to fetch and display weather data
def get_weather(city, api_key):
    """Fetch and display weather information for a given city."""

    # Construct the API URL with city name, API key and metric units (Celsius)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        # Send GET request to the API with a timeout of 10 seconds
        response = requests.get(url, timeout=10)

        # Raise an exception if the HTTP request returned an error status
        response.raise_for_status()

        # Convert the API response into JSON format (Python dictionary)
        data = response.json()

        # Check if API returned a valid response
        if data.get("cod") != 200:
            print("City not found. Please try again.")
            return

        # Extract required weather information from JSON data
        temperature = data["main"]["temp"]          # temperature in Celsius
        humidity = data["main"]["humidity"]        # humidity percentage
        weather = data["weather"][0]["description"]  # weather description
        wind = data["wind"]["speed"]               # wind speed

        # Display the weather information to the user
        print("\nWeather Information")
        print("--------------------")
        print(f"City: {city}")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather}")
        print(f"Wind Speed: {wind} m/s")

    # Catch network errors, API errors, etc.
    except requests.exceptions.RequestException as error:
        print("Error fetching weather data:", error)


# Main function that controls program execution
def main():
    """Main function to run the weather application."""

    # Store your OpenWeather API key here
    api_key = "b5a1c9ce6c06cbd9d3c4df33efae09b5"

    # Infinite loop to allow multiple city searches
    while True:

        # Ask user to enter city name
        city = input("\nEnter city name (or type 'exit'): ")

        # If user types 'exit', stop the program
        if city.lower() == "exit":
            print("Exiting program.")
            break

        # Call the function to fetch weather data
        get_weather(city, api_key)


# Entry point of the program
# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()