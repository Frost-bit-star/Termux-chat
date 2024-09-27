#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import os
import sys
import time
import webbrowser

# style and colors
i = '\033[3m'
u = '\033[4m'
w = '\033[0m'
r = '\033[1;91m'
g = '\033[1;92m'
y = '\033[1;33m'
b = '\033[1;94m'
c = '\033[1;96m'  # Cyan for menu text
d = '\033[90m'

# Function to display banner
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(w+d+"      ,,                ,,")
    print(w+d+"    (((((              )))))")
    print(w+d+"   ((((((              ))))))")
    print(w+d+"   ((((((              ))))))")
    print(w+d+"    ((((("+w+b+",r@@@@@@@@@@e,"+w+d+")))))")
    print(w+d+"     ((("+w+b+"@@@@@@@@@@@@@@@@"+w+d+")))")
    print(w+b+"      \@@/"+r+",:::,"+w+b+"\/"+r+",:::,"+w+b+"\@@/")
    print(w+b+"     /@@@|"+r+":::::"+w+b+"||"+r+":::::"+w+b+"|@@@\\")
    print(w+b+"    / @@@\\"+r+"':::'"+w+b+"/\\"+r+"':::'"+w+b+"/@@@ \\    "+w+"'"+r+"stay anonymous"+b+w+"'")
    print(w+b+"   /  /@@@@@@@//\\\@@@@@@@\  \\        "+d+"version 3.0"+w)
    print(w+b+"  (  /  '@@@@@====@@@@@'  \  )")
    print(w+b+"   \(     /          \     )/")
    print(w+b+"     \   (            )   /")
    print(w+b+"          \          /"+w)

# print letter by letter
def prints(text):
    for line in text:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.05)  # Adjusted delay for better visibility
        print('')

# Function to receive messages from the server
def receive_messages(sock, community=None):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                if community is None or community in message:
                    print(f"\033[92m{message}\033[0m")  # Print messages in green
            else:
                break
        except:
            break

# Function to start the client
def start_client(server_ip, username, community=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 9999))
    
    threading.Thread(target=receive_messages, args=(client_socket, community)).start()
    
    while True:
        message = input()
        if message.lower() == 'exit':
            webbrowser.open("https://www.youtube.com/@Mr_termux-r2l")  # Redirect to YouTube channel
            break
        full_message = f"{username}: {message}" if community is None else f"{username} [{community}]: {message}"
        client_socket.send(full_message.encode('utf-8'))
    
    client_socket.close()

# Function to display the menu and handle user choices
def display_menu():
    print(f"{c}Menu:{w}")  # Set menu color to cyan
    print("1. Chat with all users worldwide")
    print("2. Create a community")
    print("3. Join an available community")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

# Function to create a community
def create_community(communities):
    community_name = input("Enter the name of the community to be created: ")
    communities.append(community_name)
    print(f"Community '{community_name}' created successfully!")
    time.sleep(2)  # Pause for 2 seconds before returning to the menu

# Function to join a community
def join_community(communities, username):
    print("Available communities:")
    for index, community in enumerate(communities):
        print(f"{index + 1}. {community}")
    
    choice = int(input("Choose a community to join (number): ")) - 1
    if 0 <= choice < len(communities):
        print(f"You have joined the community: {communities[choice]}")
        start_client(server_ip, username, communities[choice])  # Start chatting in the community
    else:
        print("Invalid choice. Returning to menu.")
        time.sleep(2)

# Main function to run the application
if __name__ == "__main__":
    banner()  # Display the banner
    prints(["\033[1;92mWelcome to XChat!\033[0m"])  # Print welcome message in green
    username = input("Enter your username: ")
    server_ip = "138.68.79.95"  # Predefined server IP
    communities = []  # List to hold community names

    while True:
        user_choice = display_menu()
        
        if user_choice == '1':
            start_client(server_ip, username)  # Chat with all users
        elif user_choice == '2':
            create_community(communities)  # Create a community
        elif user_choice == '3':
            join_community(communities, username)  # Join an available community
        elif user_choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
