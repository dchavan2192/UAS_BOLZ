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

A "fork" is your own personal copy of the repo on GitHub. You make changes there first, then ask to merge them back into the main repo.

1. Go to [github.com/dchavan2192/UAS_BOLZ](https://github.com/dchavan2192/UAS_BOLZ)
2. Click the **Fork** button (top right corner of the page)
3. On the "Create a new fork" page, leave everything as default and click **Create fork**
4. You now have your own copy at `github.com/YOUR_USERNAME/UAS_BOLZ`

### 4. Clone Your Fork to Your Computer

This downloads your fork so you can edit files locally:

```bash
git clone https://github.com/YOUR_USERNAME/UAS_BOLZ.git
cd UAS_BOLZ
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### 5. Add the Upstream Remote

This connects your local copy to the original (main) repo so you can stay up to date:

```bash
git remote add upstream https://github.com/dchavan2192/UAS_BOLZ.git
```

Verify both remotes are set up:

```bash
git remote -v
# You should see:
# origin    https://github.com/YOUR_USERNAME/UAS_BOLZ.git (fetch)   <-- your fork
# origin    https://github.com/YOUR_USERNAME/UAS_BOLZ.git (push)
# upstream  https://github.com/dchavan2192/UAS_BOLZ.git (fetch)     <-- main repo
# upstream  https://github.com/dchavan2192/UAS_BOLZ.git (push)
```

### 6. Create a Branch for Your Work

**Never work directly on `master`.** Always create a new branch — think of it as a separate workspace for your changes:

```bash
git checkout -b your-branch-name
```

Use a descriptive name, for example: `fix-fusion-node-timeout`, `add-lidar-support`, `update-nav2-params`.

### 7. Make Your Changes

Edit files, add new scripts, fix bugs, etc. When you're done, check what changed:

```bash
git status          # shows which files you modified or added
git diff            # shows the actual line-by-line changes
```

### 8. Stage, Commit, and Push Your Changes

This is a three-step process: **stage** (pick which files to include) -> **commit** (save a snapshot with a message) -> **push** (upload to your fork on GitHub).

```bash
# Stage the files you changed
git add file1.py file2.py

# Commit with a clear message explaining WHAT you changed and WHY
git commit -m "Fix fusion node crash when IMU disconnects"

# Push your branch to your fork on GitHub
git push origin your-branch-name
```

**Commit message tips:**
- Good: `"Fix fusion node crash when IMU disconnects"`, `"Add goto_goal timeout parameter"`
- Bad: `"stuff"`, `"updates"`, `"fixed it"`

If you changed many files and want to stage them all:

```bash
git add -A                   # stages everything
git status                   # REVIEW what's staged before committing
git commit -m "Your message"
git push origin your-branch-name
```

### 9. Open a Pull Request (PR) to Merge Back to the Main Repo

A Pull Request says "hey, I made these changes in my fork — please review and merge them into the main repo."

1. Go to your fork on GitHub (`github.com/YOUR_USERNAME/UAS_BOLZ`)
2. You'll see a yellow banner saying **"Compare & pull request"** — click it
3. Make sure the base says `dchavan2192/UAS_BOLZ` `master` and the head says `YOUR_USERNAME/UAS_BOLZ` `your-branch-name`
4. Write a short description of what your changes do and why
5. Click **Create pull request**

Someone will review your code and either merge it or leave comments for changes.

### 10. Keeping Your Fork Up to Date

Other people will merge changes into the main repo. Before starting new work, always pull those changes into your fork:

```bash
# Switch back to master
git checkout master

# Pull the latest from the main repo
git pull upstream master

# Push it to your fork so it's also up to date
git push origin master

# Now create a new branch for your next task
git checkout -b my-next-feature
```

### Common Mistakes and How to Fix Them

| Mistake | Fix |
|---|---|
| Committed to `master` instead of a branch | `git checkout -b new-branch` (moves your commits to a new branch) |
| Forgot to pull before starting work | `git pull upstream master` then `git merge master` into your branch |
| Pushed the wrong file (e.g. `.DS_Store`) | Add it to `.gitignore`, then `git rm --cached .DS_Store` and commit |
| Commit message has a typo | `git commit --amend -m "New message"` (only if you haven't pushed yet) |
| Want to undo your last commit (not pushed) | `git reset --soft HEAD~1` (keeps your changes, undoes the commit) |

### Tips

- **Ask questions.** If something in the codebase is confusing, open a GitHub Issue or ask in the group chat.
- **Test before pushing.** If you changed a script, run it and make sure it works.
- **One feature per branch.** Don't mix unrelated changes in the same pull request.
- **Pull before you push.** Always sync with upstream before starting new work.
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

## Pi SD Card Backups

Full disk images of the Pi SD cards are stored in **Microsoft Teams** (too large for GitHub):

> **UAS BOLZ** team -> **UAS-BUILD** channel -> **Big Drone** folder

Backup images are byte-for-byte copies of the entire SD card — both the boot partition and the Linux root filesystem. They contain the full OS, all installed packages, ROS 2, the workspace, config files, and everything needed to get a Pi running identically.

| Image | Platform | Date | Contents |
|---|---|---|---|
| `bolzpi_crowdrone_2026-11-12.img.gz` | CrowDrone (`bolzpi`) | 2026-11-12 | Raspberry Pi OS + pymavlink + drone_project + mavenv |

### Restoring a Backup to an SD Card

You need: a microSD card (same size or larger than the original) and a card reader.

#### Option A — Raspberry Pi Imager (easiest)

1. Download and open [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Click **Choose OS** -> scroll to bottom -> **Use custom**
3. Select the `.img.gz` file (no need to decompress it — Imager handles `.gz` natively)
4. Click **Choose Storage** and select your SD card
5. Click **Write** and wait for it to finish
6. Eject the card and plug it into the Pi

#### Option B — Command line (macOS/Linux)

```bash
# 1. Find your SD card device (be VERY careful to pick the right disk)
diskutil list                 # look for your SD card size, e.g. /dev/disk5

# 2. Unmount it (do NOT eject — just unmount)
diskutil unmountDisk /dev/diskN

# 3. Write the image (replace diskN with your actual disk number)
#    Use rdiskN (raw disk) for much faster writes
gunzip -c bolzpi_crowdrone_2026-11-12.img.gz | sudo dd of=/dev/rdiskN bs=4m status=progress

# 4. Eject when done
diskutil eject /dev/diskN
```

**WARNING:** `dd` will overwrite whatever disk you point it at with no confirmation. Triple-check the disk number. If you write to the wrong disk, you will erase that drive.

#### After Restoring

- The Pi should boot and connect to the last-configured WiFi network automatically
- SSH in with the credentials from the [Devices](#devices) table above
- If the Pi doesn't appear on the network, connect a monitor + keyboard to troubleshoot WiFi

### Creating a New Backup

To back up a Pi's SD card for safekeeping or before making risky changes:

```bash
# 1. Shut down the Pi cleanly
ssh pi@bolzpi.local "sudo shutdown -h now"

# 2. Remove the SD card from the Pi and insert it into your Mac

# 3. Find the disk number
diskutil list                 # e.g. /dev/disk5

# 4. Create the compressed image
sudo dd if=/dev/rdiskN bs=4m status=progress | gzip -1 > bolzpi_YYYY-MM-DD.img.gz

# 5. Eject the card
diskutil eject /dev/diskN
```

The compressed image is typically 2-4 GB for an 8 GB card (depending on how full it is).

---

## Contact

For questions about this project, reach out to **Dhruv Chavan** — [chavan.36@osu.edu](mailto:chavan.36@osu.edu)

## License

This project is developed for academic research at the BOLZ Lab.
