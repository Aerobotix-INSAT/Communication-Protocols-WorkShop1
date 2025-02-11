# Introduction to Communication Protocols for IoT Devices

This repository contains simple implementations of various communication protocols. The goal is to introduce and explain the most common protocols in the context of IoT: MQTT, TCP, UDP, and HTTP (Flask).

Each protocol is presented with a basic client and/or server implementation to help you understand how communication happens in these environments.

## Project Structure

This project is organized into four main folders, each corresponding to a different communication protocol:

- **[MQTT](./MQTT)**: Simple MQTT client and server examples.
- **[TCP](./TCP)**: Simple TCP client and server examples.
- **[UDP](./UDP)**: Simple UDP client and server examples.
- **[HTTP (Flask)](./HTTP)**: Simple HTTP server using Flask with basic GET and POST routes.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package manager)
- **MQTT**: Install `paho-mqtt` library
- **Flask**: Install `Flask` library

To install the required dependencies for the entire project, run:

```bash
pip install -r requirements.txt
