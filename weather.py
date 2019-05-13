import pyowm

# https://api.openweathermap.org/
# API-key: 


class Weather(object):
    def __init__(self):
        owm = pyowm.OWM('YOUR API KEY', version="2.5")  # You MUST provide a valid API key
        self.reg = owm.city_id_registry()
        id = self.reg.ids_for('Zürich')
        observation = owm.weather_at_place('Zurich,CH')
        self.w = observation.get_weather()

    def __cloud(self):
        clouds = self.w.get_clouds()
        state = "Cloud coverage is: {}%".format(clouds)
        return state

    def __rain(self):
        rain = self.w.get_rain()
        if rain != {}:
            state = "Today, there's gonna be some rain"
            return state

    def __wind(self):
        wind = self.w.get_wind()
        wind_speed = wind["speed"]
        if wind["deg"] >= 22.5 and wind["deg"] < 77.5:
            state = "Wind is comming from Northeast with a Speed from {}".format(wind_speed)
            return state
        elif wind["deg"] >=77.5 and wind["deg"] < 112.5:
            state = "Wind is comming from East with a Speed from {}".format(wind_speed)
            return state
        elif wind["deg"] >=112.5 and wind["deg"] < 157.5:
            state = "Wind is comming from Southeast with a Speed from {}".format(wind_speed)
            return state
        elif wind["deg"] >=157.5 and wind["deg"] < 202.5:
            state = "Wind is comming from South with a Speed from {}".format(wind_speed)
            return state
        elif wind["deg"] >=202.5 and wind["deg"] < 247.5:
            state = "Wind is comming from Southwest with a Speed from {}".format(wind_speed)
            return state
        elif wind["deg"] >=247.5 and wind["deg"] < 292.5:
            state = "Wind is comming from West with a Speed from {}".format(wind_speed)
            return state
        elif wind["deg"] >=292.5 and wind["deg"] < 337.5:
            state = "Wind is comming from Northwest with a Speed from {}".format(wind_speed)
            return state
        else:
            state = "Wind is comming from North with a Speed from {}".format(wind_speed)
            return state

    def __humidity(self):
        humidity = self.w.get_humidity()
        state = "The humidity is around {}%".format(humidity)
        return state

    def __pressure(self):
        pressdict = self.w.get_pressure()
        pressure = pressdict["press"]
        state = "The pressure is {} hPA".format(pressure)
        return state

    def __temperature(self):
        tempdict = self.w.get_temperature('celsius')
        temperature = tempdict["temp"]
        state = "The temperature is at {}°".format(temperature)
        return state

    def __status(self):
        status = self.w.get_detailed_status()
        state = "Outside: {}".format(status)
        return state

    def __id(self):
        id = self.reg.ids_for('Zürich')
        state = "The Data is for {}".format(id)
        return state

    def call(self):
        print(self.__id())
        print(self.__wind())
        print(self.__status())
        print(self.__cloud())
        print(self.__humidity())
        print(self.__pressure())
        print(self.__temperature())
        print(self.__rain())

we = Weather()
we.call()
