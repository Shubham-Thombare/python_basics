# Weather API App
# 06556f8cca1b685e22641fe7e63436c2

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self): 

        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
          
        self.setStyleSheet("""
                        QLabel, QPushButton{
                                            font-family: calibri;
                        }
                        QLabel#city_label{
                                            font-size: 40px;
                                            font-style: italic;
                        }    
                        QLineEdit#city_input{
                                            font-size: 40px;
                        }
                        QPushButton#get_weather_button{
                                                        font-size: 30px;
                                                        font-weight: bold;
                        }
                        QLabel#temperatur_label{
                                                        font-size: 75px;
                        }
                        QLabel#emoji_label{
                                                        font-size: 100px;
                                                        font-family: segoe UI emoji;
                        }
                        QLabel#description_label{
                                                        font-size: 50px;
                        }
                            """)
        
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "06556f8cca1b685e22641fe7e63436c2"
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            print(data)

            if data["cod"] == 200:
                self.display_weather(data)
            else:
                print(data)

        except requests.exceptions.HTTPError as http_err:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check the request parameters.")
                case 401:
                    self.display_error("Invalid API key. Please check your API key.")
                case 403:
                    self.display_error("Forbidden\nAccess is Denied.")
                case 404:
                    self.display_error("City not Found.")
                case 500:
                    self.display_error("Internal server Error\nPlease try again later.")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response from server.")
                case 503:
                    self.display_error("Service Unavailable\nServer is down.")
                case 504:
                    self.display_error("Gateway Timeout\nServer is not responding.")
                case _:
                    self.display_error(f"HTTP error occurred: {http_err}")

        except requests.exceptions.ConnectionError as conn_err:
            self.display_error("Network error\nPlease check your internet connection.")

        except requests.exceptions.Timeout as timeout_err:
            self.display_error("The request timed out\nPlease try again later.")    

        except requests.exceptions.TooManyRedirects as redirect_err:
            self.display_error("Too many redirects\nThe request URL is bad.")

        except requests.exceptions.RequestException as req_err:
            self.display_error(f"An error occurred: {req_err}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("color: red; font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("color: green; font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c =  temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) + 32
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(self, weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(self, weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "🌈"
        

# to know description of weather id there are certain ranges:
# range 200-232: Thunderstorm
# range 300-321: Drizzle    
# range 500-531: Rain
# range 600-622: Snow
# range 701-781: Atmosphere (e.g., mist, smoke, haze)
# range 800: Clear
# range 801-804: Clouds

if __name__ == "__main__":
      app = QApplication(sys.argv)
      weather_app = WeatherApp()
      weather_app.show()
      sys.exit(app.exec_())
