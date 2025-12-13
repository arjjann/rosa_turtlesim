# 🤖 ROSA Turtlesim Simulation
### Natural Language Control of ROS 2 Robots

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![ROS 2 Jazzy](https://img.shields.io/badge/ROS2-Jazzy-green)](https://docs.ros.org/en/jazzy/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/arjjann/rosa_turtlesim)](https://github.com/arjjann/rosa_turtlesim/stargazers)

---

## 📌 Overview
**ROSA** is an AI-powered assistant for **ROS 1 and ROS 2**, developed by NASA JPL and built on the **LangChain framework**.  
This project demonstrates how **Turtlesim** can be controlled using **natural language commands** through ROSA, enabling intuitive and intelligent human–robot interaction.

---

## ✨ Features
- 🧠 Natural language control using LLMs  
- 🐢 Control Turtlesim robot movements  
- 🔁 Forward / backward motion  
- ↩️ Clockwise / anticlockwise turning  
- 🔵 Circle trajectory execution  
- 🔗 ROS 2 + ROSA integration  
- 🚀 Beginner-friendly AI + robotics project  

---

## 🧩 System Architecture

User Command
↓
ROSA (LLM Agent)
↓
ROS 2 Tools (@tool)
↓
Turtlesim Robot


---

## ⚙️ Installation & Setup

### 1️⃣ Create Python / Conda Environment
> ⚠️ Ensure your Python version matches your ROS 2 Python version
```bash
conda create -n rosa_env python=3.10
conda activate rosa_env

### 2️⃣ Install ROSA

pip3 install jpl-rosa

3️⃣ Clone the Repository

git clone https://github.com/arjjann/rosa_turtlesim.git
cd rosa_turtlesim

4️⃣ Configure OpenAI / Azure Keys

Create a .env file in the project root directory:

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_DEPLOYMENT_NAME=your_deployment_name

    ⚠️ Do NOT commit the .env file to GitHub.

▶️ How to Run

    Source ROS 2 Jazzy:

source /opt/ros/jazzy/setup.bash

    Activate your Python environment:

conda activate rosa_env

    Run the main program:

python main.py

    Enter natural language commands:

Move forward 3 meters
Turn 90 degrees
Draw a circle of radius 2

The turtle will respond in real time inside the Turtlesim window.
📸 Demo

Add screenshots or GIFs to improve visualization

![ROSA Turtlesim Demo](assets/demo.gif)

🔮 Future Enhancements

    🧭 Waypoint navigation using pose feedback

    🗣️ Voice-based robot control

    🤖 Multi-robot control using namespaces

    📊 Robot status feedback (pose, orientation)

    🧠 Advanced task sequencing and planning

    🌍 Migration to Gazebo with URDF-based robots

🧪 Testing & Debugging

ros2 topic list
ros2 topic echo /turtle1/cmd_vel

🛠️ Technologies Used
Technology	Description
ROS 2 Jazzy	Robot middleware
Turtlesim	2D robot simulation
ROSA	LLM-based robot assistant
LangChain	AI tool orchestration
Python	Core programming language
Azure OpenAI	LLM backend
📚 Sources & References

    ROSA (NASA JPL)
    https://github.com/nasa-jpl/rosa


https://github.com/nasa-jpl/rosa/tree/main

ROS 2 Jazzy Documentation
https://docs.ros.org/en/jazzy/

https://docs.ros.org/en/jazzy/Tutorials.html

Turtlesim
https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Introducing-Turtlesim.html

Gazebo Simulator
https://gazebosim.org/docs

https://gazebosim.org/docs/latest/ros2_integration

LangChain
https://python.langchain.com/docs/

Azure OpenAI
https://learn.microsoft.com/en-us/azure/ai-services/openai/
🙌 Acknowledgements

    NASA Jet Propulsion Laboratory (JPL)

    ROS 2 Open Source Community

    Gazebo Simulation Developers

📌 Notes

    This project is intended for educational and research purposes

    Internet connection is required for LLM usage

    Ensure ROS and Python environments are compatible
