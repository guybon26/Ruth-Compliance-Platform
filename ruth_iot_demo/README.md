# Ruth IoT Simulation Demo

This demo simulates real-time sensor data and runs it through Ruth's FractalSNN to test anomaly detection and self-repair mechanisms.

## Files:
- `iot_simulator.py`: Generates fake industrial sensor data.
- `ruth_iot_listener.py`: Loads sensor data, passes it to Ruth, logs predictions and triggers repair.

## How to Run
1. Start the simulator:
```bash
python iot_simulator.py
```
2. In another terminal, start the listener:
```bash
python ruth_iot_listener.py
```
