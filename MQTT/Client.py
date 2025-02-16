import paho.mqtt.client as mqtt
import time

# Define the MQTT broker details
broker = "127.0.0.1"  # You can use any public MQTT broker or your own
port = 1883  # Default MQTT port
subscribe_topic = "iot/test/receive"  # Topic to subscribe to
publish_topic = "iot/test/receive"  # Topic to send messages to

# Define the callback function to handle received messages

def send_message(message):
    client.publish(publish_topic, message)
    #print(f"Sent message: {message} to topic: {publish_topic}")

def on_connect(client, userdata, flags, rc, x):
    print(f"Connected to MQTT broker with result code {rc}")
    # Subscribe to the topic
    client.subscribe(subscribe_topic)
    send_message("Hello world")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_start()

# Main loop
try:
    while True:
        message = input('->')
        send_message(message)
except KeyboardInterrupt:
    print("Disconnected from MQTT broker.")
    client.loop_stop()
