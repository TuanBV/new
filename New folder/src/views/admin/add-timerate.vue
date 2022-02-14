<template>
  <div class="container-md mt-5">
    <div class="row justify-content-center">
      <div class="col-10">
        <form>
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
          <button type="button" class="btn btn-primary mt-3 w-25" @click="add_timerate()">Create Time Rate</button>
          <router-link to="/time-rate"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back</button></router-link>
        </form>
      </div>
    </div>
  </div>
  <div class="modal1" v-if="show">
    <div tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h6 class="modal-title"></h6>
            <button type="button" class="btn-close" @click="router.push('/time-rate')" aria-label="Close"></button>
          </div>
          <div class="modal-body" style="font-size: 20px;">
            <p>Create time rate new successfully <i class="fas fa-check" style="color: green;font-size: 30px;"></i></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { reactive, ref } from '@vue/reactivity';
import { useLoading } from 'vue-loading-overlay' 
import axios from 'axios';
import { useRouter } from 'vue-router'
// import schema from '../../schema/time_rate'
export default {
  setup(){
    const obj = JSON.parse(localStorage.getItem('user'))[0];
    const username = obj.username;
    const show = ref(false);
    const loading = useLoading();
    const router = useRouter();

    const data = reactive({
      nameTime : '',
      timeStart: '',
      timeEnd: ''
    })
    // method 
    const add_timerate = async()=>{
      try {
        loading.show().hide();
        await axios.post('http://localhost:8000/admin/'+ username+'/timerate', data, { withCredentials: true });
        show.value = true;
      } catch (error) {
        console.log(error);
      }
    }

    return {
      data,
      router,
      show,
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
.modal1 {
  position: fixed;
  z-index: 1;
  padding-top: 180px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
}
</style>
