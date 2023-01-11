#!/bin/bash

set -e

function run_client() {
    cd frontend
    #install the client side dependencies
    npm install
    #run the client side app
    npm run serve
    cd ..
}

function run_server() {
    cd backend
    #install the server side dependencies
    pip install -r requirements.txt
    #run the server side app
    uvicorn main:app --reload
    cd ..
}

function run_tests() {
    cd backend
    #run the unit tests
    pytest
    cd ..
}

if [ $1 == "client" ]; then
    run_client
elif [ $1 == "server" ]; then
    run_server
elif [ $1 == "test" ]; then
    run_tests
else
    echo "Invalid option. Please choose 'client', 'server' or 'test'."

