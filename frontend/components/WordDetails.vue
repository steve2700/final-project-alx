<template>
  <div class="word-details">
    <h1 class="word-details-header">{{ selectedWord }}</h1>
    <div v-if="wordDetails">
      <p class="word-definition"><strong>Definition:</strong> {{ wordDetails.definition }}</p>
      <p class="word-synonyms"><strong>Synonyms:</strong> {{ wordDetails.synonyms.join(', ') }}</p>
      <p class="word-antonyms"><strong>Antonyms:</strong> {{ wordDetails.antonyms.join(', ') }}</p>
      <!-- Add more word information here as needed -->
    </div>
    <div v-else>
      <p class="loading-message">Loading word details...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    selectedWord: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      wordDetails: null
    };
  },
  mounted() {
    this.fetchWordDetails();
  },
  methods: {
    fetchWordDetails() {
      const apiKey = 'f176880a-1df1-48a7-9519-c4b6a4622f25';
      const apiUrl = `https://dictionaryapi.com/api/v3/references/learners/json/${this.selectedWord}?key=${apiKey}`;

      axios
        .get(apiUrl)
        .then((response) => {
          // Process the API response to extract the required word details
          const wordData = response.data[0];
          this.wordDetails = {
            definition: wordData.shortdef[0],
            synonyms: wordData.meta.syns[0] || [],
            antonyms: wordData.meta.ants[0] || []
          };
        })
        .catch((error) => {
          console.error(error);
        });
    }
  }
};
</script>

<style>
.word-details {
  margin-top: 20px;
}

.word-details-header {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.word-definition {
  margin-top: 10px;
}

.word-synonyms,
.word-antonyms {
  margin-top: 5px;
  font-style: italic;
}

.loading-message {
  margin-top: 10px;
  color: #999;
}
</style>

