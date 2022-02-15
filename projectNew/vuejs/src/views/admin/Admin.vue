<template>
  <div id="admin">
    <div class="container-sm">
      <div class="row mb-2">
        <div class="col-3" style="text-align:left">
          <span class="me-3" style="font-weight: 500;font-size: 18px; ">Filter User</span>
          <button class="btn btn-danger" @click="reset_condition()">Reset Condition</button>
        </div>
        <div class="col-9" style="text-align: right;">
          <router-link to="/admin/add-user"><button class="btn col-2" style="background-color: #0C9723;color: white;font-weight: 500;" type="button">Add user</button></router-link>
        </div>
      </div>
      <div class="row mb-5">
        <div class="col-2">
          <select class="form-select" aria-label="Default select example" v-model="param.position">
            <option value="all">By position</option>
            <option value="2">Manager</option>
            <option value="3">Member</option>
          </select>
        </div>
        <div class="col-2">
          <input type="number" class="form-control" placeholder="By year" v-model="param.year">
        </div>
        <div class="col-2">
          <input type="text" class="form-control"  placeholder="By name" v-model="param.name">
        </div>
        <button class="btn col-2" style="background-color: #0C9723;color: white;font-weight: 500;" @click="load_user()">Filter</button>
      </div>
      <h3 class="col-12 text-center">List User</h3>
      <div class="row mb-3">
        <div class="col-2">
          <select class="form-select" aria-label="Default select example" v-model="param.sort" @change="load_user()">
            <option value="fullname">Sort by fullname</option>
            <option value="position">Sort by position</option>
          </select>
        </div>
        <div class="col-3">
          <select class="form-select" aria-label="Default select example" v-model="param.limit" @change="load_user()">
            <option value="12">Get 12 record number</option>
            <option value="2">Get 2 record</option>
            <option value="4">Get 4 record</option>
            <option value="8">Get 8 record</option>
          </select>
        </div>
        <div class="col-2" style="line-height: 38px;">
          Has {{ number_record }} record
        </div>
      </div>
      <table class="table table-striped border" width="100%">
        <thead>
          <tr>
            <th width="10%">STT</th>
            <th width="15%">Fullname</th>
            <th width="10%">Username</th>
            <th width="10%">Email</th>
            <th width="10%">Position</th>
            <th width="10%">Birthday</th>
            <th width="10%">Address</th>
            <th width="10%"></th>
          </tr>
        </thead>
        <tbody id="loadUser">
          <tr v-for="(user, index) in users" :key="index">
            <td width="10%">{{ param.limit*(param.page-1)+index+1 }}</td>
            <td width="15%">{{ user.fullname }}</td>
            <td width="10%">{{ user.username }}</td>
            <td width="10%">{{ user.email }}</td>
            <td width="10%">{{ user.name }}</td>
            <td width="10%" v-if="user.birthday != None">{{ user.birthday }}</td>
            <td width="10%" v-else> --- </td>
            <td width="10%">{{ user.address }}</td>
            <td width="20%">
              <router-link :to="{path:'/admin/edit-user', query: { id: user.iduser }}"><button class='btn btn-warning me-2'>Edit</button></router-link>
              <router-link to="/admin" @click="delete_user(user.iduser)"><button class='btn btn-danger'>Delete</button></router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="container load" ></div>
    <!-- load pagination -->
      <div class="container" style="margin-top: 100px;">
        <ul class="pagination pagination-sm" v-if="pages>1">
          <li class='page-item px-2 py-2' v-for="index in pages" :key="index"><button class='btn' style='border:1px solid #dee2e6;' @click="param.page=index;load_user();">{{ index }}</button></li>
        </ul>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import { ref, reactive } from '@vue/reactivity';
import { onMounted } from '@vue/runtime-core';
import { useRouter } from 'vue-router';
import { useLoading } from 'vue-loading-overlay'
export default {
  setup() {
    const users = ref([]);
    const obj = JSON.parse(localStorage.getItem('user'))[0];
    const username = obj.username;
    const router = useRouter();
    const pages = ref(0);
    const number_record = ref(0);
    const loading = useLoading();
    // condition filter
    const param = reactive({
      position: 'all',
      year: '',
      name: '',
      limit: 12,
      page: 1,
      sort: 'fullname'
    })
    // methods
    const reset_condition = async () => {
      param.position = 'all';
      param.year = '';
      param.name = '';
      param.limit = 12;
      param.page = 1;
      param.sort = 'fullname';
      load_user();
    }
    // delete user
    const delete_user = async(id)=>{
      try {
        await axios.delete('http://127.0.0.1:8000/admin/'+username+'/users/'+id)
        load_user();
      } catch (error) {
        console.log(error);
      }
    }
    // load user
    const load_user = async () => {
      try {
        const loader = loading.show({
          fullPage: true,
          canCancel: true,
          useSlot: false,
          loader: 'bars',
          color: '#00ab00',
          bgColor: '#4b4b4b',
          height: 64,
          width: 64,
        });
        const response = await axios.get('http://localhost:8000/admin/'+ username +'/users', {params : param}, {headers: {token: document.cookie.split('=')[1]}});
        users.value = response.data.data
        number_record.value = response.data.count
        pages.value = Math.ceil(response.data.count/param.limit);
        loader.hide();

      } catch (error) {
        console.log(error.message);
      }
    }
    onMounted(() => {
      load_user();
    })
    return {
      username,
      param,
      pages,
      router,
      load_user,
      reset_condition,
      delete_user,
      users,
      number_record
    }
  }
}
</script>

<style scoped>
#admin{
  margin-top: 20px;
}
router-link{
  color: white;
}
.vld-overlay {
  float: right;
}
</style>