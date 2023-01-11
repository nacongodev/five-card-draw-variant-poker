#!/bin/bash


# Build server-side code
cd backend
echo -e "\nNavigating to server directory"
sleep 2
if [ $? -ne 0 ]; then
  echo -e "\nError: could not navigate to server directory" 
  exit 1
fi

# Create and activate the virtual environment
python -m venv venv
echo -e "\nCreating virtual environment"
sleep 2
if [ $? -ne 0 ]; then
  echo -e "\nError: creating virtual environment failed" 
  exit 1
fi
source venv/scripts/activate
echo -e "\nActivating virtual environment"
sleep 2
if [ $? -ne 0 ]; then
  echo -e "\nError: activating virtual environment failed" 
  exit 1
fi

# Run the command to install the requirements
pip3 install -r requirements.txt
echo -e "\nInstalling server-side dependencies"
sleep 2
if [ $? -ne 0 ]; then
  echo -e "\nError: installing server-side dependencies failed" 
  exit 1
fi

# go to the test folder and run the tests
cd backend/tests/
echo -e "\nRunning tests, please wait..."
sleep 2
python -m unittest discover -p "test_*.py" -v

# Start the server
echo -e "\nStarting the server"
sleep 2
uvicorn main:app --host 127.0.0.1 --port 8000
if [ $? -ne 0 ]; then
  echo "Error: installing server-side dependencies failed"
  exit 1
fi

