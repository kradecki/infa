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

def cmd_prepare(params, opts_args, opts_flags):
    """
    Prepare the command parameters

    Args:
       params (str): parameters supplied
       opts_args ([str]): list of command line options with arguments
       opts_flags ([str]): list of command line options without arguments
    """
    command = []
    for key, value in params.iteritems():
        if key in opts_args:
            command.extend(['-' + key, value])
        elif key in opts_flags:
            command.extend(['-' + key])
        elif key not in opts_args + opts_flags:
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
