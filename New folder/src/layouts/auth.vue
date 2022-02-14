<template>
    <NavBar/>
    <!-- slot có thể thay thế bằng router-view -->
    <slot/>
</template>
<script>
import NavBar from "../components/navbar.vue"
import { mapGetters } from 'vuex'
export default {
    components:{
        NavBar
    },
    computed: {
        ...mapGetters(['user'])
    }
}
</script>