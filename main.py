from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import BME280        #importing BME280 library

i2c = I2C(sda = Pin(21), scl = Pin(22), freq = 1000)     #initializing the I2C method for ESP32


bme = BME280.BME280(i2c=i2c)          #BME280 object created
temperature = bme.temperature            #reading the value of temperature
humidity = bme.humidity                     #reading the value of humidity
pressure = bme.pressure                     #reading the value of pressure

print('Temperature is: ', temperature)    #printing BME280 values
print('Humidity is: ', humidity)
print('Pressure is: ', pressure)
#sleep(10)           #delay of 10s
