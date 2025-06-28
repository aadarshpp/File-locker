# In-build library
import os.path

# Intalled library
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box

# User defined library
import clone
import locker

console = Console()

def main():
    console.print(Panel("🔐 [bold cyan]Python File Locker[/bold cyan]", box=box.ROUNDED))

    while True:

        command = Prompt.ask(
            "[bold yellow]\nChoose action[/bold yellow]",
            choices=["lock", "unlock", "clone", "exit"],
            default="lock"
        )

        if command == "exit":
            console.print("[bold red]Program closed[/bold red]")
            return

        filepath = Prompt.ask("[bold green]Enter the path to the file[/bold green]")

        notfound = not os.path.exists(filepath)
        notafile = not os.path.isfile(filepath)

        if notfound or notafile:
            valid = False
            message = f"'{filepath}' not found" if notfound else f"'{filepath}' not a file"
            console.print(f"[#FF8C00]ERROR: {message}[/#FF8C00]")

            if notfound and os.path.exists(f"{filepath}.locked"):
                question = f"[italic]Did you mean '{filepath}.locked'?[/italic]"
                answer = Prompt.ask(question, choices=["y", "n"], default="n")
                if answer == "y":
                    filepath = f"{filepath}.locked"
                    valid = True

            if not valid:
                console.print("[bright_red]Action aborted[/bright_red]")
                continue

        if command == "clone":
            console.print(f"[blue]Cloning file {filepath}...[/blue]")
            clone_file(filepath)
            console.print(f"[green]File cloned successfully[/green]")
            continue

        password = Prompt.ask("[bold magenta]Enter your password[/bold magenta]", password=True)

        if command == "lock":

            if filepath.endswith(".locked"):
                question = f"[bold cyan]{filepath} is already locked, do you want to lock it again?[/bold cyan]"
                answer = Prompt.ask(question, choices=["y", "n"], default="n")
                if answer == "n":
                    console.print("[bright_red]Action aborted[/bright_red]")
                    continue

            console.print("[yellow]Encrypting and locking file...[/yellow]")
            encrypt_file(filepath, password)
            console.print("[green]File encrypted and locked[/green]")

        elif command == "unlock":

            if not filepath.endswith(".locked"):
                console.print(f"[red]{filepath} is not a '.locked' file. Decryption rejected.[/red]")
                console.print("[bright_red]Action aborted[/bright_red]")
                continue

            console.print("[yellow]Decrypting and unlocking file...[/yellow]")
            decrypt_success = decrypt_file(filepath, password)
            if decrypt_success:
                console.print("[green]File decrypted and unlocked[/green]")
            else:
                console.print("[red]Decryption failed[/red]")


def encrypt_file(filepath: str, password: str):
    return locker.encrypt_file(filepath, password)

def decrypt_file(filepath: str, password: str) -> bool:
    return locker.decrypt_file(filepath, password)

def clone_file(source: str) -> str:
    return clone.clone_file(source)

if __name__ == "__main__":
    main()
