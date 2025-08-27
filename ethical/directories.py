import requests
from termcolor import colored

target_url= input('[+] Enter taget URL :')
file_name= input('[+] Enter name of the file containing directories :')

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
    
file = open(file_name , 'r')
for line in file:
    directory= line.strip()
    full_url= target_url + '/' + directory
    response= request(full_url)
    if response:
        print(colored(('[*] Discovered directory at this path '+ full_url), 'green'))
        exit()
    else:
        print(colored(('[*] Directory not found '), 'red'))