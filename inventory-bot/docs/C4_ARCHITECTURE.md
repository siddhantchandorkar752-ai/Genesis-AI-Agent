# C4 Architecture: Autonomous Inventory Bot

## 1. System Context
The edge robot operating in the physical warehouse, intercepting imagery and performing inference while communicating with the central orchestrator via K3s.

## 2. Container Diagram

```mermaid
graph TD;
    RedTeam[Intruder 2D Spoof] --> CameraSensor;
    CameraSensor --> EdgeNode[K3s Pod / Jetson Nano];
    
    subgraph Edge Compute
    EdgeNode --> YOLO[YOLO11 3D Verifier];
    YOLO -->|Pass| VLM[Quantized Student VLM];
    YOLO -->|Fail| Alert[Security Alert to human];
    VLM --> NeuroSymbolic[Logic Engine];
    end
    
    NeuroSymbolic -->|DISCARD| RoboticArm[Actuate Claw to Discard Bin];
    NeuroSymbolic -->|KEEP| RoboticArm[Actuate Claw to Ship Bin];
```

### Sensor Spoofing Defense
The [RED] team spoofing (where an intruder uses printed 2D images to trick the system) is blocked at the `YOLO11 3D Verifier` phase, which validates the Z-depth of the bounding box before continuing to VLM.
