<script>
import ScoreTable from './components/ScoreTable.vue'
import ThrownDices from './components/ThrownDices.vue'

export default {
    components:{
        ScoreTable,
        ThrownDices
    }
}
</script>

<template>
  <h1>Scoreblok</h1>
    <ScoreTable />

    <table>
        <tr>
            <ThrownDices />
        </tr>
    </table>
    <input type="button" value="Gooien!" id="throwButton">
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
