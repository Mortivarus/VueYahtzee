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
            },

            countConsequtives(array){
                array.sort()
                array = [...new Set(array)]
                let conseqCount = 0
                let size = []

                for(let i = 0; i< array.length-1; i++){
                    if(array[i]+1 === array[i+1]){
                        conseqCount += 1
                        console.log(`${array[i]+1}, ${array[i+1]}`)
                    } else{
                        size.push(conseqCount + 1)
                        conseqCount = 0
                        console.log(`${array[i]+1}, ${array[i+1]}`)
                    }
                }
                size.push(conseqCount + 1)
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