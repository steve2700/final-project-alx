<template>
  <div class="search">
    <div class="search-container">
          <h1 class="search-header">Word Recommendation</h1>

      <input
        class="search-input"
        type="text"
        placeholder="Enter a search query"
        v-model="searchInput"
        @input="fetchWordRecommendations"
      />
      <ul class="recommendations" v-if="recommendations.length">
        <li v-for="word in recommendations" :key="word" class="recommendation">
          <a @click="performSearch(word)">{{ word }}</a>
        </li>
      </ul>
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
    fetchWordRecommendations() {
      if (this.searchInput.length > 0) {
        axios
          .get('https://api.datamuse.com/words', {
            params: {
              ml: this.searchInput,
              max: 10,
            },
          })
          .then((response) => {
            this.recommendations = response.data.map((wordObj) => wordObj.word);
          })
          .catch((error) => {
            console.error(error);
          });
      } else {
        this.recommendations = [];
      }
    },
    performSearch(query) {
      // Implement your search functionality here
      console.log('Performing search for:', query);
      // Redirect to search results page or fetch search results
    },
  },
};
</script>

<style>
body {
  background-color: black;
}

.search {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.search-input {
  width: 300px;
  padding: 10px;
  font-size: 18px;
  color: white; /* Set the text color to white */
  background-color: rgba(255, 255, 255, 0.1); /* Set a semi-transparent background */
  border: 1px solid #ccc;
  border-radius: 5px;
}

.recommendations {
  list-style-type: none;
  padding: 0;
  margin: 10px 0;
}

.recommendation {
  margin-bottom: 5px;
}

.recommendation a {
  color: #007bff;
  cursor: pointer;
  text-decoration: none;
}
.search-header {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #007bff; /* Change the color to your desired value */
  }

</style>

