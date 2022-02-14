import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'vuelidate'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "@fortawesome/fontawesome-free"

import { registerGlobalComponents} from "./utils/import"

const app = createApp(App)

registerGlobalComponents(app);
app.use(store);
app.use(router);
app.mount('#app');