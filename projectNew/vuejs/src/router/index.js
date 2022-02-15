import { createRouter, createWebHistory } from 'vue-router'
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
    component: () => import('../views/forgot-password.vue')
  },  
  {
    path: '/',
    name: 'Home',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/home.vue')
  },
  {
    path: '/transcript',
    name: 'Transcript',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/transcript.vue')
  },
  {
    path: '/transcript-employee',
    name: 'TranscriptEmployee',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/transcript-employee.vue')
  },
  // user
  {
    path: '/admin',
    name: 'Admin',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/admin.vue')
  },  
  {
    path: '/admin/add-user',
    name: 'AddUser',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/add-user.vue')
  },  
  {
    path: '/admin/edit-user',
    name: 'EditUser',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/edit-user.vue')
  },
  // time rate
  {
    path: '/time-rate',
    name: 'TimeRate',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/admin/timerate.vue')
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
    component: () => import('../views/manager/manager.vue')
  },
  {
    path: '/confirm-transcript-employee',
    name: 'ConfirmTranscriptEmployee',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/manager/confirm-transcrip-employee.vue')
  },  
  {
    path: '/change-password',
    name: 'ChangePassword',
    meta:{
      layout: 'auth'
    },
    component: () => import('../views/changepassword.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
