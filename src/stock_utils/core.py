"""Core orchestration logic for launching project scripts."""

import subprocess
from pathlib import Path
from stock_utils.utils.console import console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.align import Align
from playsound3 import playsound


def _discover_scripts():
    """Discover runnable Python scripts under the project modules.

    Returns:
        A dictionary keyed by module name containing sorted script names such as
        ``"algo.binary_search"``.
    """
    src_dir = Path(__file__).resolve().parent
    modules = ("algo", "math", "utils")
    discovered = {}

    for module in modules:
        module_dir = src_dir / module
        scripts = []

        if module_dir.is_dir():
            for file_path in sorted(module_dir.glob("*.py")):
                if file_path.name == "__init__.py":
                    continue
                scripts.append(f"{module}.{file_path.stem}")

        discovered[module] = scripts

    return discovered


def _chooser(options) -> int:
    """Display a selection table and return the user's choice index.

    Args:
        options: Sequence of labels to show in the chooser.

    Returns:
        The selected option number, with ``0`` reserved for the exit choice.
    """
    table = Table(title="Options")
    table.add_column('#', justify='center', style='cyan', no_wrap=True)
    table.add_column('Title', justify='center', style='cyan')
    choices = ['0']
    for i, j in enumerate(options):
        choice_string = str(i + 1)
        table.add_row(choice_string, j)
        choices.append(choice_string)
    centered_table = Align.center(table, vertical='middle')
    console.print(centered_table)
    choice_message = Align.center('Enter your choice:', vertical='middle')
    console.print(choice_message)
    choice = IntPrompt.ask('', choices=choices, default=0)
    return choice


class Orchestrator:
    """Menu-driven orchestrator for launching project scripts."""

    def __init__(self, name):
        """Initialize the orchestrator with a display name.

        Args:
            name: Human-readable name for the orchestrator instance.
        """
        self.name = name
        self.scripts = _discover_scripts()

    def menu_loop(self, silent=False):
        """Run the primary interactive menu until the user exits.

        Args:
            silent: If ``True``, suppress the startup audio.

        Returns:
            The exit status code chosen by the user.
        """
        sound = None
        if not silent:
            src_dir = Path(__file__).resolve().parent.parent
            audio = src_dir / 'stock_utils/static/test_audio.mp3'
            sound = playsound(audio, block=False)
        status = 1
        while status == 1:
            mod_options = ('algo', 'math', 'utils')
            mod_choice = _chooser(mod_options)
            mod_choice -= 1
            if mod_choice == -1 or mod_choice > len(mod_options) - 1:
                status = mod_choice
            else:
                script_options = self.scripts[mod_options[mod_choice]]
                script_choice = _chooser(script_options)
                script_choice -= 1
                if script_choice == -1 or script_choice > len(script_options):
                    status = script_choice
                else:
                    s = self.scripts[mod_options[mod_choice]][script_choice]
                    module, stem = s.split(".")
                    script_path = Path(__file__).resolve().parent / module / f"{stem}.py"
                    subprocess.run(["python", str(script_path)])

        if sound:
            sound.stop()
        return status
