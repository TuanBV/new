<template>
  <div class="container-md mt-5">
    <div class="row justify-content-center">
      <div class="col-10">
        <form>
          <h4 class="title pb-3">Edit Time Rate New</h4>
          <div class="row justify-content-md-center">
            <div class="col-3">
                <label for="username" class="form-label">Name Time Rate
                    <span class="">(Required)</span>
                </label>
            </div>
            <div class="col-6">
              <input type="text" class="form-control"  v-model="data.nameTime"/>
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
          <button type="button" class="btn btn-primary mt-3 w-25">Create Time Rate</button>
          <router-link to="/time-rate"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back</button></router-link>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import { useRoute } from 'vue-router'
import { onMounted } from '@vue/runtime-core';
import { reactive } from '@vue/reactivity';
export default {
  name: "EditTimeRate",
  setup(){
    const route = useRoute()
    const obj = JSON.parse(localStorage.getItem('user'))[0];
    const username = obj.username;

    const data = reactive({
      id : '',
      nameTime : '',
      timeStart: '',
      timeEnd: ''
    })
    // methods
    const get_data = async()=>{
      try {
        const response = await axios.get('http://localhost:8000/admin/'+ username +'/timerate/'+route.query.id)
        data.id = response.data[0].idtime
        data.nameTime = response.data[0].nameTime
        data.timeStart = response.data[0].timeStart
        data.timeEnd = response.data[0].timeEnd
      } catch (error) {
        console.log(error);
      }
    }
    onMounted(()=>{
      get_data()
    })
    return {
      data,
      get_data,
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
