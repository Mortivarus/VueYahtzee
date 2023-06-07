<script setup>
import ScoreTable from './components/ScoreTable.vue'
import ThrownDices from './components/ThrownDices.vue'
import {ref, reactive} from 'vue'


let thrownDice = ref([0,0,0,0,0])

const numFreq = ref([0,0,0,0,0,0])



const log = () => console.log(thrownDice.value)


</script>

<template>
  <h1>Scoreblok</h1>
  <ThrownDices :thrown="thrownDice" :frequency="numFreq" @submitThrown="log()" />
  

  
  <ScoreTable :freq="numFreq" :thrownDice="thrownDice"/>
</template>







<style>
  table{
    display: inline-table;
    border-collapse: collapse;
}

th, td, table{
    border: 1px solid #888;
    padding: 10px;
    font-family: sans-serif;
}

th{
    color: white;
    background-color: black;
    text-align: left;
}

.tmpLocked{
    background-color:grey;
}

.locked{
    background-color: firebrick;

}
</style>
