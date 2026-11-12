# UAS Pi 5 Autonomous Platforms

| Project | Description |
|---|---|
| [CrowDrone](./CrowDrone/) | Aerial platform — [Marvelmind/Pixhawk integration](./CrowDrone/DRONE_INTEGRATION.md) |
| [GroundRobots](./GroundRobots/turtlebot-navigation/) | TurtleBot2 indoor autonomous navigation |

## Repository layout

```
CrowDrone/                      # drone code (pymavlink → Pixhawk)
  drone.py, config.py, main.py
  test_connection.py, test_arming.py   # run from inside CrowDrone/
  requirements.txt
GroundRobots/turtlebot-navigation/
  marvelmind_fusion/            # deployed ROS 2 package: fusion, goto_goal, perimeter, calibration
  scripts/                      # standalone tools + earlier/alternate node versions
  diagnostics/                  # one-off sensor/serial debugging scripts
  nav2_config/  config/         # Nav2 launch/params/map; IMU params, yaw calibration
  kobuki_launch.py              # custom Kobuki launch
  requirements.txt              # pip deps; ROS deps come from apt
MARVELMIND.md, Pi_Hotspot_SSH_Guide.md   # shared docs
```

Install Python deps for a platform with `pip install -r <platform>/requirements.txt`.

## Shared

- **[Marvelmind Guide](./MARVELMIND.md)** — indoor positioning, used by both platforms. **Read before switching the hedgehog between projects.**
- [Pi Hotspot & SSH Guide](./Pi_Hotspot_SSH_Guide.md)

## Devices

| Platform | Hostname | Username | SSH |
|---|---|---|---|
| Drone | `bolzpi` | `pi` | `ssh pi@bolzpi.local` |
| Ground robot | `bolzpi2` | `uas` | `ssh uas@bolzpi2.local` |
