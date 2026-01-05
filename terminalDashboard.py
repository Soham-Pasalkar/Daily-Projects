import psutil
from rich.console import Console
from time import sleep

console = Console()

while True:
    console.clear()
    
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    console.print(f"[bold green]CPU Usage:[/bold green] {cpu_usage}%")
    
    # Memory Usage
    memory = psutil.virtual_memory()
    console.print(f"[bold blue]Memory Usage:[/bold blue] {memory.percent}% ({memory.used // (1024 ** 2)}MB used of {memory.total // (1024 ** 2)}MB)")
    
    # Disk Usage
    disk = psutil.disk_usage('/')
    console.print(f"[bold yellow]Disk Usage:[/bold yellow] {disk.percent}% ({disk.used // (1024 ** 3)}GB used of {disk.total // (1024 ** 3)}GB)")
    
    # Network Stats
    net_io = psutil.net_io_counters()
    console.print(f"[bold magenta]Network I/O:[/bold magenta] Sent: {net_io.bytes_sent // (1024 ** 2)}MB, Received: {net_io.bytes_recv // (1024 ** 2)}MB")
    
    sleep(5)