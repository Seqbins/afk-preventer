# AFK Preventer

A lightweight Python script that simulates periodic key presses to keep your system active and prevent it from going idle or entering sleep/AFK mode.

---

## Features

- **Customizable interval** — set the time between key presses to suit your needs
- **Key selection** — choose any valid keyboard key (defaults to `shift`)
- **Natural randomization** — slight timing variation to mimic real key presses
- **Cross-platform** — works on macOS, Linux, and Windows
- **Lightweight** — minimal dependencies, easy to run

---

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script:

```bash
python afk_preventer.py
```

You will be prompted to:

1. **Enter the time interval** (in seconds) between key presses
2. **Choose a key** to simulate (press Enter to use the default: `shift`)

The script will then keep pressing the selected key at the specified interval until you stop it.

To stop the script at any time, press:

```
Ctrl + C
```

---

## Use Cases

- 🎮 **Games** — stay marked as active and avoid being kicked for inactivity in online games
- 💬 **Chat & messaging apps** — keep your status as "online" or "active"
- 🖥️ **Remote desktop / VMs** — prevent idle disconnects during long sessions
- ⏳ **Long-running tasks** — stop your screen from locking while waiting for downloads, renders, or builds
- 🏢 **Work apps** — keep activity status green in tools like Teams or Slack

---

## Platform Notes

### macOS

You may need to grant Accessibility permissions before the script can simulate key presses:

```
System Settings → Privacy & Security → Accessibility
```

### Linux

Requires a display server (X11 or Wayland). Make sure the `DISPLAY` or `WAYLAND_DISPLAY` environment variable is set in your session.

### Windows

No special setup is typically required.

---

## Disclaimer

This tool is intended for personal use only. Be aware that some games, applications, and workplace platforms explicitly prohibit the use of automation tools or AFK prevention scripts in their Terms of Service. Using this script in those contexts may result in penalties, bans, or other consequences. Always check the rules of the game or platform before use, and use responsibly.

---

## License

This project is open-source and available under the [MIT License](LICENSE).