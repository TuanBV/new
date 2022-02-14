import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Transcript from '../views/transcript.vue'
import TranscriptEmployee from '../views/TranscriptEmployee.vue'
import Admin from '../views/admin/admin.vue'
import TimeRate from '../views/admin/timerate.vue'
import Manager from '../views/manager/manager.vue'
import ChangePassword from '../views/ChangePassword.vue'

import AddUser from '../views/admin/add-user.vue'
import EditUser from '../views/admin/edit-user.vue'
import ForgotPassword from '../components/forgot-password.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    meta:{
      layout: 'default'
    },
    component: ()=> import('../views/login.vue')
  },  
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    meta:{
      layout: 'default'
    },
    component: ForgotPassword
  },  
  {
    path: '/',
    name: 'Home',
    meta:{
      layout: 'auth'
    },
    component: Home
  },
  {
    path: '/transcript',
    name: 'Transcript',
    meta:{
      layout: 'auth'
    },
    component: Transcript
  },
  {
    path: '/transcript-employee',
    name: 'TranscriptEmployee',
    meta:{
      layout: 'auth'
    },
    component: TranscriptEmployee
  },
  // user
  {
    path: '/admin',
    name: 'Admin',
    meta:{
      layout: 'auth'
    },
    component: Admin
  },  
  {
    path: '/admin/add-user',
    name: 'AddUser',
    meta:{
      layout: 'auth'
    },
    component: AddUser
  },  
  {
    path: '/admin/edit-user',
    name: 'EditUser',
    meta:{
      layout: 'auth'
    },
    component: EditUser
  },
  // time rate
  {
    path: '/time-rate',
    name: 'TimeRate',
    meta:{
      layout: 'auth'
    },
    component: TimeRate
  },  
  {
    path: '/admin/add-time-rate',
    name: 'AddTimerate',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/add-timerate.vue')
  },  
  {
    path: '/admin/edit-time-rate',
    name: 'EditTimerate',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/edit-timerate.vue')
  },
  {
    path: '/admin/time-rate/detail',
    name: 'DetailTimerate',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/detail-timerate.vue')
  },
  // manager
  {
    path: '/manager',
    name: 'Manager',
    meta:{
      layout: 'auth'
    },
    component: Manager
  },  
  {
    path: '/change-password',
    name: 'ChangePassword',
    meta:{
      layout: 'auth'
    },
    component: ChangePassword
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
