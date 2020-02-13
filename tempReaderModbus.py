#!/usr/bin/env python
import minimalmodbus
import time


# Temperature sensor
#
# Temperature reading is:
# Device Address: 0x01
# Function code:  0x04


# Device configuration

# slave address (in decimal)
DEVICE_ADDRESS = 1
# ENABLE/DISABLE communication debug mode
DEVICE_DEBUG = True
# Master PORT name.
PORT_NAME = '/dev/ttyUSB0'

# MODBUS instrument initialization
instrument = minimalmodbus.Instrument(PORT_NAME, DEVICE_ADDRESS, debug=DEVICE_DEBUG)

# MODBUS instrument connection settings
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity   = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
instrument.serial.timeout = 0.2

# Print MODBUS configuration
print ("MODBUS Configuration\n")
print ("********************\n")
print (instrument)
print ("\n********************\n")

# Read Temperature
REGISTER_ADDRESS_TEMP = 1
REGISTER_NUMBER_DECIMALS = 1
ModBus_Command = 4

while True:
    # Register number, number of decimals, function code
#    temperature = instrument.read_register(1, 2, 4)
    temperature = instrument.read_register(REGISTER_ADDRESS_TEMP, REGISTER_NUMBER_DECIMALS, ModBus_Command)
    try:
        print(temperature)
        temp_celcius = temperature / 10
    except IOError:
        print("Failed to read from instrument")
    time.sleep(1)