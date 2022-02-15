<template>
    <div v-if="loading">
        <div style="text-align: center;margin-top: 200px">
            Loading...<div id="loading" class="spinner-border text-warning" style="width: 20px;height: 20px;" role="status"></div>
        </div>
    </div>
    <div v-else class="transcript-employee">
        <div class="container">
            <table class="table" style="text-align:left; width:80%;margin-left: 10%; margin-top:20px;line-height: 40px;" v-for="infor in infors" :key="infor">
                <!-- load infor user -->
                <tr>
                    <th colspan='2'>Id Member : </th>
                    <td colspan='2'> 
                        <span>VN{{ infor.iduser }}</span>
                    </td>
                    <th colspan='2'>Name Member :</th>
                    <td colspan='2'>
                        <span>{{ infor.fullname }}</span>
                    </td>
                </tr>
                <tr>
                    <th colspan='2'>Position : </th>
                    <td colspan='2'>
                        <span v-if="infor.idposition==1">Admin</span>
                        <span v-else-if="infor.idposition==2">Manager</span>
                        <span v-else>Member</span>
                    </td>
                    <th colspan='2'></th>
                    <td colspan='2'></td>
                </tr>
                <tr>
                    <th colspan='2'>Date start :</th>
                    <td colspan='2'>
                        <span>{{ infor.timeStart }}</span>
                    </td>
                    <th colspan='2'>Date end :</th>
                    <td colspan='2'>
                        <span>{{ infor.timeEnd }}</span>
                    </td>
                </tr>
                <tr>
                    <th colspan='2'>Censor :</th>
                    <td colspan='2'> 
                        <span>{{ infor.censor }}</span>      
                    </td>
                    <th colspan='2'>Status : </th>
                    <td colspan="2">
                        <span v-if="infor.status == 0"> Chưa Tạo</span>
                        <span v-else-if="infor.status == 1">Chưa Duyệt</span>
                        <span v-else-if="infor.status == 2">Đã Duyệt</span>
                        <span v-else-if="infor.status == 3">Trả Lại</span>
                        <span v-else>Lưu Tạm</span>
                    </td>
                </tr>
                <tr>
                    <th colspan='2'>Time work</th>
                    <td colspan='2'> <input type='date' class='form-select w-75' v-model="infor.timework" readonly style="background-color: #e9ecef;"/></td>
                    <th colspan='2'>Time work end</th>
                    <td colspan='2'><input type='date' class='form-select w-75' v-model="infor.timeworkend" readonly style="background-color: #e9ecef;"/></td>
                </tr>

            </table>
        </div>        
        <div class="container">
            <hr class="my-4" />
            <!-- load name Transcript -->
            <h3 class="col-12 text-center text-uppercase my-3" style="font-weight: 600" v-for="infor in infors" :key="infor">{{ infor.nameTranscript }}</h3>
            <form style="margin-bottom: 200px;" method="get">
                <table class="table border table-bordered" style="width: 100%">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th style="width: 15%">Mục tiêu/Nhiệm vụ</th>
                            <th style="width: 40%">Tiêu chuẩn đánh giá</th>
                            <th style="width: 10%">Mục tiêu</th>
                            <th style="width: 10%">Kết quả</th>
                            <th style="width: 10%">Đánh giá</th>
                            <th style="width: 10%">Nhận xét</th>
                        </tr>
                    </thead>
                    <!-- load transcript Member -->
                    <tbody v-for="(target,index) in targets" :key="index">
                        <tr>
                            <td v-bind:rowspan="target.count">{{ index+1 }}</td>
                            <td style="width: 15%;" v-bind:rowspan="target.count">{{ target.nameTarget }}</td>
                        </tr>
                        <tr v-for="standard in target.standard" :key="standard">
                            <td style="width: 10%;text-align: left;">{{ standard.nameStandard }}</td>
                            <td style="width: 10%">{{ standard.scoreStandard }}</td>
                            <td style="width: 10%">
                                <input type="number" class="w-75" v-model="standard.TuDanhGia" style="text-align: center;background-color: #e9ecef;" readonly>
                            </td>
                            <td style="width: 10%" v-for="infor in infors" :key="infor">
                                <input type="number" class="w-75" v-if="(infor.status == 1 && !infor.opinion )||(infor.status == 2 && !infor.opinion)" v-model="standard.QLDanhGia" @change="infor.sumResultManager+=standard.QLDanhGia" style="text-align: center;" >
                                <input type="number" class="w-75" v-else v-model="standard.QLDanhGia" style="text-align: center;background-color: #e9ecef;" readonly>
                            </td>
                            <td style="width: 10%" v-for="infor in infors" :key="infor">
                                <textarea v-model="standard.NhanXet" v-if="(infor.status == 1 && !infor.opinion )||(infor.status == 2 && !infor.opinion)"></textarea>
                                <textarea v-model="standard.NhanXet" v-else style="text-align: center;background-color: #e9ecef;" readonly></textarea>
                            </td>
                        </tr>
                    </tbody> 
                    <tbody>
                        <tr v-for="infor in infors" :key="infor">
                            <td colspan="3"></td>
                            <td style="width: 10%">100</td>
                            <td style="width: 10%">{{ infor.sumScoreUser }}</td>
                            <td style="width: 10%">{{ infor.sumResultManager }}</td>
                            <td style="width: 10%"></td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <td colspan='7' v-for="infor in infors" :key="infor">
                                {{ infor }}
                                <div class='row ps-4'>Manager's comments</div>
                                <textarea class="w-100" rows='3' v-if="(infor.status == 1 && !infor.opinion )||(infor.status == 2 && !infor.opinion)" v-model="infor.ghichu"></textarea>
                                <textarea class="w-100" rows='3' v-else v-model="infor.ghichu" style="background-color: #e9ecef;" readonly></textarea>
                            </td>
                        </tr>
                    </tbody>
                    <!-- load opinion of member -->
                    <tbody>
                        <tr>
                            <td colspan="7" v-for="infor in infors" :key="infor">
                            <div class="row ps-4">The Member's opinion is evaluated</div>
                                <textarea style="width: 100%;background-color: #e9ecef;" rows="3" readonly></textarea>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!-- load button click transcript -->
                <div v-for="infor in infors" :key="infor">
                    <button class='btn btn-primary me-5 col-2' v-if="infor.status==1" @click.prevent="infor.status=2;confirm_transcript()">Confirm</button>
                    <button class='btn btn-warning me-5 col-2'  v-if="infor.status==1" @click.prevent="infor.status=3;confirm_transcript()">Reject</button>
                    <button class='btn btn-warning me-5 col-2' v-if="infor.status == 2 && infor.opinion == null" @click.prevent="confirm_transcript()">Update </button>
                    <router-link to="/manager"><button class='btn btn-danger col-2'>Back</button></router-link>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
