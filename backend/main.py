##if __name__ == '__main__':
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deck import Deck

# Initialize the Deck

deck = Deck()
app = FastAPI()


class Card(BaseModel):
    suit: str
    rank: int


class Hand(BaseModel):
    cards: List[Card]
    rank: str


# CORS to allow to map the frontend to the Backend

origins = [

    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/draw/{n}")
def draw_cards(n: int = 1):
    """
       Draw a card or cards from the top of the deck.

       Parameters:
       - n: The number of cards to draw (default is 1).
       """
    try:
        if deck is None:
            raise HTTPException(status_code=400, detail="Deck Not found")
        if n < 1:
            raise HTTPException(status_code=400, detail="Number of Cards to draw must be greater than 0")
        if deck.size() < n:
            raise HTTPException(status_code=404, detail=f"Not enough cards in the deck (only {deck.size()} remaining)")
        hand = deck.draw(n)
        if deck.size() == 0:
            raise HTTPException(status_code=404, detail="Deck is empty")
        deck.shuffle()
        return {"Shuffling status": "Shuffling done ", "Your Hand": hand.cards, "Your Rank": hand.rank}
    except ValueError as e:
        return {"error": str(e)}


@app.get("/")
def shuffle_deck():
    """
    Shuffle the deck of cards.
    """
    # Check if the deck is empty
    if deck.size() == 0:
        raise HTTPException(status_code=404, detail="Deck is empty")
    deck.shuffle()
    return {"message": "Shuffling... Shuffling... Shuffling..."}


@app.get("/size")
def get_deck_size():
    """
    Get the number of cards remaining in the deck.
    """
    # Check if the deck has been initialized
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck has not been initialized")
    return {"Remaining cards in the deck": deck.size()}


