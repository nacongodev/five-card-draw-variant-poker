<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <CardDeck></CardDeck>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import CardDeck from './components/CardComponent.vue'
//import Drawcards from './components/Drawcards.vue'
//import ShuffleDeck from './components/ShuffleDeck.vue'

export default {
  name: 'App',
  components: {
    CardDeck
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
