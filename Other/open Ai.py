import tkinter as tk
import webbrowser
import urllib.parse
from bs4 import BeautifulSoup
import requests

url = 'https://chat.openai.com'

def search():
    # Get the user's search term
    search_term = entry.get()

    # Generate the search URL
    search_url = f'{url}/search?q={urllib.parse.quote(search_term)}'

    # Print the search URL (for debugging purposes)
    print(search_url)

    # Request the search results page
    response = requests.get(search_url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the search results container
    results_container = soup.find('div', {'class': 'search-results'})

    # Clear the current contents of the output text widget
    output.delete('1.0', tk.END)

    # Display the search results in the output text widget
    output.insert(tk.END, str(results_container))

# Create a new window
window = tk.Tk()

# Set the window title
window.title('OpenAI Chat Search')

# Create an entry box for the user's search term
entry = tk.Entry(window)

# Create a button to submit the search term
button = tk.Button(window, text='Search', command=search)

# Create a text widget to display the search results
output = tk.Text(window)

# Add the entry, button, and output to the window
entry.pack(padx=50, pady=10)
button.pack(padx=50, pady=10)
output.pack(padx=50, pady=10)

# Run the window
window.mainloop()
