<script setup>
import {ref} from 'vue'

let props = defineProps(['thrown'])




function throwDice(){
    props.thrown = [0,0,0,0,0]

    // for(let i = 0; i < 5; i++){
    //     props.thrown.push(Math.floor(Math.random()*6) +1)
    // }

    console.log(props.thrown)
}



// const emit = defineEmits(['submitThrown'])
</script>

<template>
    <h2>Thrown Dice</h2>
    <table>
        <tr>
            <td v-for="(item, index) in props.thrown" :key="index">
                {{ item }}
            </td>
           
        </tr>
    </table>
    
    <h2>Number Frequencies</h2>
    <table>
        <tr>
            <td v-for="n in 6">
              <b>
                {{ n }}
              </b>  
            </td>
        </tr>
        <tr>
            <td v-for="(item, index) in numFreq" :key="index">
                {{ item }}
            </td>
        </tr>
    </table>
    <button @click="throwDice()">herp</button>
    <!-- <button @click="$emit('submitThrown')">derp</button> -->
</template>