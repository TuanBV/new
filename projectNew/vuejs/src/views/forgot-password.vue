<template>
  <div class="forgot-password">
    <div class="container">
      <div class="wrapper">
        <div class="title"><span>Account</span></div>
        <form>
          <div class="row">
            <i class="fas fa-envelope"></i>
            <input type="email" placeholder="Email" v-model="email" v-bind:class="{'is-invalid': email.length == 0}"/>
            <div class="invalid-feedback" v-if="email.length == 0">{{ error }}</div>
          </div>
          <div class="row">
            <button type="button" @click="send_email()">Submit</button>
          </div>
          <div class="pass">
            Back to <a @click="this.$router.push('/login')"> Login !!!</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// import axios from 'axios'
export default {
  name: "ForgotPassword",
  data() {
      return {
        error: '',
        email :''
    }
  },
  methods: {
      validate_email(){
        this.error = '';
        var inValid = true;
        if(!this.email){
          this.error = 'Please enter email';
          inValid = false;
        }
        return inValid;
      },
      send_email(){
        let formData = new FormData();
        formData.email = this.email;
        if(this.validate_email() == true){
          axios.post('http://127.0.0.1:8000/forgot-password',
            formData
          ).then(function(){
            console.log('SUCCESS!!');
          }).catch(function(){
            console.log('FAILURE!!');
          });
        }
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
