# Sleek Terminal Music Player

![Terminal Music Player](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A feature-rich terminal music player built with Python, VLC, and Rich for beautiful terminal interfaces. Control your music with keyboard commands while enjoying a visually appealing interface with playlist management, volume control, and playback features.

## ✨ Features

- **Modern Terminal UI**: Beautiful interface using Rich library with panels, tables, and formatted text
- **Playlist Management**:
  - Create multiple named playlists
  - Switch between playlists
  - Add/remove songs from playlists
- **Playback Controls**:
  - Play/pause toggle
  - Next/previous track navigation
  - Shuffle mode
  - Loop mode
- **Audio Controls**:
  - Volume adjustment (0-100)
  - Mute toggle
- **File Support**: Plays any audio format supported by VLC
- **Keyboard Commands**: Intuitive command-based interface

## 🚀 Installation

1. Ensure you have Python 3.7+ installed
2. Install required dependencies:

```bash
pip install python-vlc rich keyboard
```

3. Download the script:

```bash
wget https://raw.githubusercontent.com/funterminal/music.sh/refs/heads/main/music.py
```

## 🎛 Usage

Run the player:
```bash
python3 music.py
```

### Command Reference

| Command       | Description                          | Example                     |
|---------------|--------------------------------------|-----------------------------|
| `play <file>` | Play specified file                  | `play song.mp3`             |
| `list`        | Show current playlist                | `list`                      |
| `add <file>`  | Add file to current playlist         | `add song.mp3`              |
| `remove <file>` | Remove file from playlist          | `remove song.mp3`           |
| `create <name>` | Create new playlist                | `create workout`            |
| `switch <name>` | Switch to different playlist      | `switch workout`            |
| `shuffle`     | Toggle shuffle mode                  | `shuffle`                   |
| `pause`      | Toggle play/pause                    | `pause`                     |
| `volume <0-100>` | Set volume level                 | `volume 80`                 |
| `loop`       | Toggle loop mode                     | `loop`                      |
| `next`       | Play next track                      | `next`                      |
| `prev`       | Play previous track                  | `prev`                      |
| `mute`       | Toggle mute                          | `mute`                      |
| `quit`       | Exit the player                      | `quit`                      |

## 🛠 Technical Details

### Architecture

- **VLC Integration**: Uses python-vlc binding for robust audio playback
- **Rich UI**: Implements panels, tables, and formatted text for beautiful output
- **State Management**: Tracks player state (volume, mute, shuffle, loop) globally
- **Playlist System**: Supports multiple named playlists with easy switching

### Key Components

1. **Player Core**:
   - VLC MediaPlayer instance
   - Volume and mute controls
   - Playback state tracking

2. **Playlist System**:
   - Dictionary-based playlist storage
   - Current playlist tracking
   - Index-based navigation

3. **UI Layer**:
   - Rich console output
   - Status panel with current settings
   - Tabular playlist display

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## 📚 Dependencies

- [python-vlc](https://wiki.videolan.org/PythonBinding/)
- [Rich](https://github.com/Textualize/rich)
- [keyboard](https://github.com/boppreh/keyboard)

Enjoy your music in the terminal! 🎧