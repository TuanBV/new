<template>
  <div id="timerate">
    <div class="container" v-if="show">
      <div v-if="isShow==false">
        <div class="row mb-2">
            <div class="col-3" style="text-align:left">
                <span class="me-3" style="font-weight: 500;font-size: 18px; ">Filter User</span>
                <button class="btn btn-danger" @click="reset_condition()">Reset Condition</button>
            </div>
            <div class="col-9" style="text-align: right;">
                <router-link to="/admin/add-time-rate"><button class="btn col-2" style="background-color: #0C9723;color: white;font-weight: 500;" type="button">Add Time Rate</button></router-link>
            </div>
        </div>
        <div class="row mb-5">
            <div class="col-3">
                <input type="text" class="form-control" placeholder="By name time " v-model="param.name">
            </div>
            <button class="btn col-2" style="background-color: #0C9723;color: white;font-weight: 500;" @click="load_timerate()">Filter Time Rate</button>
        </div>
        <h3 class="col-12 text-center">List Time Rate</h3>
        <div class="row mb-3">
            <div class="col-3">
              <select id="sel3" class="form-select" aria-label="Default select example" v-model="param.sort" @change="load_timerate()">
                <option value="nameTimeAsc">Sort by Name Time &uarr;</option>
                <option value="nameTimeDesc">Sort by Name Time &darr;</option>
                <option  value="timeStartAsc">Sort by Time Start &uarr;</option>
                <option  value="timeStartDesc">Sort by Time Start &darr;</option>
                <option  value="timeEndAsc">Sort by Time End &uarr;</option>
                <option  value="timeEndDesc">Sort by Time End &darr;</option>
              </select>
            </div>
            <div class="col-3">
              <select id="sel" class="form-select" aria-label="Default select example" v-model="param.limit" @change="load_timerate()">
                <option value="12">Get 12 record</option>
                <option value="1">Get 1 record</option>
                <option value="4">Get 4 record</option>
                <option value="8">Get 8 record</option>
              </select>
            </div>
            <div class="col-2" style="line-height: 38px;">
              Has {{ number_record }} record
            </div>
        </div>
        <table class="table table-striped border">
            <thead>
                <tr>
                    <th>#</th>
                    <th width="25%">Name time rate</th>
                    <th width="15%">Time start</th>
                    <th width="15%">Time end</th>
                    <th width="10%">Evaluated</th>
                    <th width="10%">Sum user</th>
                    <th width="25%"></th>
                </tr>
            </thead>
            <tbody>
                <!-- Load data for time rate -->
                <tr v-for="(timerate, index) in timerates" :key="index"> 
                    <td>{{ param.limit*(param.page-1)+index+1 }}</td>
                    <td width="25%">{{ timerate.nameTime }}</td>
                    <td width="15%">{{ timerate.timeStart }}</td>
                    <td width="15%">{{ timerate.timeEnd }}</td>
                    <td width="10%">{{ timerate.count1 }}</td>
                    <td width="10%">{{ timerate.count2 }}</td>
                    <td width="20%">
                        <router-link :to="{path:'/admin/time-rate/detail', query: { id: timerate.idtime }}"><button class='btn btn-primary me-2'>Detail</button></router-link>
                        <router-link :to="{path:'/admin/edit-time-rate', query: { id: timerate.idtime }}"><button class='btn btn-warning me-2'>Edit</button></router-link>
                        <router-link to="/time-rate" @click="get_record(timerate.idtime)"><button class='btn btn-danger'>Delete</button></router-link>
                    </td>
                </tr>
            </tbody>
        </table>
        <!-- load pagination -->
          <div class="container" style="margin-top: 100px;">
            <ul class="pagination pagination-sm" v-if="pages>1">
              <li class='page-item px-2 py-2' v-for="index in pages" :key="index"><button class='btn' style='border:1px solid #dee2e6;' @click="param.page=index;load_timerate();">{{ index }}</button></li>
            </ul>
          </div>
      </div>
    <!-- modal delete time rate success -->
      <div data-bs-keyboard="false" tabindex="-1" aria-hidden="true" v-if="isShow">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" @click="isShow=false" class="btn-close" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="font-size: 20px; font-weight: 500;">
              Delete time rate success !<i style="color: green;" class="fas fa-check-circle"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- modal show infor time rate delete -->
    <div v-else tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
          <div class="modal-content">
              <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">Do you want to delete this time rate?</h5>
                  <button class="btn-close" @click="show=true" aria-label="Close"></button>
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
                  <button class="btn btn-secondary" @click="show=true">Close</button>
                  <button class="btn btn-primary" @click="delete_timerate(data.idtime)">Agree</button>
              </div>
          </div>
        </div>
      <!-- load pagination -->
        <div class="container" style="margin-top: 100px;">
          <ul class="pagination pagination-sm" v-if="pages>1">
            <li class='page-item px-2 py-2' v-for="index in pages" :key="index"><button class='btn' style='border:1px solid #dee2e6;' @click="param.page=index;load_user();">{{ index }}</button></li>
          </ul>
        </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import { ref, reactive } from '@vue/reactivity';
import { onMounted } from '@vue/runtime-core';
export default {
  name: "timerate",
  setup() {
    const timerates = ref([]);
    const show = ref(true);
    const isShow = ref(false);


    const pages = ref(0);
    const number_record = ref(0);
    const obj = JSON.parse(localStorage.getItem('user'))[0];
    var username = obj.username;

    // condition filter
    const param = reactive({
      name: '',
      limit: 12,
      page: 1,
      sort: 'nameTimeAsc'
    })
    // methods
    const reset_condition = async () => {
      param.name = '';
      param.limit = 12;
      param.page = 1;
      param.sort = 'nameTimeAsc';
      load_timerate();
    }
    const load_timerate = async () => {
      try {
        const response = await axios.get('http://localhost:8000/admin/'+ username +'/timerate', {params : param}, {headers: {token: '1111111'} },{ withCredentials: true });
        timerates.value = response.data.data;
        number_record.value = response.data.count
        pages.value = Math.ceil(response.data.count/param.limit);
      } catch (error) {
        console.log(error.message);
      }
    }

    const delete_timerate = async(id)=>{
      try {
        await axios.delete('http://127.0.0.1:8000/admin/'+username+'/timerate/'+id);
        load_timerate();
        show.value = true;
        isShow.value = true;
      } catch (error) {
        console.log(error);
      }
    }
    const data = reactive({
      idtime: '',
      nameTime : '',
      timeStart : '',
      timeEnd : ''
    })
    const get_record = async(id)=>{
      try {
        const response = await axios.get('http://localhost:8000/admin/'+ username +'/timerate/'+ id);
        show.value = false;
        data.idtime = response.data[0].idtime;
        data.nameTime = response.data[0].nameTime;
        data.timeStart = response.data[0].timeStart;
        data.timeEnd = response.data[0].timeEnd;
      } catch (error) {
        console.log(error);
      }
    }
    onMounted(() => {
      load_timerate();
    })
    return {
      username,
      param,
      timerates,
      show,
      isShow,
      data,
      pages,
      number_record,
      load_timerate,
      reset_condition,
      delete_timerate,
      get_record
    }
  },
}
</script>

<style scoped>
#timerate{
  margin-top: 20px;
}
</style>
