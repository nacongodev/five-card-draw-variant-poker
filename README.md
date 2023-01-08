# five-card-draw-variant-poker
This is poker game with Backend API and frontend using VUE js

The Backed is written using FastApi and the Frontend Vue Js

How to run the Backend 

- pip install -r requirements.txt

ENPOINTS: 

- http://127.0.0.1:8000/draw/{n} n is the number of cards you can draw
- http://127.0.0.1:8000/shuffle : Check if the Deck is shuffled
- http://127.0.0.1:8000/size : Get the size of the deck in other to know the remaining amount of cards in the Deck

How to run the frontend

- use npm install to install all packages and use npm run serve to start the frontend

Work in progress:

Vue Js (Display of the cards and the rank of the Hand)

Note: CORS established between the Backend end Frontend
