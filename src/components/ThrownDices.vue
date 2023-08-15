<script setup>
import {ref} from 'vue'

let props = defineProps(['thrown', 'frequency'])

function calcDice(){
    props.thrown.length = 0

    for(let i = 0; i < 5; i++){
        props.thrown.push(Math.floor(Math.random()*6) +1)
    }
}

function calcFreq(){
    props.frequency.length = 0

    for(let i = 1; i < 7; i++){

        let ln = props.thrown.filter(number => number == i).length

        props.frequency.push(ln)
    }
}

function throwDice(){
    calcDice()
    calcFreq()
}

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
    <button @click="throwDice()">Throw!</button>
</template>