<template>
  <div class="app">
    <div class="word-recommendation">
      <h1 class="title">Word Recommendation</h1>
      <input
        class="input"
        type="text"
        placeholder="Enter a word"
        v-model="searchInput"
      />
      <button class="button" @click="search">Search</button>
      <ul class="recommendations" v-if="recommendations.length">
        <li v-for="word in recommendations" :key="word" class="recommendation">
          {{ word }}
        </li>
      </ul>
      <p class="no-results" v-else>No recommendations found.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchInput: '',
      recommendations: [],
    };
  },
  methods: {
    search() {
      axios
        .get('https://api.datamuse.com/words', {
          params: {
            ml: this.searchInput,
            max: 5,
          },
        })
        .then((response) => {
          this.recommendations = response.data.map((wordObj) => wordObj.word);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
body {
  background-color: blue;
}

.app {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.word-recommendation {
  max-width: 400px;
  padding: 20px;
  text-align: center;
  background-color: #f8f8f8;
  border-radius: 5px;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

.input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.recommendations {
  list-style-type: none;
  padding: 0;
  margin: 20px 0;
}

.recommendation {
  font-size: 18px;
  margin-bottom: 5px;
}

.no-results {
  font-style: italic;
  color: #777;
}
</style>

