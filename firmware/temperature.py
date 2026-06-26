from machine import Pin
import time
import onewire
import ds18x20

ow = onewire.OneWire(Pin(13))
ds = ds18x20.DS18X20(ow)

if __name__=="__main__":
    roms = ds.scan()
    print("initialization successful")
    while True:
        ds.convert_temp()
        time.sleep(1)
        for rom in roms: #might have multiple sensors on the same data line
            print("Temp：%.4f°C" %ds.read_temp(rom))
        

