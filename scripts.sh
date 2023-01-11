#!/bin/bash

echo "Welcome to the Five Card Draw Poker Game"
echo "Please select the option to build:"
echo "1. Build the client"
echo "2. Build the server"

read -p "Enter your choice: " choice

if [ $choice -eq 1 ]; then
  sh client_build.sh
elif [ $choice -eq 2 ]; then
  sh server_build.sh
else
  echo "Invalid choice. Exiting."
fi


