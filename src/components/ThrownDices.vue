<script>

    export default{
        data(){
            return {
                thrown: [1, 2, 3, 4, 5]
            }
        },
        methods:{
            throw(){
                self.thrown = []

                for(let i = 0; i<5; i++){
                    self.thrown.push(Math.floor(Math.random()*6+1))
                }
            }
        }
    }

</script>

<template>
    <td>
        {{ thrown }}
    </td>
</template>