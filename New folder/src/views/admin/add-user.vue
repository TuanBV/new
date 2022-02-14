<template>
  <div class="container-md mt-5">
    <div class="row justify-content-center">
      <div class="col-10">
        <form>
          <h4 class="title pb-3">Create User</h4>
          <div class="row">
            <div class="col-3">
              <label for="fullname" class="form-label">Full Name</label>
            </div>
            <div class="col-9">
              <input type="text" class="form-control" v-model="data.fullname" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
                <label for="username" class="form-label">Username
                <span class="">(Required)</span>
                </label>
            </div>
            <div class="col-9">
              <input type="text" class="form-control" v-model="data.username" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
                <label for="email" class="form-label">Email 
                  <span class="" >(Required)</span>
                </label>
            </div>
            <div class="col-9">
              <input type="email" class="form-control" v-model="data.email" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
                <label for="Age" class="form-label">Birthday
                  <span class="text-muted"></span>
                </label>
            </div>
            <div class="col-9">
              <input type="date" class="form-control w-50" v-model="data.birthday" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
              <label for="address" class="form-label">Address</label>
            </div>
            <div class="col-9">
              <input type="text" class="form-control" v-model="data.address" />
            </div>
          </div>
          <div class="row">
            <div class="col-3">
                <label for="position" class="form-label">Position
                    <span class="">(Required)</span>
                </label>
            </div>
            <div class="col-9">
              <table class="col-12">
                <tr>
                  <td>
                    <label for="rdoPosition3" class="me-2">Member</label>
                    <input type="radio" id="rdoPosition3" value="3" v-model="data.idposition"/>
                  </td>
                  <td>  
                    <label for="rdoPosition2" class="me-2">Manager</label>
                    <input type="radio" id="rdoPosition2" value="2" v-model="data.idposition"/>
                  </td>
                </tr>
              </table>
            </div>
          </div>
          <hr class="col-12 my-4" />
          <button type="button" class="btn btn-primary mt-3 w-25" @click="add_user()">Create User</button>
          <router-link to="/admin"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back</button></router-link>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import { reactive } from '@vue/reactivity';
import axios from 'axios';
export default {
  name: "AddUser",
  setup(){
    const data = reactive({
      fullname : '',
      username : '',
      email : '',
      birthday : '',
      address : '',
      idposition : ''
    })
    const obj = JSON.parse(localStorage.getItem('user'))[0];
    const username = obj.username;
    // methods
    const add_user = async ()=>{
      try {
        await axios.post('http://127.0.0.1:8000/admin/'+username+'/users', data ,{headers: {token: document.cookie.split('=')[1]}})
      } catch (error) {
        console.log(error);
      }
    }

    return {
      data,
      add_user
    }
  }

  // methods: {
  //   validate_form_user(){
  //       this.error = {
  //           fullname: "",
  //           username: "",
  //           email: "",
  //           birthday: "",
  //           address: "",
  //           position: "",
  //       }
  //       if(this.user.fullname.length > 100){
  //           this.error.fullname = "Fullname more than 100 characters"
  //       }
  //       if(this.user.username.length < 4 || this.user.username.length > 30){
  //           this.error.username = "Username least 4 characters and more than 30 characters"
  //       }
  //   },
  //   create_user() {
  //   },
  // },
};
</script>
<style scoped>
.row{
  margin-top: 20px;
}
.col-3{
  text-align: left;
}
span {
  color: red;
}
</style>
