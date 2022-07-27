# Weather App for RaspberryPi with Dht_11 sensor
This is a tkinter powered project to make a widget that display the current weather, one week forecast, and internal temperature and humidity using a DHT_11/22 sensor for RaspberryPi with the Adafruit_dht librery help.

The widget app will give you the reading via openweather Api of the current weather of the selected city, the week forecast, the measurement of the internal temperature and humidity, the current time and date.

it will change background and foreground colors to match the current wheather condition and more features.

```27/07/2022: the project is in is very early stage and need more work to do wat it promise so be patient for the complete version.```
## Prerequisites:

- RaspberryPI
- DHT_11 / DHT_22 sensor 
- Python 3.* 
- python3-libgpiod
- pip 3

<hr>

## Getting Started:

Clone this repository to your RaspberryPi

    git clone https://github.com/Andollini89/weather_app.git

To keep your system clear from unecessary packages that can only be used for this project we raccommend to use a virtual envoirment. so run:
    
    cd 'your path to weather_app

    sudo python3 -m v-env weather_app
To activate the virtual envoirment run:

    source weather_app/bin/activate

On RaspberryPi you may find troubles when tryng to modify files in the virtual envoirment as is been created with the suco command.

If so you need to gain the writing permissions via ```chown``` command or ```chmod``` command

Once you are done run the following command to install the required dependancies

    python3 -m pip install -r requirements.txt

#### Api weather account:
go to [openweathermap.org](https://openweathermap.org) and get your account with the API Key

now run from terminal in weather_app folder the folliwing command:
    
    sudo touch .env && sudo echo -e '\nAPIKEY=yourApiKeyFromOpenWeather' >> .env

#### __To run the programm__ run :

    python3 weatherApp.py
<hr>

## ToDo:

- Make the weather lookup on widget open based on user ip location
- Make possible to insert city and country to change weather research
- Make api call for weekly forecast and add it to the screen
- Add a database  to store user research and preferences
- Make graphic improvements like icons, colors, spacing, positioning etc..
