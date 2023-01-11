# five-card-draw-variant-poker
This is poker game with Backend API and frontend using VUE js


# How to run

- You can run the the front and backend by calling sh scripts.sh and choose an option client or server.

`sh scripts.sh`

+ run the scripts twice on different command window 
+ the sever side option will also run all the test


# ENPOINTS: 

- http://127.0.0.1:8000/draw/{n} n is the number of cards you can draw
```json
{
"Shuffling status": "Shuffling done ",
"Hand": [
{
"rank": 11,
"suit": "♦"
},
{
"rank": 5,
"suit": "♦"
}
],
"Handrank": "High Cards"
}
```
- http://127.0.0.1:8000/ : Entry point to start shuffling the deck
```json
  {
"message": "Shuffling... Shuffling... Shuffling..."
}

```
- http://127.0.0.1:8000/size : Get the size of the deck in other to know the remaining amount of cards in the Deck

```json
{
"Remaining cards in the deck": 52
}
```

# Work in progress:

  - Vue Js (Display of the cards and the rank of the Hand)

  - Note: CORS established between the Backend end Frontend
