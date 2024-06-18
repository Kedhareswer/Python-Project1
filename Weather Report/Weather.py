import requests
import json
import tkinter as tk

# Set up the GUI
root = tk.Tk()
root.title("Weather App")

# Create labels and entry fields for location input and unit selection
location_label = tk.Label(root, text="Enter location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

unit_label = tk.Label(root, text="Select unit:")
unit_label.pack()
unit_var = tk.StringVar()
unit_var.set("imperial")
unit_imperial = tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value="imperial")
unit_metric = tk.Radiobutton(root, text="Celsius", variable=unit_var, value="metric")
unit_imperial.pack()
unit_metric.pack()

# Create a function to retrieve weather data from the API
def get_weather():
    # Get the location input from the user
    location = location_entry.get()
    
    # Make an API request to OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units={unit_var.get()}&appid=4a613c2e952661de99c0f360ed97376c"
    response = requests.get(url)
    
    # Parse the JSON data from the response
    data = json.loads(response.text)
    
    # Extract the relevant weather information
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    
    # Update the weather display labels
    temp_label.config(text=f"Temperature: {temp}°")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_label.config(text=f"Wind Speed: {wind_speed} mph")
    description_label.config(text=f"Description: {description.capitalize()}")

# Create a button to retrieve weather data when clicked
button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

# Create labels to display weather data
temp_label = tk.Label(root)
temp_label.pack()
humidity_label = tk.Label(root)
humidity_label.pack()
wind_label = tk.Label(root)
wind_label.pack()
description_label = tk.Label(root)
description_label.pack()

# Start the GUI main loop
root.mainloop()
