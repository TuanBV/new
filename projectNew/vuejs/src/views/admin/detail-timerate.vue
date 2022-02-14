<template>
    <div v-if="loading">
        <div style="text-align: center;margin-top: 200px">
            Loading...<div id="loading" class="spinner-border text-warning" style="width: 20px;height: 20px;" role="status"></div>
        </div>
    </div>

    <div v-else class="detail-timerate">
        <div class="container">
            <form method="get">
                <div class="row mb-2">
                <div class="col-12" style="text-align: left;">
                    <span class="me-3" style="font-weight: 500;font-size: 18px; ">Filter Transcript</span>
                    <button class="btn btn-danger" @click="reset_condition()">Reset Condition</button>
                </div>
                </div>
                <div class="row mb-5">
                <div class="col-2">
                    <select id="sel2" class="form-select" aria-label="Default select example" onchange="">
                    <option value="all">By status</option>
                    <option data-option="2" value="0">Chưa Tạo</option>
                    <option data-option="2" value="1">Chưa Duyệt</option>
                    <option data-option="2" value="2">Đã Duyệt</option>
                    <option data-option="2" value="3">Trả Lại</option>
                    <option data-option="2" value="4">Lưu Tạm</option>
                    </select>
                </div>
                <div class="col-2">
                    <input type="number" class="form-control" placeholder="By score user " id="scoreUser" v-model="score_user" min="0">
                </div>
                <div class="col-2">
                    <input type="number" class="form-control" placeholder="By score manager" id="scoreManager" v-model="score_manager" min="0">
                </div>
                <button class="btn col-2" style="background-color: #0C9723;color: white;font-weight: 500;" type="button" @click="load_data()">Filter Transcript</button>
                </div>
            </form>
        </div>
        <div class="container">
            <h3 class="col-12 text-center my-4" id="title-timerate"></h3>
            <div class="row mb-3">
                <div class="col-3">
                <select id="sel3" class="form-select" aria-label="Default select example" onchange="getRecord()">
                    <option data-option="4" value="username">Sort by Username </option>
                    <option data-option="4" value="status">Sort by Status </option>
                    <option data-option="4" value="sumUserAsc">Sort by Sum User &uarr;</option>
                    <option data-option="4" value="sumUserDesc">Sort by Sum User &darr;</option>
                    <option data-option="4" value="sumManagerAsc">Sort by Sum Manager &uarr;</option>
                    <option data-option="4" value="sumManagerDesc">Sort by Sum Manager &darr;</option>
                </select>
                </div>
                <div class="col-3">
                <select id="sel" class="form-select" aria-label="Default select example" onchange="getRecord()">
                    <option value="12">Get 12 record</option>
                    <option data-option="4" value="10">Get 10 record</option>
                    <option data-option="4" value="20">Get 20 record</option>
                    <option data-option="4" value="30">Get 30 record</option>
                </select>
                </div>
            </div>
            <table class="table table-striped border" width="100%">
                <thead>
                <tr>
                    <th width="10%">#</th>
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
                        <td width="10%">{{ index+1 }}</td>
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
            <div class="container" style="margin-top: 100px;text-align: center;">
            <ul class="pagination pagination-sm" id="addPagination">
                <!-- load pagination -->
            </ul>
            <!-- http://127.0.0.1:5500/view/TimeRate.html#l=12&p=0 -->
            <router-link to="/time-rate"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back Time Rate</button></router-link>
        </div>
  </div>
</template>
<script>
import { ref } from '@vue/reactivity'
export default {
    name: "detail-time-rate",
    setup(){
        const loading = ref(false)


        return {
            loading,
        }
    }
    
}
</script>
<style scoped>
.container{
  margin-top: 20px;
}
</style>
