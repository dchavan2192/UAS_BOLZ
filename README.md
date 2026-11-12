# UAS BOLZ — Indoor Autonomous Platforms

Research platforms for GPS-denied indoor autonomous navigation, developed at the BOLZ Lab.

Two platforms share a common Marvelmind indoor positioning system:

| Platform | Description | Status |
|---|---|---|
| [GroundRobots](./GroundRobots/turtlebot-navigation/) | TurtleBot2 + Pi 5 + ROS 2 Jazzy + Marvelmind + MicroStrain IMU | Active |
| [CrowDrone](./CrowDrone/) | 10.5" quadcopter + Pixhawk 6C + ArduPilot + Marvelmind NMEA | Active |

## Demo

https://github.com/dchavan2192/UAS_BOLZ/raw/master/media/autonomous_indoor_robot_demo.mp4

---

## Repository Structure

```
UAS_BOLZ/
├── CrowDrone/                          # Drone platform (pymavlink + Pixhawk)
│   ├── drone.py                        # Core flight control
│   ├── config.py                       # Connection/flight parameters
│   ├── main.py                         # Takeoff/land test entry point
│   ├── test_connection.py              # Verify Pixhawk serial link
│   ├── test_arming.py                  # Arming sequence test
│   ├── requirements.txt                # Python dependencies
│   └── DRONE_INTEGRATION.md           # Marvelmind/Pixhawk wiring and params
│
├── GroundRobots/turtlebot-navigation/  # Ground robot platform (ROS 2)
│   ├── marvelmind_fusion/              # Deployed ROS 2 package (ament_python)
│   │   └── marvelmind_fusion/
│   │       ├── fusion_node.py          # Marvelmind + IMU -> odometry + TF
│   │       ├── goto_goal.py            # Turn-then-drive waypoint controller
│   │       ├── goto_goal_obstacle.py   # Waypoint nav with obstacle detours
│   │       ├── perimeter.py            # Beacon-bounded perimeter run
│   │       └── calibrate_yaw.py        # IMU yaw offset calibration
│   ├── scripts/                        # Standalone tools and earlier node versions
│   ├── diagnostics/                    # IMU/serial debugging scripts
│   ├── nav2_config/                    # Nav2 launch, params, static map
│   ├── config/                         # IMU params, yaw calibration data
│   ├── kobuki_launch.py                # Custom Kobuki launch (TF off, odom remapped)
│   ├── requirements.txt                # Python dependencies
│   └── README.md                       # Full build guide (20 phases)
│
├── media/                              # Demo videos and images
│   └── Autonomous Indoor Robot Demo.MOV
│
├── MARVELMIND.md                       # Shared Marvelmind hardware guide
├── Pi_Hotspot_SSH_Guide.md             # How to connect to the Pi over SSH
└── .gitignore
```

---

## Quick Start

### Prerequisites

- A computer with Git installed
- Python 3.10+
- For the ground robot: a Raspberry Pi 5 running Ubuntu 24.04 + ROS 2 Jazzy
- For the drone: Mission Planner + a Pixhawk 6C

### Clone the Repo

```bash
git clone https://github.com/dchavan2192/UAS_BOLZ.git
cd UAS_BOLZ
```

### Install Dependencies

```bash
# Drone platform
pip install -r CrowDrone/requirements.txt

# Ground robot platform
pip install -r GroundRobots/turtlebot-navigation/requirements.txt
```

### Read the Platform Guides

- **Ground robot (start here):** [GroundRobots/turtlebot-navigation/README.md](./GroundRobots/turtlebot-navigation/README.md) — full build guide from Pi setup through autonomous navigation
- **Drone:** [CrowDrone/DRONE_INTEGRATION.md](./CrowDrone/DRONE_INTEGRATION.md) — Marvelmind/Pixhawk wiring, ArduPilot parameters, EKF3 config
- **Marvelmind (both platforms):** [MARVELMIND.md](./MARVELMIND.md) — beacon placement, protocol switching, troubleshooting. **Read this before switching the hedgehog between projects.**
- **SSH into the Pi:** [Pi_Hotspot_SSH_Guide.md](./Pi_Hotspot_SSH_Guide.md)

