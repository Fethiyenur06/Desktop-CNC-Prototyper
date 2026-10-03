# 3-Axis Desktop CNC & PCB Prototyper

## Overview
This repository contains the mechanical architecture, electronic schematics, and control logic for a custom-built 3-axis desktop CNC milling machine. The system is specifically optimized for rapid PCB engraving, drilling, and small-scale mechanical prototyping. 

This project demonstrates a complete mechatronics workflow: from 3D CAD modeling and CAM generation to embedded motor control.

## System Architecture

### 1. Mechanical Design (CAD)
- **Modeling Software:** Fusion 360 
- **Structure:** Cartesian coordinate robot using NEMA 17 stepper motors, linear guide rails, and T8 lead screws for high-precision micro-stepping.
- **Spindle:** 775 DC Motor with ER11 collet for precise PCB milling bits.

### 2. Electronics (Hardware)
- **Controller:** Arduino Uno / Nano paired with CNC Shield (A4988 Stepper Drivers).
- **PCB Design:** Schematics drafted in EasyEDA for potential custom controller boards.
- **Safety Limits:** Integrated mechanical limit switches for homing and emergency stop interrupts.

### 3. Software & Control (Code)
- **Firmware:** GRBL (C/C++) for real-time G-Code parsing and trajectory planning.
- **Communication:** Python-based serial communication scripts to stream `.nc` / `.gcode` files from the host PC to the microcontroller.

## Repository Structure
- `/CAD_Files`: Contains `.step` and `.stl` files for 3D printed brackets and mechanical mounts.
- `/Electronics`: Schematics and wiring diagrams for the CNC control unit.
- `/Scripts`: Custom Python scripts for G-Code streaming and serial port monitoring.

---
*Note: This is an active open-source hardware project. 3D models and source code are updated iteratively based on machining tolerances.*
