import requests
import random
import time

# Replace these with your actual channel details
API_KEY = "SO7UMJBWZIGVT39K"  # Replace with your ThingSpeak Write API key
URL = "https://api.thingspeak.com/update"

while True:
    temperature = round(random.uniform(20, 35), 2)  # Simulated temp
    humidity = round(random.uniform(40, 80), 2)     # Simulated humidity

    payload = {
        "api_key": API_KEY,
        "field1": temperature,
        "field2": humidity
    }

    response = requests.post(URL, data=payload)
    print(f"Sent → Temp: {temperature} °C, Humidity: {humidity} % → Status: {response.status_code}")

    time.sleep(15)  # ThingSpeak allows 1 update every 15 seconds


    # import requests
# import time

# # Replace with your ThingSpeak Write API Key
# API_KEY = "YOUR_WRITE_API_KEY"  
# URL = "https://api.thingspeak.com/update"

# # Initial simulated sensor values
# temperature = 20.0  # Start at 20°C
# humidity = 80.0     # Start at 80%

# while True:
#     # Send data to ThingSpeak
#     payload = {
#         "api_key": API_KEY,
#         "field1": round(temperature, 2),
#         "field2": round(humidity, 2)
#     }

#     response = requests.post(URL, data=payload)
    
#     if response.status_code == 200:
#         print(f"✅ Sent → Temperature: {temperature}°C, Humidity: {humidity}%")
#     else:
#         print(f"❌ Failed to send data. Status Code: {response.status_code}")

#     # Simulate sensor behavior
#     temperature += 1.0         # Increase temp by 1°C
#     humidity -= 0.5            # Decrease humidity slightly

#     # Reset values for realism
#     if temperature > 40:
#         temperature = 20.0
#     if humidity < 40:
#         humidity = 80.0

#     # Wait before next update
#     time.sleep(15)  # ThingSpeak minimum update interval






# https://api.thingspeak.com/update?api_key=RBKWJ9P0B3TD4A91&field1=29.4&field2=62.7





# void setup() {
#   Serial.begin(9600);
# }

# void loop() {
#   int analogValue = analogRead(A0); // Read from potentiometer
#   float temperature = map(analogValue, 0, 1023, 20, 40); // Map to 20–40°C

#   Serial.print("Temperature: ");
#   Serial.println(temperature);

#   delay(30000); // 5 seconds delay
# }


# Left Pin	5V (Red)
# Middle Pin	A0 (Analog In)
# Right Pin	GND (Black)