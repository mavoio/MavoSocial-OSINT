import requests
import time
from bs4 import BeautifulSoup
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.prompt import Prompt
from rich.style import Style
from pyfiglet import Figlet
import random

# Initialize Rich console
console = Console()

# Custom User-Agent to avoid some blocks
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Dictionary of platforms and their URL formats with icons
PLATFORMS = {
    'Instagram': {'url': lambda u: f'https://www.instagram.com/{u}/', 'icon': '📸'},
    'YouTube': {'url': lambda u: f'https://www.youtube.com/@{u}', 'icon': '🎥'},
    'Reddit': {'url': lambda u: f'https://www.reddit.com/user/{u}', 'icon': '🤖'},
    'Roblox': {'url': lambda u: f'https://www.roblox.com/user.aspx?username={u}', 'icon': '🎮'},
    'Twitter': {'url': lambda u: f'https://twitter.com/{u}', 'icon': '🐦'},
    'Steam': {'url': lambda u: f'https://steamcommunity.com/id/{u}', 'icon': '🎲'},
    'GitHub': {'url': lambda u: f'https://github.com/{u}', 'icon': '💻'},
    'TikTok': {'url': lambda u: f'https://www.tiktok.com/@{u}', 'icon': '🎵'},
    'Twitch': {'url': lambda u: f'https://www.twitch.tv/{u}', 'icon': '🎬'},
    'Pinterest': {'url': lambda u: f'https://www.pinterest.com/{u}', 'icon': '📌'},
    'DeviantArt': {'url': lambda u: f'https://www.deviantart.com/{u}', 'icon': '🎨'},
    'Spotify': {'url': lambda u: f'https://open.spotify.com/user/{u}', 'icon': '🎵'},
    'Medium': {'url': lambda u: f'https://medium.com/@{u}', 'icon': '📝'},
    'Telegram': {'url': lambda u: f'https://t.me/{u}', 'icon': '📱'},
    'VKontakte': {'url': lambda u: f'https://vk.com/{u}', 'icon': '🌐'}
}

def display_title():
    # Create figlet banner with a cool font
    f = Figlet(font='banner3-D')
    title = f.renderText('MAVO OSINT')
    
    # Create styled panel with gradient effect
    content = Text()
    
    # Add the title with styling
    for line in title.split('\n'):
        content.append(str(line) + '\n', style="bold magenta")
    
    # Add author info
    content.append('\n', style="bold cyan")  # Add spacing
    content.append('🔥 Created by github.com/mavoio 🔥', style="bold cyan")
    
    # Create the panel
    title_panel = Panel(
        Align.center(content),
        border_style="magenta",
        padding=(1, 2),
        style="on black"
    )
    console.print(title_panel)
    
    # Print subtitle with emojis
    console.print(
        Align.center(Text("🔍 Advanced Social Media Intelligence Tool 🔍", style="bold yellow")),
        "\n"
    )

def create_results_table():
    table = Table(show_header=True, header_style="bold magenta", border_style="cyan")
    table.add_column("Platform", style="cyan", no_wrap=True)
    table.add_column("Status", style="bold")
    table.add_column("URL", style="blue")
    return table

def check_site(username, url, platform_name, platform_info, progress, task_id):
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        progress.advance(task_id)
        
        if response.status_code == 200:
            return {
                'platform': f"{platform_info['icon']} {platform_name}",
                'status': "[green]FOUND[/green]",
                'url': url
            }
        else:
            return {
                'platform': f"{platform_info['icon']} {platform_name}",
                'status': "[red]NOT FOUND[/red]",
                'url': "N/A"
            }
    except Exception as e:
        progress.advance(task_id)
        return {
            'platform': f"{platform_info['icon']} {platform_name}",
            'status': "[yellow]ERROR[/yellow]",
            'url': "N/A"
        }

def search_username(username):
    results = []
    found_count = 0
    total_platforms = len(PLATFORMS)
    
    # Create progress bar
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(complete_style="green", finished_style="green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        # Add overall progress task
        search_task = progress.add_task(
            f"[cyan]Searching for '{username}'...",
            total=total_platforms
        )
        
        # Search each platform
        for platform_name, info in PLATFORMS.items():
            url = info['url'](username)
            result = check_site(username, url, platform_name, info, progress, search_task)
            results.append(result)
            if result['status'] == "[green]FOUND[/green]":
                found_count += 1
            time.sleep(0.5)  # Small delay to avoid rate limiting
    
    # Create and populate results table
    table = create_results_table()
    for result in results:
        table.add_row(result['platform'], result['status'], result['url'])
    
    # Display results
    console.print("\n")
    console.print(Panel(table, title="[bold cyan]Search Results[/bold cyan]", border_style="cyan"))
    
    # Display summary in a more compact way
    summary = Panel(
        f"[cyan]Found [green]{found_count}[/green] profiles out of [yellow]{total_platforms}[/yellow] platforms checked.[/cyan]\n[dim cyan]💡 Star us on GitHub: [link=https://github.com/mavoio]github.com/mavoio[/link][/dim cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(summary)

def main():
    console.clear()
    display_title()
    
    while True:
        username = Prompt.ask("\n[yellow]Enter username to search[/yellow] ([red]'quit'[/red] to exit)")
        
        if username.lower() == 'quit':
            console.print("\n[yellow]Thanks for using MAVO OSINT! Goodbye![/yellow] 👋")
            console.print("[dim]Don't forget to star us on GitHub: https://github.com/mavoio[/dim]\n")
            break
        
        if not username:
            console.print("[red]Please enter a valid username![/red]")
            continue
        
        console.clear()
        display_title()
        search_username(username)
        
        console.print("\n[yellow]Press Enter to search another username or type 'quit' to exit[/yellow]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Program terminated by user.[/yellow] 👋\n")
    except Exception as e:
        console.print(f"\n[red]An unexpected error occurred: {str(e)}[/red]") 