import { useRoute } from 'vue-router'
import axios from 'axios'
import { ref } from '@vue/reactivity';
import { onMounted } from '@vue/runtime-core';

export default {
    setup() {
        const route = useRoute();
        const infors = ref([]);
        const targets = ref([]);
        const censors = ref([]);
        const obj = JSON.parse(localStorage.getItem('user'))[0];
        const username = obj.username;

        // method
        // load transcript
        const load_transcript = async () => {
            try {
                const response = await axios.get('http://localhost:8000/user/'+ username +'/transcript/'+route.query.id, {headers: {token: document.cookie.split('=')[1]}});
                infors.value = response.data.infor
                console.log(infors.value);
                targets.value = response.data.target
            } catch (error) {
                console.log(error.message);
            }
        }
        // send transcript
        const confirm_transcript = async ()=>{
            try {
                console.log(infors.value);
                console.log(targets.value);
                const response = await axios.put('http://localhost:8000/manager/'+username+'/transcript', 
                                                {
                                                    'infors': infors.value, 
                                                    'targets': targets.value
                                                }
                                            );
                console.log(response);
            } catch (error) {
                console.log(error.message)
            }
        }

        onMounted(() => {
            load_transcript();
        })
        return {
            username,
            infors,
            targets,
            censors,
            // method
            load_transcript,
            confirm_transcript,
        }
    },
}
</script>
<style scoped>
button, router-link{
    color: white;
}

</style>