import Vue from 'vue';
import App from './App.vue';
import router from './router';  // Import du router (si présent)
import store from './store';    // Import du store (si présent)

Vue.config.productionTip = false;

new Vue({
  router,      // Ajoute le router si tu l'utilises
  store,       // Ajoute le store si tu utilises Vuex
  render: h => h(App)
}).$mount('#app');