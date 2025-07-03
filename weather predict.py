import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your working API key
API_KEY = "927d23a5ccbe2241097a159e9e8fc2d9"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={API_KEY}&q={city}&units=metric"

    try:
        response = requests.get(complete_url)
        print(f"URL used: {complete_url}")  # Debug: show URL
        print(f"Status Code: {response.status_code}")  # Debug: show HTTP status
        print(f"Response Text: {response.text}")  # Debug: show raw response

        response.raise_for_status()  # Raises HTTPError for bad codes

        data = response.json()
        print(data)

        if data["cod"] != 200:
            return f"Error: {data.get('message', 'City not found')}"

        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]["description"].capitalize()

        result = (
            f"City: {city.title()}\n"
            f"Temperature: {main['temp']} °C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Pressure: {main['pressure']} hPa\n"
            f"Weather: {weather_desc}\n"
            f"Wind Speed: {wind['speed']} m/s"
        )
        return result

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP Error: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request Error: {req_err}"
    except Exception as e:
        return f"Other Error: {e}"

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    weather_info = get_weather(city)
    result_label.config(text=weather_info)

root = tk.Tk()
root.title("Basic Weather App")
root.geometry("400x300")
root.resizable(False, False)

heading = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"))
heading.pack(pady=10)

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", command=show_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
