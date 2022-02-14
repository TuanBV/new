import { ref } from 'vue'
import axios from 'axios';
// import { useStore } from 'vuex'

const error = ref(null);
const isLoading = ref(false);
async function signin(username, password){
    error.value = null;
    isLoading.value = true;
    // const store = useStore();
    try {
        const response = await axios.post("http://localhost:8000/users/login/"+username, {username : username, password: password})
        if(!response) throw new Error("Username or password is invalid !");
        localStorage.setItem('user', JSON.stringify(response.data));
        // store.dispatch('user', response.data);
        return response;
    } catch (err) {
        error.value = err.response.data.message;
    } finally{
        isLoading.value = false;
    }
}

export function useSignIn(){
    return { error, isLoading, signin };
}