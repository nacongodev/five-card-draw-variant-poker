<template>
  <div>
    <label>Number of cards:</label>
    <input type="number" v-model.number="numCards">
    <button @click="drawCards">Draw Cards</button>
    <div v-if="hand.length">
      <p>Your Hand:</p>
      <ul>
        <li v-for="(card, index) in hand" :key="index " :style="{display: 'inline-block'}">{{ card.rank }}{{ card.suit }}</li>
      </ul>
      <p>Your rank: {{ rank}}</p>
    </div>
    <div v-else>
      <p>No cards in hand</p>
    </div>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      hand: [],
      rank: '',
      error: '',
      numCards: 1
    }
  },
  methods: {
    async drawCards() {
      try {
        const response = await axios.get(`http://localhost:8000/draw/${this.numCards}`)
        this.hand = response.data.Hand
        console.log(this.hand)
        this.rank = response.data.Rank
        console.log(this.rank)
      } catch (error) {
        this.error = error.response.data.error
        if (error.response.status === 404) {
      this.error = "Not enough cards in the deck";
    } else {
      this.error = "An error occurred";
    }
      }
    }
  }
}
</script>
