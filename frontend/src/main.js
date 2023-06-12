import { createApp } from 'vue';
import WordRecommendation from './views/WordRecommendation.vue';

import axios from 'axios';
import 'vuetify/dist/vuetify.css';
import { createVuetify } from 'vuetify';
import router from './router';

const app = createApp(WordRecommendation);

app.config.productionTip = false;
app.config.globalProperties.$axios = axios;

app.use(createVuetify());
app.use(router);

app.mount('#app');