---

## Devices

| Platform | Hostname | Username | SSH Command |
|---|---|---|---|
| Drone Pi | `bolzpi` | `pi` | `ssh pi@bolzpi.local` |
| Ground robot Pi | `bolzpi2` | `uas` | `ssh uas@bolzpi2.local` |

---

## Contributing (For New Members)

Welcome! This section walks you through how to contribute code to this repo. No prior Git experience is assumed.

### 1. Install Git

- **Mac:** Open Terminal and run `xcode-select --install`
- **Windows:** Download from [git-scm.com](https://git-scm.com/downloads)
- **Linux:** `sudo apt install git`

### 2. Set Up Your GitHub Account

If you don't have one, create a free account at [github.com](https://github.com).

Configure Git with your name and email (use the email linked to your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Fork the Repository

1. Go to [github.com/dchavan2192/UAS_BOLZ](https://github.com/dchavan2192/UAS_BOLZ)
2. Click the **Fork** button (top right)
3. This creates a copy of the repo under your own GitHub account

### 4. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/UAS_BOLZ.git
cd UAS_BOLZ
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 5. Add the Upstream Remote

This lets you pull in new changes from the main repo:

```bash
git remote add upstream https://github.com/dchavan2192/UAS_BOLZ.git
```

Verify both remotes are set up:

```bash
git remote -v
# origin    https://github.com/YOUR_USERNAME/UAS_BOLZ.git (fetch)
# origin    https://github.com/YOUR_USERNAME/UAS_BOLZ.git (push)
# upstream  https://github.com/dchavan2192/UAS_BOLZ.git (fetch)
# upstream  https://github.com/dchavan2192/UAS_BOLZ.git (push)
```

### 6. Create a Branch for Your Work

Never work directly on `master`. Always create a new branch:

```bash
git checkout -b your-branch-name
```

Use a descriptive name, for example: `fix-fusion-node-timeout`, `add-lidar-support`, `update-nav2-params`.

### 7. Make Your Changes

Edit files, add new scripts, etc. When you're done, check what changed:

```bash
git status          # shows modified/new files
git diff            # shows the actual changes
```

### 8. Stage and Commit

```bash
git add file1.py file2.py    # stage specific files
git commit -m "Short description of what you changed"
```

Write clear commit messages. Good: `"Fix fusion node crash when IMU disconnects"`. Bad: `"stuff"`.

### 9. Push to Your Fork

```bash
git push origin your-branch-name
```

### 10. Open a Pull Request

1. Go to your fork on GitHub (`github.com/YOUR_USERNAME/UAS_BOLZ`)
2. You'll see a banner saying "Compare & pull request" — click it
3. Write a short description of what your changes do and why
4. Click **Create pull request**

Someone will review your changes and merge them, or leave feedback.

### Keeping Your Fork Up to Date

Before starting new work, always sync with the latest changes:

```bash
git checkout master
git pull upstream master
git push origin master
```

Then create a new branch from the updated `master`.

### Tips

- **Ask questions.** If something in the codebase is confusing, open a GitHub Issue or ask in the group chat.
- **Test before pushing.** If you changed a script, run it and make sure it works.
- **One feature per branch.** Don't mix unrelated changes in the same pull request.
- **Read the platform README** for whichever platform you're working on — they document known issues, gotchas, and the reasoning behind design decisions.

---

## Architecture Overview

Both platforms use Marvelmind ultrasonic indoor positioning as their primary position source:

```
[Stationary Beacons (4-6)]
        |  ultrasonic ranging
        v
   [Hedgehog (mobile beacon)]
        |
        +--- NMEA over UART ---> [Pixhawk 6C]  (drone)
        |
        +--- Binary over USB --> [Raspberry Pi 5] + IMU --> ROS 2 --> [Kobuki base]  (ground robot)
```

The hedgehog can only output one protocol at a time (NMEA or Marvelmind binary). See [MARVELMIND.md](./MARVELMIND.md) for how to switch between platforms.

---

## License

This project is developed for academic research at the BOLZ Lab.
