<template>
  <div class="container-md mt-5">
    <div class="row justify-content-center">
      <div class="col-10">
            <form v-for="infor in infors" :key="infor">
                <h4 class="title pb-3">Update Profile User</h4>
                <div class="row">
                    <div class="col-3">
                        <label for="fullname" class="form-label">Full Name</label>
                    </div>
                    <div class="col-9">
                        <input type="text" class="form-control" v-model="infor.fullname" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="username" class="form-label">Username
                            <span class="">(Required)</span>
                        </label>
                    </div>
                    <div class="col-9">
                        <input type="text" class="form-control" v-model="infor.username" style="background-color: #e9ecef" readonly/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="email" class="form-label">Email 
                            <span class="" >(Required)</span>
                        </label>
                    </div>
                    <div class="col-9">
                        <input type="email" class="form-control" v-model="infor.email" style="background-color: #e9ecef" readonly/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="Age" class="form-label">Birthday
                            <span class="text-muted"></span>
                        </label>
                    </div>
                    <div class="col-9">
                        <input type="date" class="form-control w-50" v-model="infor.birthday"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="address" class="form-label">Address</label>
                    </div>
                    <div class="col-9">
                        <input type="text" class="form-control" v-model="infor.address"/>
                    </div>
                </div>
                <div class="row">
                    <div class="col-3">
                        <label for="position" class="form-label">Position
                            <span class="" >(Required)</span>
                        </label>
                    </div>
                    <div class="col-9">
                    <table class="col-12">
                        <tr>
                            <td>
                                <label for="rdoPosition3" class="me-2">Member</label>
                                <input type="radio" v-model="infor.idposition" id="rdoPosition3" value="3" />
                            </td>
                            <td>  
                                <label for="rdoPosition2" class="me-2">Manager</label>
                                <input type="radio" v-model="infor.idposition" id="rdoPosition2" value="2"/>
                            </td>
                            <td v-if="infor.idposition==1">  
                                <label for="rdoPosition1" class="me-2">Admin</label>
                                <input type="radio" v-model="infor.idposition" id="rdoPosition1" value="1"/>
                            </td>
                        </tr>
                    </table>
                    </div>
                </div>
                <hr class="my-4" />
                <button type="button" class="btn btn-primary mt-3 w-25" >Update User</button>
                <router-link to="/admin"><button type="button" class="btn btn-danger mt-3 ms-3 w-25">Back</button></router-link>
            </form>
       </div>
    </div>
  </div>
</template>
<script>
import { ref } from "@vue/reactivity"
import { onMounted } from "@vue/runtime-core";
import axios from "axios";
import { useRoute } from "vue-router";


export default ({
    setup() {
        const infors = ref([]);
        const route = useRoute();

        const obj = JSON.parse(localStorage.getItem('user'))[0];
        const username = obj.username;

        // methods 
        // load infor of user
        const load_data = async ()=> {
            try {
                const response = await axios.get('http://localhost:8000/admin/'+username+'/users/'+route.query.id);
                infors.value = response.data
            } catch (error) {
                console.log(error);
            }
        }
        onMounted(()=>{
            load_data();
        })
        return {
            infors,
            // method
            load_data
        }
    },
})
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
