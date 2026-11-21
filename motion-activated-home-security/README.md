## Motion-Activated Home Security System Using Raspberry Pi

## Project Overview

This project focuses on developing a motion-activated home security system using Raspberry Pi, a PIR (Passive Infrared) motion sensor and a camera module. The system detects movement, triggers image/video capture and supports alert-based monitoring for enhanced home security.

## Project Objectives

Detect motion using a PIR sensor.

Trigger image or video capture when motion is detected.

Integrate hardware components with a Raspberry Pi for automated monitoring.

Enable alert-based notification and surveillance.

Develop an affordable and customizable security prototype.

## Hardware Components

Raspberry Pi

PIR Motion Sensor (HC-SR501 or equivalent)

Raspberry Pi Camera Module or USB Camera

MicroSD Card

Power Supply

Breadboard and Jumper Wires

Optional Buzzer and LEDs

## Software & Technologies

Python

Raspberry Pi OS (Linux-based)

GPIO Interface

OpenCV (for image/video processing, where implemented)

Camera Integration

System Architecture

Input Layer

The PIR motion sensor detects changes in infrared radiation associated with movement and sends a signal to the Raspberry Pi.

Processing Layer

The Raspberry Pi processes the sensor input and triggers the associated monitoring actions.

Output Layer

The system initiates image or video capture and supports notification and media storage functionality.

## Working Principle

The system continuously monitors the surroundings using the PIR motion sensor.

When movement is detected, the sensor sends a signal to the Raspberry Pi.

The Raspberry Pi processes the input and triggers the connected camera.

Images or videos are captured and stored for review.

Alert mechanisms can notify the user of detected activity.

## Technical Concepts

Raspberry Pi GPIO interfacing

PIR-based motion sensing

Embedded system integration

Camera interfacing

Python-based hardware control

Linux-based computing

IoT and remote monitoring concepts

## Reported Results

According to the project report:

Motion detection was reported within an approximate range of 5–7 metres.

Response time was reported as approximately 1–2 seconds.

Camera capture functionality was described at an average resolution of 720p.

Notification delivery was reported within approximately 5–10 seconds, depending on network connectivity.

A 24-hour continuous-operation test was reported.

## Limitations

False triggering due to environmental conditions.

Dependence on network connectivity for remote notifications.

Storage limitations for captured video.

Limited low-light performance without suitable camera or IR support.


Mobile application integration.

Multi-sensor integration.

Improved power efficiency and backup.


