<template>
    <div>
        <h1> {{message}}</h1>
        </div>
</template>
<script> 
import axios from 'axios'

export default {
    name:'Home',
    data () {
        return{
            message: 'Mensaje del servidor :D'
        }
    },
    methods: {
        getMessage(){
            const path = 'http://localhost:5000/api/message'
            axios.get(path).then((success) => {
                this.message = success.data
            })
            .catch((error) => {
                console.log(error)
            })
            
            }
        },
        created(){
            this.getMessage()
        } 
    }
    </script>
