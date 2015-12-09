"""
This module contains generic functions for handling communication with
Informatica programs and process their output.
"""
import subprocess

def cmd_execute(command):
    """
    Execute a command and return the output as an array of lines.
    """
    command_output = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).communicate()
    return command_output[0].split('\n')

def cmd_prepare(params, opts_r, opts_q, opts_b):
    """
    Prepare the command parameters

    Args:
       params (str): parameters supplied
       opts_r ([str]): list of command line switches of which arguments need not be quoted
       opts_q ([str]): list of command line switches of which arguments must be quoted
       opts_b ([str]): list of command line switches without arguments (boolean)
    """
    command = []
    for key, value in params.iteritems():
        if key in opts_r:
            command.extend(['-' + key, value])
        elif key in opts_q:
            command.extend(['-' + key, '"' + value + '"'])
        elif key in opts_b:
            command.extend(['-' + key])
        elif key not in opts_r + opts_q + opts_b:
             raise Exception("unsupported option: %s" % key)
    return command

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
