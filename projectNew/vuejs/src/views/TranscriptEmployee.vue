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
                    <td colspan='2'> VN </td>
                    <th colspan='2'>Name Member :</th>
                    <td colspan='2'>{{  }}</td>
                </tr>
                <tr>
                    <th colspan='2'>Position : </th>
                    <td colspan='2'>{{  }}</td>
                    <th colspan='2'></th>
                    <td colspan='2'></td>
                </tr>
                <tr>
                    <th colspan='2'>Date start :</th>
                    <td colspan='2'>{{ infor.timeStart }}</td>
                    <th colspan='2'>Date end :</th>
                    <td colspan='2'>{{ infor.timeEnd }}</td>
                </tr>
                <tr>
                    <th colspan='2'>Censor :</th>
                    <td colspan='2'>{{ }}</td>
                    <th colspan='2'>Status : </th>
                    <td colspan='2' v-if="infor.status == 0"> Chưa Tạo</td>
                    <td colspan='2' v-else-if="infor.status == 1">Chưa Duyệt</td>
                    <td colspan='2' v-else-if="infor.status == 2">Đã Duyệt</td>
                    <td colspan='2' v-else-if="infor.status == 3">Trả Lại</td>
                    <td colspan='2' v-else>Lưu Tạm</td>
                </tr>
                <tr rowspan='2'>
                    <th colspan='2'>Time work</th>
                    <!-- // user enter time work -->
                    <td colspan='2'> <input type='date' class='form-label' style='margin-top: 1px;margin-bottom: 1px;line-height: 23px;'/></td>
                    <!-- //-------------------- -->
                    <th colspan='2'>Time work end</th>
                    <!-- // user enter time work -->
                    <td colspan='2'><input type='date' class='form-label' style='margin-top: 1px;margin-bottom: 1px;line-height: 23px;'/></td>
                </tr>
                <!-- //----------message error----- -->
                <!-- <tr style='border: none;'>
                    <td colspan='2'></td>
                    <td colspan='2'><p id='alerttimework' style='color: red;display: none;'>Please enter time work !</p></td>
                    <td colspan='2'></td> 
                    <td colspan='2'><p id='alerttimeworkend' style='color: red;display: none;'>Please enter time work end greater than time work !</p></td>
                </tr> -->
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
                            <td style="width: 10%"><input type="number" class="w-75"></td>
                            <td style="width: 10%"><input type="number" class="w-75"></td>
                            <td style="width: 10%"><textarea></textarea></td>
                        </tr>
                    </tbody> 
                    <tbody>
                        <tr>
                            <td colspan="3"></td>
                            <td style="width: 10%">100</td>
                            <td style="width: 10%">a</td>
                            <td style="width: 10%">a</td>
                            <td style="width: 10%"></td>
                        </tr>
                    </tbody>
                    <tbody id="note">
                        <tr>
                            <td colspan='7'>
                                <div class='row ps-4'>Manager's comments</div>
                                <textarea name='' style='width: 100%;background-color: #e9ecef;' rows='3' readonly></textarea>
                            </td>
                        </tr>
                    </tbody>
                    <!-- load opinionMember -->
                    <tbody>
                        <tr>
                            <td colspan="7">
                            <div class="row ps-4">The Member's opinion is evaluated</div>
                            <textarea name='' style="width: 100%;background-color: #e9ecef;" rows="3" id="opinion" readonly></textarea>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!-- load button click transcript -->
                <div v-for="infor in infors" :key="infor">
                    <router-link to="/transcript"  v-if="infor.status == 0"><button class='btn btn-primary me-5 w-25'>Send</button></router-link>
                    <router-link to="/transcript" v-if="infor.status == 2"><button class='btn btn-warning me-5'>Update</button></router-link>
                    <router-link to="/transcript"><button class='btn btn-danger w-25'>Back</button></router-link>
                </div>
                
            </form>
            <!-- <div class="col-3">
                <div class="modal">
                    <div class="modal-content" style="width: 400px">
                        <span class="close">&times;</span>
                        <p>Cập nhật bảng điểm <i style="color: green" class="fas fa-check-circle"></i>
                        </p>
                    </div>
                </div>
            </div> -->
            <!-- <div class="col-3">
                <div class="modal1" style="margin: 0;">
                    <div class="modal-content" style="width: 400px; ">
                        <span class="close">&times;</span>
                        <p id="content" style="color: red;"></p>
                    </div>
                </div>
            </div> -->
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
        const route = useRoute()
        const infors = ref([])
        const targets = ref([])
        const loading = ref(true)
    

        const obj = JSON.parse(localStorage.getItem('user'))[0];
        const username = obj.username;

        // method
        const load_data = async () => {
            try {
                const response = await axios.get('http://localhost:8000/user/'+ username +'/transcript/'+route.query.id, {headers: {token: document.cookie.split('=')[1]}});
                infors.value = response.data.infor
                targets.value = response.data.target
                loading.value = false
            } catch (error) {
                console.log(error.message);
            }
        }
        onMounted(() => {
            load_data();
        })
        return {
            username,
            infors,
            targets,
            loading,
            // method
            load_data,
        }
    },
}
</script>