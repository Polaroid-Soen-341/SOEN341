import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/feed',
    name: 'MainLayout',
    component: () => import('../views/MainLayout.vue'),
    children: [
      
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
