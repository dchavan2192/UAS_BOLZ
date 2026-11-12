# Pi SD Card Backups

Full disk images of the Pi SD cards are stored in **Microsoft Teams** (too large for GitHub):

> **UAS BOLZ** team -> **UAS-BUILD** channel -> **Big Drone** folder

Backup images are byte-for-byte copies of the entire SD card — both the boot partition and the Linux root filesystem. They contain the full OS, all installed packages, ROS 2, the workspace, config files, and everything needed to get a Pi running identically.

| Image | Platform | Date | Contents |
|---|---|---|---|
| `bolzpi_crowdrone_2026-11-12.img.gz` | CrowDrone (`bolzpi`) | 2026-11-12 | Raspberry Pi OS + pymavlink + drone_project + mavenv |

## Restoring a Backup to an SD Card

You need: a microSD card (same size or larger than the original) and a card reader.

### Option A — Raspberry Pi Imager (easiest)

1. Download and open [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Click **Choose OS** -> scroll to bottom -> **Use custom**
3. Select the `.img.gz` file (no need to decompress it — Imager handles `.gz` natively)
4. Click **Choose Storage** and select your SD card
5. Click **Write** and wait for it to finish
6. Eject the card and plug it into the Pi

### Option B — Command line (macOS/Linux)

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

### After Restoring

- The Pi should boot and connect to the last-configured WiFi network automatically
- SSH in with the credentials from the [Devices table](./README.md#devices) in the main README
- If the Pi doesn't appear on the network, connect a monitor + keyboard to troubleshoot WiFi

## Creating a New Backup

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

Upload the image to the **Big Drone** folder on Teams when done.
