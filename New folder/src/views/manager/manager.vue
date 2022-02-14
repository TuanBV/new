<template>
  <div class="manager">
    <div class="container mt-2">
      <div class="row mb-3" style="text-align: left">
        <div class="col-9">
          <span class="me-3" style="font-weight: 500;font-size: 18px; ">Filter</span>
          <button class="btn btn-danger" @click="reset_condition()">Reset Condition</button>
        </div>
      </div>
      <div class="row mb-2">
        <div class="col-2">
          <select class="form-select" aria-label="Default select example" v-model="param.nameTime">
            <option value='all'>By name time</option>
            <!-- load name time rate -->
            <option v-for="condition in conditions" v-bind:key="condition" :value="condition.nameTime">
              {{ condition.nameTime }}
            </option>
          </select>
        </div>
        <div class="col-2">
          <select class="form-select" aria-label="Default select example">
            <option value="all">By status</option>
            <option value="0">Chưa Tạo</option>
            <option value="1">Chưa Duyệt</option>
            <option value="2">Đã Duyệt</option>
            <option value="3">Trả Lại</option>
          </select>
        </div>
        <div class="col-2">
          <input type="number" class="form-control" placeholder="By score user..." v-model="param.scoreUser" min="0" max="100">
        </div>
        <div class="col-2">
          <input type="number" class="form-control" placeholder="By score manager..." v-model="param.scoreManager" min="0" max="100">
        </div>
        <button class="btn col-2" style="background-color: #0c9723; color: white; font-weight: 500" @click="load_data()">Filter Transcript</button>
      </div>
      <!-- <div class="row ms-0 mb-2 fade record">Record number : <p id="record"></p> </div> -->
    </div>
    <div class="container mt-5">
      <h3 class="col-12 text-center">List Transcript</h3>
      <div class="row mb-3">
        <div class="col-3">
          <select class="form-select" aria-label="Default select example" v-model="param.sort" @change="load_data()">
            <option value="nameTranscript">Sort by Name Transcript</option>
            <option value="username">Sort by Username </option>
            <option value="status">Sort by Status </option>
            <option value="sumUserAsc">Sort by Sum User &uarr;</option>
            <option value="sumUserDesc">Sort by Sum User &darr;</option>
            <option value="sumManagerAsc">Sort by Sum Manager &uarr;</option>
            <option value="sumManagerDesc">Sort by Sum Manager &darr;</option>
          </select>
        </div>
        <div class="col-3">
          <select class="form-select" aria-label="Default select example" v-model="param.limit" @change="load_data()">
            <option value="12">Get 12 record</option>
            <option value="1">Get 1 record</option>
            <option value="20">Get 20 record</option>
            <option value="30">Get 30 record</option>
          </select>
        </div>
        <div class="col-3" style="line-height: 38px;" id="sumfilter">
          <!-- load sum filter transcript -->
        </div>
      </div>
      <table class="table table-striped border" width="100%">
        <thead>
          <tr>
            <th width="10%">#</th>
            <th width="20%">Name transcipt</th>
            <th width="10%">Username</th>
            <th width="10%">Fullname</th>
            <th width="10%">Status</th>
            <th width="10%">Self-assessment</th>
            <th width="10%">Points evaluated</th>
            <th width="10%"></th>
          </tr>
        </thead>
        <tbody>
          <!-- Load data transcript manager -->
          <tr v-for="(transcript, index) in transcripts" :key="index">
            <td width="10%">{{ param.limit*(param.page-1)+index+1 }}</td>
            <td width="20%">{{ transcript.nameTranscript }}</td>
            <td width="10%">{{ transcript.username }}</td>
            <td width="10%">{{ transcript.fullname }}</td>
            <td width="10%">{{ transcript.status }}</td>
            <td width="10%">{{ transcript.sumResultManager }}</td>
            <td width="10%">{{ transcript.sumScoreUser }}</td>
            <td width="10%">
              <router-link :to="{path:'/transcript-employee', query: { id: transcript.idtranscript }}" v-if="transcript.status == 1 || transcript.status == 2"><button class='btn btn-warning'>View</button></router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- load pagination -->
      <div class="container" style="margin-top: 100px;">
        <ul class="pagination pagination-sm" v-if="pages>1">
          <li class='page-item px-2 py-2' v-for="index in pages" :key="index"><button class='btn' style='border:1px solid #dee2e6;' @click="param.page=index;load_data();">{{ index }}</button></li>
        </ul>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { reactive, ref } from '@vue/reactivity';
import { onMounted } from '@vue/runtime-core';
export default {
  setup() {
    const transcripts = ref([]);
    const conditions = ref([]);
    const pages = ref(0);

    const obj = JSON.parse(localStorage.getItem('user'))[0];
    const username = obj.username;
    // condition
    const param = reactive({
      nameTime : 'all',
      status : 'all',
      scoreUser: '',
      scoreManager: '',
      limit: 12,
      page : 1,
      sort: 'nameTranscript'
    })
    // methods
    const load_condition = async () =>{
      try {
        const response = await axios.get('http://localhost:8000/condition-nametime');
        conditions.value = response.data
      } catch (error) {
        console.log(error.message);
      }
    }
    // load data
    const load_data = async () => {
      try {
        console.log(param);
        const response = await axios.get('http://localhost:8000/manager/'+ username +'/transcript', {params : param}, {headers: {token: document.cookie.split('=')[1]}});
        transcripts.value = response.data.data;
        pages.value = Math.ceil(response.data.count/param.limit);
      } catch (error) {
        console.log(error.message);
      }
    }
    // delete condition filter
    const reset_condition = async () => {
      param.nameTime = 'all';
      param.status = 'all';
      param.scoreUser = '';
      param.scoreManager = '';
      param.limit = 12;
      param.page = 1;
      param.sort = 'nameTranscript';
      load_data();
    }
    onMounted(() => {
      load_condition();
      load_data();
    })
    return {
      username,
      load_condition,
      reset_condition,
      load_data,
      param,
      conditions,
      transcripts,
      pages
    }
  }
}
</script>