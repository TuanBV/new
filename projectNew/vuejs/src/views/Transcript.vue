<template>
  <div v-if="loading">
    <div style="text-align: center;margin-top: 200px">
        Loading...<div id="loading" class="spinner-border text-warning" style="width: 20px;height: 20px;" role="status"></div>
    </div>
  </div>
  <div v-else id="transcript">
    <div class="container">
      <div class="row mb-2">
        <div class="col-12" style="text-align: left;">
          <span class="me-3" style="font-weight: 500;font-size: 18px; ">Filter Transcript</span>

          <button class="btn btn-danger" @click="reset_condition()">Reset Condition</button>
        </div>
      </div>
      <div class="row mb-5">
        <div class="col-3">
          <!-- load name time rate -->
          <select class="form-select" aria-label="Default select example" v-model="param.nameTime">
            <option value='all'>By name time</option>
            <option v-for="condition in conditions" v-bind:key="condition" :value="condition.nameTime">
              {{ condition.nameTime }}
            </option>
          </select>
        </div>
        <div class="col-2">
          <select id="sel2" class="form-select" aria-label="Default select example" v-model="param.status">
            <option value="all">By status</option>
            <option data-option="2" value="0">Chưa Tạo</option>
            <option data-option="2" value="1">Chưa Duyệt</option>
            <option data-option="2" value="2">Đã Duyệt</option>
            <option data-option="2" value="3">Trả Lại</option>
            <option data-option="2" value="4">Lưu Tạm</option>
          </select>
        </div>
        <div class="col-2">
          <input type="number" class="form-control" placeholder="By score user " v-model="param.scoreUser" min="0" max="100">
        </div>
        <div class="col-2">
          <input type="number" class="form-control" placeholder="By score manager" v-model="scoreManager" min="0" max="100">
        </div>
        <button class="btn col-2" style="background-color: #0C9723;color: white;font-weight: 500;" type="button" @click="load_data()">Filter Transcript</button>
      </div>
      <h3 class="col-12 text-center mb-4">List Transcript</h3>
      <div class="row mb-3">
        <div class="col-3">
          <select class="form-select" aria-label="Default select example" v-model="param.sort" @change="load_data()">
            <option value="nameTranscriptAsc">Sort by name transcript &uarr;</option>
            <option value="nameTranscriptDesc">Sort by name transcript &darr;</option>
            <option data-option="4" value="sumUserAsc">Sort by Sum User &uarr;</option>
            <option data-option="4" value="sumUserDesc">Sort by Sum User &darr;</option>
            <option data-option="4" value="sumManagerAsc">Sort by Sum Manager &uarr;</option>
            <option data-option="4" value="sumManagerDesc">Sort by Sum Manager &darr;</option>
          </select>
        </div>
        <div class="col-3">
          <select class="form-select" aria-label="Default select example" v-model="param.limit" @change="load_data()">
            <option value="12">Get 12 record</option>
            <option value="1">Get 1 record</option>
            <option value="10">Get 10 record</option>
            <option value="20">Get 20 record</option>
          </select>
        </div>
        <div class="col-2" style="line-height: 38px;">
          Has {{ number_record }} record
        </div>

      </div>
      <table class="table border">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name transcipt</th>
            <th scope="col">Status</th>
            <th scope="col">Censor</th>
            <th width="15%">Self-assessment</th>
            <th width="15%">Points evaluated</th>
            <th scope="col-2"></th>
          </tr>
        </thead>
        <!-- load transcript of user -->
        <tbody>
          <tr v-for="(transcript, index) in transcripts" :key="index">
            
            <td scope="col">{{ param.limit*(param.page-1)+index+1 }}</td>
            <td scope="col">{{ transcript.nameTranscript }}</td>
            <td scope="col">
              <p v-if="transcript.status == 0">Chưa tạo</p>
              <p v-else-if="transcript.status == 1">Chờ duyệt</p>
              <p v-else-if="transcript.status == 2">Đã duyệt</p>
              <p v-else-if="transcript.status == 3">Trả lại</p>
              <p v-else>Lưu tạm</p>
            </td>
            <td scope="col" v-if="transcript.censor != ''">{{ transcript.censor }}</td>
            <td scope="col" v-else>...</td>
            <td width="15%">{{ transcript.sumScoreUser }}</td>
            <td width="15%">{{ transcript.sumResultManager }}</td>
            <td scope="col-2">
              <router-link :to="{path:'/transcript-employee', query: { id: transcript.idtranscript }}" v-if="transcript.status == 0"><button class='btn btn-warning'>Create</button></router-link>
              <router-link :to="{path:'/transcript-employee', query: { id: transcript.idtranscript }}" v-else-if="transcript.status == 2 || transcript.status==1"><button class='btn btn-warning'>View</button></router-link>
              <router-link :to="{path:'/transcript-employee', query: { id: transcript.idtranscript }}" v-else><button class='btn btn-warning'>Edit</button></router-link>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="col-3">
        <div class="modal">
          <div class="modal-content" style="width: 400px;">
            <span class="close">&times;</span>
            <p id="title-modal" style="color: red;"></p>
          </div>
        </div>
      </div>
      <!-- load pagination -->
      <div style="margin-top: 100px;">
        <ul class="pagination pagination-sm" v-if="pages>1">
          <li class='page-item px-2 py-2' v-for="index in pages" :key="index"><button class='btn' style='border:1px solid #dee2e6;' @click="param.page=index;load_data();">{{ index }}</button></li>
        </ul>
      </div>
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
    const number_record = ref(0)

    // condition filter
    const param = reactive({
      nameTime: 'all',
      status: 'all',
      scoreUser: '',
      scoreManager: '',
      limit: 12,
      page: 1,
      sort: 'nameTranscriptAsc'
    })

    const obj = JSON.parse(localStorage.getItem('user'))[0];
    var username = obj.username;

    // methods
    // load condition 
    const load_condition = async () =>{
      try {
        const response = await axios.get('http://localhost:8000/condition-nametime');
        conditions.value = response.data;
      } catch (error) {
        console.log(error.message);
      }
    }
    // load data
    const load_data = async () => {
      try {
        const response = await axios.get('http://localhost:8000/user/'+ username +'/transcript', {params : param}, {headers: {token: document.cookie.split('=')[1]}});
        transcripts.value = response.data.data;
        number_record.value = response.data.count
        pages.value = Math.ceil(response.data.count/param.limit);
      } catch (error) {
        console.log(error);
      }
    }
    // delete condition filter
    const reset_condition = async () => {
      param.name_time = 'all';
      param.status = 'all';
      param.score_user = '';
      param.score_manager = '';
      param.limit = 12;
      param.page = 1;
      param.pagination = 0;
      param.sort = 'nameTranscriptAsc';
      load_data();
    }
    onMounted(() => {
      load_condition();
      load_data();
    })
    return {
      conditions,
      username,
      param,
      pages,
      transcripts,
      number_record,
      // methods
      load_condition,
      reset_condition,
      load_data,
    }
  }
}
</script>
<style scoped>
#transcript{
  margin-top: 20px;
}

</style>
