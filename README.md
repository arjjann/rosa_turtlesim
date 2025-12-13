🛠️ Installation & Setup

Follow these steps to set up the necessary environment and clone the repository.
Prerequisites

    A working installation of ROS 2 (Humble or Jazzy).

    Conda or Mamba for environment management.

Steps

    Create and activate the dedicated Python environment

    Install the ROSA library

    Clone the project repository

    Install specific project dependencies

🏃 Running the Program

Follow these steps to launch the ROS 2 simulation and start the control script.

    Source your ROS 2 environment (Important! Use the command appropriate for your shell)

    Activate the ROSA environment

    Launch the Turtlesim simulation

    In a new terminal, run the ROSA control script (ensure you have sourced ROS 2 and activated rosa_env in this terminal too)

    Provide commands You can now type natural language instructions, such as:

        Move forward 2 units, then turn 90 degrees left.

        Draw a small square.

        Stop moving and reset the simulation.

📸 Screenshots and GIFs

Watch the ROSA agent control the Turtlesim robot using only natural language instructions!
🛣️ Future Enhancements / Roadmap

    Waypoint Navigation: Implement ability to navigate to specific coordinates.

    Voice-based Control: Integrate a speech-to-text module for hands-free operation.

    Multi-robot Support: Extend the framework to coordinate control of multiple Turtlesim instances.

    Integration with Real Hardware: Adapt the tools layer for physical robots (e.g., TurtleBot 4).

🔬 Testing & Debugging

These commands are useful for verifying the ROS 2 environment and monitoring the robot's commands. Run these in a separate terminal after launching the simulation.
List Active ROS 2 Topics
Echo Command Velocity

Use this to see the raw velocity messages being sent to the robot.
⚙️ Technologies Used
🔗 Sources & References

    : Official documentation and source code for the ROSA framework.

    : Official documentation for the ROS 2 ecosystem.

🙏 Acknowledgements

A special thanks to the developers of the ROSA framework for creating an intuitive and powerful tool for robotics control.

Enjoy using ROSA! If you find this project useful, please consider starring the repository!
