import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import MainLayout from '../views/MainLayout.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/feed',
    name: 'MainLayout',
    component: MainLayout
  }
]

const router = new VueRouter({
  routes
})

export default router
