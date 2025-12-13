
# 🤖 ROSA Turtlesim Simulation
### Natural Language Control of ROS 2 Robots

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
```yaml
conda create -n rosa_env python=3.10
conda activate rosa_env
```
### 2️⃣ Install ROSA
```yaml
pip3 install jpl-rosa
```
### 3️⃣ Clone the Repository
```yaml
git clone https://github.com/arjjann/rosa_turtlesim.git
cd rosa_turtlesim
```

### 4️⃣ Configure OpenAI / Azure Keys

Create a .env file in the project root directory:

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_DEPLOYMENT_NAME=your_deployment_name

    ⚠️ Do NOT commit the .env file to GitHub.

 #### How to Run

Source ROS 2 Jazzy:

    source /opt/ros/jazzy/setup.bash

Activate your Python environment:

    conda activate rosa_env

    Run the main program:

python main.py

#### Enter natural language commands:

    Move forward 3 meters
    Turn 90 degrees
    Draw a circle of radius 2

The turtle will respond in real time inside the Turtlesim window.
📸 Demo

## Testing & Debugging

    ros2 topic list
    ros2 topic echo /turtle1/cmd_vel



[ROSA (NASA JPL)](https://github.com/nasa-jpl/rosa)

[ROS 2 Jazzy Documentation](https://docs.ros.org/en/jazzy/)

[Gazebo Simulator](https://gazebosim.org/docs)

[LangChain](https://python.langchain.com/docs/)

[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
