import time
from datetime import datetime


def current_timezone():
    """
    Get the system's current timezone.

    Returns:
    - str: The current timezone (e.g., 'UTC', 'EST', 'PST').
    """
    return time.tzname[0]

def current_date():
    """
    Get the current date.

    Returns:
    - str: The current date in 'YY-MM-DD' format.
    """
    return datetime.now().strftime('%Y-%m-%d')

def current_time():
    """
    Get the current time.

    Returns:
    - str: The current time in 'HH:MM:SS' format.
    """
    return datetime.now().strftime('%H:%M:%S')

def days_until(date_str):
    """
    Calculate the number of days from today until a specified date.

    Parameters:
    - date_str (str): The target date in 'YYYY-MM-DD' format.

    Returns:
    - int: The number of days between today and the target date.
    """
    target_date = datetime.strptime(date_str, '%Y-%m-%d')
    today = datetime.now()
    return (target_date - today).days