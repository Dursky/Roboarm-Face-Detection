import board
import busio as io
import adafruit_mlx90614

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

ambient_temp = mlx.ambient_temperature - 1 
object_temp = mlx.object_temperature + 10
# temperature results in celsius
print("Srednia Temp: ", ambient_temp)
print("Twarz Temp: ", object_temp)
