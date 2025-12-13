# 🤖 ROSA Turtlesim Simulation
### Natural Language Control of ROS 2 Robots

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![ROS 2 Jazzy](https://img.shields.io/badge/ROS2-Jazzy-green)](https://docs.ros.org/en/jazzy/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📌 Overview
**ROSA** is an AI-powered assistant for **ROS 1 and ROS 2**, developed by NASA JPL and built on the **LangChain framework**.  
This project demonstrates how **Turtlesim** can be controlled using **natural language commands**, enabling intuitive human–robot interaction.

---

## ⚙️ Installation & Setup

### 1️⃣ Create Python / Conda Environment & Install Everything
> ⚠️ Ensure your Python version matches your ROS 2 Python version
```bash
# Create and activate Python environment
conda create -n rosa_env python=3.10
conda activate rosa_env

# Install ROSA
pip3 install jpl-rosa

# Clone the repository
git clone https://github.com/arjjann/rosa_turtlesim.git
cd rosa_turtlesim

# Configure OpenAI / Azure Keys
echo "AZURE_OPENAI_API_KEY=your_api_key" >> .env
echo "AZURE_OPENAI_ENDPOINT=your_endpoint" >> .env
echo "AZURE_DEPLOYMENT_NAME=your_deployment_name" >> .env
# ⚠️ Do NOT commit the .env file to GitHub

# Source ROS 2 Jazzy
source /opt/ros/jazzy/setup.bash

# Activate Python environment again (if needed)
conda activate rosa_env

# Run the main program
python main.py

# Example commands to enter
# Move forward 3 meters
# Turn 90 degrees
# Draw a circle of radius 2

# Testing & debugging
ros2 topic list
ros2 topic echo /turtle1/cmd_vel
