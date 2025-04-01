import json, time, torch
from pathlib import Path
from ruth.core import FractalSNN, QKEVerification
from ruth.monitoring.faw_monitor import FAWMonitor
from ruth.rcg.rcg_log import RCGLog
from ruth.repair.ruth_auto_repair import RuthAutoRepair
from ruth.trainers import OnlineTrainer

# Initialize model components
model = FractalSNN(input_size=3, hidden_size=8, output_size=5, depth=3)
qke = QKEVerification()
faw_monitor = FAWMonitor()
rcg_log = RCGLog()
trainer = OnlineTrainer()
auto_repair = RuthAutoRepair(model, trainer, qke, faw_monitor, rcg_log)

def read_sensor_input():
    try:
        with open("sensor_input.json", "r") as f:
            data = json.load(f)
            return torch.tensor([[data["vibration"], data["temperature"], data["pressure"]]], dtype=torch.float32)
    except:
        return None

while True:
    input_tensor = read_sensor_input()
    if input_tensor is None:
        time.sleep(1)
        continue

    output, attention = model([input_tensor])
    faw_monitor.update(attention)
    fault = auto_repair.detect_fault([input_tensor])

    print(f"Prediction: {output.argmax().item()}, Confidence: {1 - qke.verify(output.detach().numpy().max(), output.detach().numpy())}")
    if fault:
        auto_repair.run_repair([([input_tensor], torch.tensor([0]))], fault)
        print("[AutoRepair Triggered]", fault)
    time.sleep(1)
