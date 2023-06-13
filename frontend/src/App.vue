<template>
  <div id="app">
    <WordRecommendation />
    <WordDetails v-if="selectedWord" :word="selectedWord" />
  </div>
</template>

<script>
import WordRecommendation from '@/views/WordRecommendation.vue';
import WordDetails from '@/views/WordDetails.vue';

export default {
  name: 'App',
  components: {
    WordRecommendation,
    WordDetails,
  },
  data() {
    return {
      selectedWord: '',
    };
  },
  methods: {
    showWordDetails(word) {
      this.selectedWord = word;
    },
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
}
</style>

