"""
This module contains generic functions for handling communication with
Informatica programs and process their output.
"""
import subprocess

def execute_cmd(command):
    """
    Execute a command and return the output as an array of lines.
    """
    command_output = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    return command_output[0].split('\n')

def format_output(output, field_separator):
    """
    Cleanse output and format it to an API-friendly list
    """
    ignore_lines=(
        'Informatica',
        'Copyright',
        'All Rights Reserved',
        'This Software is protected',
        'Invoked at',
        'Completed at',
        '.listobjects completed',
        'listconnections completed'
    )
    return [
        item.strip().split(field_separator) for item in output
        if item and not item.startswith(ignore_lines)
    ]
