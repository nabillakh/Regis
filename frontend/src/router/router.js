// src/router/index.js (ou router.js si tu le places dans le dossier src directement)
import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from '../components/HomePage.vue';  // Exemple de composant à router

Vue.use(VueRouter);

const routes = [
  { path: '/', component: HomePage },
  // Ajoute ici d'autres routes si besoin
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router;
