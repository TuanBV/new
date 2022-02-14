<template>
  <div class="sign-in">
    <div class="container">
      <div class="wrapper" id="login">
        <div class="title"><span>Login Account</span></div>
        <form method="post">
          <div class="row">
            <i class="fas fa-user"></i>
            <input type="text" placeholder="Username" v-model="username"/>
          </div>
          <p class="form-text" id="alert-user"></p>
          <div class="row">
            <i class="fas fa-lock"></i>
            <input type="password" placeholder="Password" v-model="password"/>
          </div>
          <div class="pass">
            <router-link to='/forgot-password'><a> Forgot password !!!</a></router-link>
          </div>
          <div class="row">
            <button type="button" v-if="isLoading">Loading ...</button>
            <button type="button" v-else @click="login()">Login</button>
          </div>
          <div v-if="error" class="text-center" style="color: red; background: #f8f9fa;line-height: 40px;border-radius: 5px;">
            <span>{{ error }}</span>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from "vue-router"

import { useSignIn } from "@/composables/useSignIn";

export default {
  setup(){
    const username = ref('');
    const password = ref('');
    const router = useRouter();
    const { error, isLoading, signin} = useSignIn();
    // method
    async function login(){
      await signin(username.value, password.value);
      if (!error.value) router.push({'name': "Home", params: {}});
    }
    return {
      username,
      password,
      error,
      isLoading,
      // method
      login
    } 
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&display=swap");
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
.container {
  max-width: 440px;
  padding: 0 10px;
  margin: 250px auto;
}
.wrapper {
  width: 100%;
  background: #fff;
  border-radius: 5px;
  border: 1px solid #19ab8d;
  box-shadow: 0px 4px 10px 1ppx rgba(0, 0, 0, 0.1);
}
.wrapper .title {
  height: 90px;
  background: #19ab8d;
  border-radius: 5px 5px 0 0;
  color: #fff;
  font-size: 30px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
}
.wrapper form {
  padding: 30px 25px 25px 25px;
}
.wrapper form .row {
  height: 45px;
  margin-bottom: 30px;
  position: relative;
}
.wrapper form .row input {
  height: 100%;
  width: 100%;
  outline: none;
  padding-left: 60px;
  border-radius: 5px;
  border: 1px solid lightgrey;
  font-size: 16px;
  transition: all 0.3s ease;
}
.wrapper form .row button {
  height: 100%;
  width: 100%;
  outline: none;
  font-weight: 600;
  border-radius: 5px;
  border: 1px solid lightgrey;
  font-size: 16px;
  transition: all 0.3s ease;
}

form .row input:focus {
  border-color: #16a085;
  box-shadow: inset 0px 0px 2px 2px rgba(26, 188, 156, 0.25);
}
.wrapper form .row i {
  position: absolute;
  width: 47px;
  height: 100%;
  color: #fff;
  font-size: 18px;
  background: #16a085;
  border: 1px solid #16a085;
  border-radius: 5px 0 0 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.wrapper form .pass {
  margin: -8px 0 20px 0;
}
.wrapper form .pass a {
  color: #16a085;
  font-size: 17px;
  text-decoration: none;
}
.wrapper form .pass a:hover {
  text-decoration: underline;
}
.wrapper form .pass input {
  color: #fff;
  font-size: 20px;
  font-weight: 500;
  padding-left: 0px;
  background: #16a085;
  border: 1px solid #16a085;
  cursor: pointer;
}
form .button input:hover {
  background: #12876f;
}
form button:hover {
  background: #16a085;
  color: #fff;
}
</style>
