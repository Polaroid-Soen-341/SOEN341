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
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/feed',
    name: 'MainLayout',
    component: () => import('../views/MainLayout.vue'),
    children: [
      {path: '/feed', name: 'Feed', component: () => import('../views/Feed.vue')},
      {path: '/myprofile', name: 'MyProfile', component: () => import('../views/MyProfile.vue')},
      {path: '/userprofile', name: 'UserProfile', component: () => import('../views/UserProfile.vue')},
      {path: '/connections', name: 'Connections', component: () => import('../views/Connections.vue')},
      {path: '/notifications', name: 'Notifications', component: () => import('../views/Notifications.vue')},
      {path: '/settings', name: 'Settings', component: () => import('../views/Settings.vue')},
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
