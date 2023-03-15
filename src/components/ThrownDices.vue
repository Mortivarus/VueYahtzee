<script>

    export default{
        data(){
            return {
                thrown: [0,0,0,0,0],
                numFreq: []
            }
        },
        methods:{

            throwCount(){
                this.numFreq = []
                for(let i = 1; i < 7; i++){

                    let ln = this.thrown.filter(number => number == i).length

                    this.numFreq.push(ln)
                }
            },   


            throwDice(){
                this.thrown = []

                for(let i = 0; i < 5; i++){
                    this.thrown.push(Math.floor(Math.random()*6) +1)
                }

                return this.throwCount()
            }

            


        }
    }

</script>

<template>
    <h2>Thrown Dice</h2>
    <table>
        <tr>
            <td v-for="(item, index) in thrown" :key="index">
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
    <button v-on:click="throwDice()">herp</button>
</template>