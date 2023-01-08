<template>
  <div>
    <label>Number of cards:</label>
    <input type="number" v-model.number="numCards">
    <button @click="drawCards">Draw Cards</button>
    <p v-if="error">{{ error }}</p>
    <p v-else>Your Hand: {{ hand.join(', ') }}</p>
    <p>Your Rank: {{ rank }}</p>
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
        this.hand = response.data.hand
        this.rank = response.data.rank
      } catch (error) {
        this.error = error.response.data.error
      }
    }
  }
}
</script>
