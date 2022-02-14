// import axios from 'axios'
import { createStore } from 'vuex'
// import { useRouter } from 'vue-router';
export default createStore({
  state: {
    user : null
  },
  getters:{
    user: (state) => {
      return state.user;
    }
  },
  mutations: {
    user (state, user){
      state.user = user;
    }
  },
  actions: {
    user(context, user){
      context.commit('user', user);
    }
  },
  modules: {
  }
})
