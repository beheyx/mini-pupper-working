from MangDang.mini_pupper.ESP32Interface import ESP32Interface

positions = [512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
esp32 = ESP32Interface()
#positions = [512, 512, 100, 512, 100, 512, 512, 512, 512, 512, 512, 512]

esp32.servos_set_position(positions)
