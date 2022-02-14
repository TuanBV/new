<template>
  <div class="container-md mt-5">
    <div class="row justify-content-center">
      <div class="col-10" v-if="!isShow">
        <form v-if="show">
          <h4 class="title pb-3">Create Time Rate New</h4>
          <div class="row justify-content-md-center">
            <div class="col-3">
                <label for="username" class="form-label">Name Time Rate
                    <span class="">(Required)</span>
                </label>
            </div>
            <div class="col-6">
              <input type="text" class="form-control" v-model="data.nameTime"/>
            </div>
          </div>
          <div class="row justify-content-md-center">
            <div class="col-3">
                <label for="Age" class="form-label">Time Start
                  <span class="">(Required)</span>
                </label>
            </div>
            <div class="col-6">
              <input type="date" class="form-control" v-model="data.timeStart"/>
            </div>
          </div>
          <div class="row justify-content-md-center">
            <div class="col-3">
                <label for="Age" class="form-label">Time End
                  <span class="">(Required)</span>
                </label>
            </div>
            <div class="col-6">
              <input type="date" class="form-control" v-model="data.timeEnd"/>
            </div>
            <hr class="col-9 my-4"/>
          </div>
          <button type="button" class="btn btn-primary mt-3 w-25" @click="show=false">Create Time Rate</button>
          <router-link to="/time-rate"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back</button></router-link>
        </form>
        <!-- modal show infor time rate new -->
        <div v-else tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <h5 class="modal-title" id="exampleModalLabel">Do you want to create time rate new?</h5>
                      <button class="btn-close" aria-label="Close" @click="show=true"></button>
                  </div>
                  <div class="modal-body">
                    <table class="table table-borderless">
                      <tbody style="text-align: left;">
                        <tr>
                          <td class="w-50">Name time :</td>
                          <td>{{ data.nameTime }}</td>
                        </tr>                    
                        <tr>
                          <td>Time start :</td>
                          <td>{{ data.timeStart }}</td>
                        </tr>                    
                        <tr>
                          <td>Time end :</td>
                          <td>{{ data.timeEnd }}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div class="modal-footer">
                      <button class="btn btn-secondary" @click="show=true" >Close</button>
                      <button class="btn btn-primary" @click="add_timerate()">Agree</button>
                  </div>
              </div>
            </div>
        </div>
      </div>

      <!-- modal delete time rate success --> 
      <div data-bs-keyboard="false" tabindex="-1" aria-hidden="true" v-else>
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" @click="router.push('/time-rate')" class="btn-close" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="font-size: 20px; font-weight: 500;">
              Create time rate success !<i style="color: green;" class="fas fa-check-circle"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { reactive, ref } from '@vue/reactivity';
import axios from 'axios';
import router from '../../router/index'
// import schema from '../../schema/time_rate'
export default {
  setup(){
    const obj = JSON.parse(localStorage.getItem('user'))[0];
    const show = ref(true)
    const isShow = ref(false)

    var username = obj.username;
    const data = reactive({
      nameTime : '',
      timeStart: '',
      timeEnd: ''
    })
    // method 
    const add_timerate = async()=>{
      try {
        await axios.post('http://localhost:8000/admin/'+ username+'/timerate', data, { withCredentials: true })
        isShow.value = true
      } catch (error) {
        console.log(error);
      }
    }

    return {
      data,
      show,
      isShow,
      router,
      add_timerate
    }
  }
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
