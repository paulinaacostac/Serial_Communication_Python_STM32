#!/usr/bin/python3
import time
import serial

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")


serial_port = serial.Serial(
    #port="/dev/ttyTHS2",
    port="COM5",
    baudrate=38400,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0.5,
    inter_byte_timeout=0.1
)
# Wait a second to let the port initialize
time.sleep(5)

try:
    # Send a simple header
    mensaje = "UART Demonstration Program"
    serial_port.write(mensaje.encode('utf-8'))
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.readline()
            print(data)
            #serial_port.write(data)
            # if we get a carriage return, add a line feed too
            # \r is a carriage return; \n is a line feed
            # This is to help the tty program on the other end
            # Windows is \r\n for carriage return, line feed
            # Macintosh and Linux use \n
            if data == "\r".encode('utf-8'):
                # For Windows boxen on the other end
                serial_port.write("\n".encode('utf-8'))


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
