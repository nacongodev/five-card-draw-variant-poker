#!/bin/bash

# Build client-side code
cd frontend
echo -e "\nNavigating to client directory"
sleep 2
if [ $? -ne 0 ]; then
  echo -e "\nError: could not navigate to client directory" 
  exit 1
fi

# Install dependencies
npm install
echo -e "\nInstalling client-side dependencies"
sleep 2
if [ $? -ne 0 ]; then
  echo -e "\nError: installing client-side dependencies failed" 
  exit 1
fi

npm run serve
echo -e "\Lauching the client"
if [ $? -ne 0 ]; then
  echo "Error: building client-side code failed" 
  exit 1
fi
