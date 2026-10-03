import serial
import time

# CNC Machine Serial Configuration
# Adjust 'COM3' (Windows) or '/dev/ttyUSB0' (Linux) based on the hardware setup
SERIAL_PORT = 'COM3'
BAUD_RATE = 115200

def send_gcode_to_cnc(file_path):
    print(f"[INFO] Connecting to CNC Controller on {SERIAL_PORT}...")
    try:
        # Initialize serial connection to Arduino/CNC Shield
        cnc_serial = serial.Serial(SERIAL_PORT, BAUD_RATE)
        cnc_serial.write(b"\r\n\r\n") # Wake up GRBL firmware
        time.sleep(2)
        cnc_serial.flushInput()
        
        print(f"[INFO] Opening G-Code file: {file_path}")
        with open(file_path, 'r') as file:
            for line in file:
                cmd = line.strip()
                # Skip comments or empty lines in G-Code
                if cmd.startswith(';') or not cmd: 
                    continue 
                
                print(f"[TX] Sending: {cmd}")
                cnc_serial.write((cmd + '\n').encode('utf-8'))
                
                # Wait for 'ok' response from GRBL
                response = cnc_serial.readline().strip().decode('utf-8')
                print(f"[RX] Response: {response}")
                
        cnc_serial.close()
        print("[SUCCESS] Machining job completed successfully!")
        
    except Exception as e:
        print(f"[ERROR] Communication failure: {e}")

if __name__ == "__main__":
    # Execute the test routing
    send_gcode_to_cnc("test_routing_path.nc")
