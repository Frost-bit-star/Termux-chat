# install.sh
#!/bin/bash

# Update package list and install required packages
echo "Updating package list..."
apt update

echo "Installing required packages..."
apt install python3 python3-pip -y

# Install any Python dependencies (if applicable)
pip3 install -r requirements.txt

# Create an alias for xchat to run advanced3.py
echo "alias xchat='python3 /data/data/com.termux/files/home/Termux-chat/advanced3.py'" >> ~/.bashrc

# Source the .bashrc to apply changes
source ~/.bashrc
chmod +x install.sh
echo "Installation complete! You can now run 'xchat' in your Termux terminal."
