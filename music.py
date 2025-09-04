import os
import random
import time
import vlc
import keyboard
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

playlists = {}
current_playlist = []
current_index = 0
is_paused = False
is_shuffle = False
is_looping = False
current_volume = 100
is_muted = False
player = None
current_playlist_name = "Default"
playlists[current_playlist_name] = []

def ui_header():
    console.clear()
    console.rule("[bold cyan]Sleek Terminal Music Player[/bold cyan]")
    status = f"[green]Playing[/green]" if not is_paused else "[yellow]Paused[/yellow]"
    console.print(Panel.fit(f"[bold]Playlist:[/bold] {current_playlist_name}    "
                            f"[bold]Volume:[/bold] {current_volume}    "
                            f"[bold]Status:[/bold] {status}    "
                            f"[bold]Loop:[/bold] {is_looping}    "
                            f"[bold]Shuffle:[/bold] {is_shuffle}    "
                            f"[bold]Muted:[/bold] {is_muted}",
                            title="[bold magenta]Now Playing Info", expand=False))

def file_exists(file):
    return os.path.isfile(file)

def play_music(file):
    global player
    if not file_exists(file):
        console.print(f"[bold red]File not found:[/bold red] {file}")
        return
    stop_music()
    media = vlc.MediaPlayer(file)
    media.audio_set_volume(current_volume)
    player = media
    player.play()
    console.print(f"[bold green]Now playing:[/bold green] {file}")
    time.sleep(1)

def stop_music():
    global player
    if player:
        player.stop()

def list_playlist():
    if not current_playlist:
        console.print("[bold red]Playlist is empty[/bold red]")
        return
    table = Table(title=f"Playlist: {current_playlist_name}")
    table.add_column("Index", style="cyan")
    table.add_column("Song", style="magenta")
    for i, song in enumerate(current_playlist):
        table.add_row(str(i + 1), song)
    console.print(table)

def add_to_playlist(file):
    if not file_exists(file):
        console.print(f"[bold red]File not found:[/bold red] {file}")
        return
    current_playlist.append(file)
    playlists[current_playlist_name] = current_playlist
    console.print(f"[bold green]Added to playlist:[/bold green] {file}")

def remove_from_playlist(file):
    if file in current_playlist:
        current_playlist.remove(file)
        console.print(f"[bold green]Removed from playlist:[/bold green] {file}")
    else:
        console.print(f"[bold red]File not in playlist:[/bold red] {file}")

def create_playlist(name):
    if name in playlists:
        console.print(f"[bold red]Playlist already exists:[/bold red] {name}")
        return
    playlists[name] = []
    console.print(f"[bold green]Created playlist:[/bold green] {name}")

def switch_playlist(name):
    global current_playlist, current_playlist_name
    if name not in playlists:
        console.print(f"[bold red]Playlist not found:[/bold red] {name}")
        return
    current_playlist_name = name
    current_playlist = playlists[name]
    console.print(f"[bold green]Switched to playlist:[/bold green] {name}")

def toggle_shuffle():
    global is_shuffle
    is_shuffle = not is_shuffle
    console.print(f"[bold green]Shuffle mode {'enabled' if is_shuffle else 'disabled'}[/bold green]")
    if is_shuffle:
        random.shuffle(current_playlist)

def pause_music():
    global is_paused
    if player:
        player.pause()
        is_paused = not is_paused
        console.print("[bold yellow]Toggled pause[/bold yellow]")

def set_volume(level):
    global current_volume
    try:
        level = int(level)
        if 0 <= level <= 100:
            current_volume = level
            if player:
                player.audio_set_volume(level)
            console.print(f"[bold green]Volume set to {level}[/bold green]")
        else:
            console.print("[bold red]Volume must be between 0 and 100[/bold red]")
    except:
        console.print("[bold red]Invalid volume value[/bold red]")

def toggle_loop():
    global is_looping
    is_looping = not is_looping
    console.print(f"[bold green]Loop mode {'enabled' if is_looping else 'disabled'}[/bold green]")

def play_next():
    global current_index
    if is_looping and not current_playlist:
        return
    current_index = (current_index + 1) % len(current_playlist)
    play_music(current_playlist[current_index])

def play_previous():
    global current_index
    current_index = (current_index - 1 + len(current_playlist)) % len(current_playlist)
    play_music(current_playlist[current_index])

def toggle_mute():
    global is_muted, current_volume
    is_muted = not is_muted
    if player:
        player.audio_set_mute(is_muted)
    console.print(f"[bold green]{'Muted' if is_muted else 'Unmuted'}[/bold green]")

def command_prompt():
    while True:
        ui_header()
        command = Prompt.ask("[bold cyan]Enter command[/bold cyan]").strip().split()
        if not command:
            continue
        cmd = command[0]
        args = command[1:]

        if cmd == "play" and args:
            play_music(args[0])
        elif cmd == "list":
            list_playlist()
        elif cmd == "add" and args:
            add_to_playlist(args[0])
        elif cmd == "remove" and args:
            remove_from_playlist(args[0])
        elif cmd == "create" and args:
            create_playlist(args[0])
        elif cmd == "switch" and args:
            switch_playlist(args[0])
        elif cmd == "shuffle":
            toggle_shuffle()
        elif cmd == "pause":
            pause_music()
        elif cmd == "volume" and args:
            set_volume(args[0])
        elif cmd == "loop":
            toggle_loop()
        elif cmd == "next":
            play_next()
        elif cmd == "prev":
            play_previous()
        elif cmd == "mute":
            toggle_mute()
        elif cmd == "quit":
            console.print("[bold green]Goodbye![/bold green]")
            stop_music()
            break
        else:
            console.print("[bold red]Unknown command[/bold red]")

if __name__ == "__main__":
    command_prompt()