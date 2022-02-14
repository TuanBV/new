<template>
  <div id="nav">
    <router-link to="/">Home</router-link> 
    <router-link to="/transcript">Transcript</router-link> 
    <router-link to="/admin" v-if="position == 1">Admin</router-link> 
    <router-link to="/time-rate" v-if="position == 1">Time Rate</router-link> 
    <router-link to="/manager" v-if="position == 2">Manager</router-link> 
    <router-link to="/change-password">Change Password</router-link> 
    <router @click="logout()">Logout</router>
  </div>
</template>
<script>
import { useRouter } from 'vue-router'
// import { mapGetters } from 'vuex'
export default {
  setup() {
    const router = useRouter();
    const position = JSON.parse(localStorage.getItem('user'))[0].idposition;
    async function logout(){
      localStorage.clear();
      document.cookie ="token" + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
      router.push('/login');
    }
    return {
      position,
      logout
    }
  },
  // computed:{
  //   ...mapGetters(['user'])
  // }
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 20px;
  background-color: #7cd8ae ;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  padding: 15px;
}
#nav a.router-link-exact-active {
  color: #168352;
  /* background-color: #00ff8c; */
  /* border-radius: 5px; */
}
router{
  font-weight: bold;
}
router:hover{
  cursor: pointer;
}
</style>
