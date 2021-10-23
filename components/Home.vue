<template lang="html">
    <div class="">
        <p> {{mensaje}} </p>
        </div>   
</template>

<script> 
import axios from 'axios'
export default {
    name: 'Main',
    data() {
        return {
            mensaje: 'Nuevo mensaje desde Vue JS'
        }
    }

}, 
methods: {
    getMensaje(){
        const path = 'http://localhost:5000/api'
    axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
    })
    .catch((error) => {
        console.error(error);
    })
    }
}
</script>

<style lang="css" scoped>
</style>