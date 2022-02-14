<template>
  <div class="change-password">
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-4">
          <h3 class="my-3">Change Password</h3>
          <!-- v-on:click.prevent="change()" -->
          <form method="post" @submit.prevent="change()">
            <div class="form-row mb-3">
              <label for="" class="form-label">Password Now</label>
              <input
                type="password"
                class="form-control"
                v-model="password_now"
                :class="{'is-invalid': error_password_now}"
              />
              <div class="invalid-feedback" v-if="error_password_now">{{ error_password_now }}</div>
            </div>
            <div class="mb-3">
              <label for="" class="form-label">Password New</label>
              <input
                type="password"
                class="form-control"
                v-model="password_new"
                v-bind:class="{'is-invalid': error_password_new, 'is-valid': password_new.length > 7 && password_new.length < 15}"
              />
              <div class="invalid-feedback" v-if="password_new.length < 8 || password_new.length > 15">{{ error_password_new }}</div>
            </div>
            <div class="mb-3">
              <label for="" class="form-label">Confirm Password New</label>
              <input
                type="password"
                class="form-control"
                v-model="re_password_new"
                v-bind:class="{'is-invalid': error_re_password_new, 'is-valid': re_password_new.length > 7 && re_password_new.length < 15}"
              />
              <div class="invalid-feedback" v-if="re_password_new.length < 8 || re_password_new.length > 15">{{ error_re_password_new }}</div>
            </div>
            <button type="submit" class="btn btn-primary mt-3">
              Change Password
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// import '../schema/change_password.js'
import axios from 'axios'
import Ajv from 'ajv'
import normalise from 'ajv-error-messages'
import { ref } from '@vue/reactivity';
import schema from '../schema/change_password'
export default {
  name: "ChangePassword",
  setup(){
    const password_now = ref('');
    const password_new = ref('');
    const re_password_new = ref('');

    const ajv = new Ajv({allErrors: true}) // options can be passed, e.g. {allErrors: true}

    var error_password_now = ref(null);
    const error_password_new = ref('');
    const error_re_password_new = ref('');
    
    const update_password = async () => {
      const user = {
        password_now: password_now.value,
        password_new: password_new.value,
        re_password_new: re_password_new.value
      }
      const obj = JSON.parse(localStorage.getItem('user'))[0];
      var username = obj.username;
      try {
        const response = await axios.put('http://127.0.0.1:8000/user/'+username+'/change-password', user);
        // const data = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    }
    // sửa
    const change = async () => {
      const user = {
        password_now: password_now.value,
        password_new: password_new.value,
        re_password_new: re_password_new.value
      }
      
      const validate = ajv.compile(schema)
      const valid = validate(user)
      if (!valid){
        const ob = normalise(validate.errors)['fields'];
        ob.password_now ? error_password_now.value = ob.password_now[0] : error_password_now = '';
        ob.password_new ? error_password_new.value = ob.password_new[0] : error_password_new.value = '';
        ob.re_password_new ? error_re_password_new.value = ob.re_password_new[0] : error_re_password_new.value = '';
      }else{
        update_password();
      }
    }


    return {
      password_now,
      password_new,
      re_password_new,
      error_password_now,
      error_password_new,
      error_re_password_new,
      change
    }
  
  }
};
</script>

<style scoped>
.mb-3 {
  text-align: left;
}
.invalid-feedback{
    font-size: 14px;
}
</style>
