import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Price from '../components/Price.vue';
import Index from '../components/Index.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/',
    name: 'Index',
    component: Index,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/price',
    name: 'Price',
    component: Price,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

console.log(router.getRoutes());

export default router;
