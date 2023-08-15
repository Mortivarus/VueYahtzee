<script setup>
// TODO :: imports die je niet gebruikt opruimen
import {ref, reactive, computed} from 'vue'

const props = defineProps(['freq', 'thrownDice'])

const countConsequtives = (array) => {
    array.sort()
    array = [...new Set(array)]
    let conseqCount = 0
    let size = []

    for(let i = 0; i< array.length-1; i++){
        if(array[i]+1 === array[i+1]){
            conseqCount += 1
            // console.log(`${array[i]+1}, ${array[i+1]}`)
        } else{
            size.push(conseqCount + 1)
            conseqCount = 0
            // console.log(`${array[i]+1}, ${array[i+1]}`)
        }
    }
    size.push(conseqCount + 1)

    return Math.max.apply(Math, size)

}

// TODO :: wordt niet meer gebruikt, kan dus weg
function sumValues(obj){
    Object.values(obj).reduce((a, b)=> a+b, 0)
}

const reducer = (accumulator, item) => {return accumulator + item}

// TODO :: alle "let" kunnen hier "const" zijn
let scoreOne = computed(()=> props.thrownDice.reduce(reducer, 0))

let bonus = computed(()=>{
    return scoreOne >=  63 ? 35 : 0  
})

//Three times the same dice
let threeOfAKind = computed(()=> {
    if (props.freq.includes(3)) {
        // TODO :: misschien een idee om een sumOfAllDice() iets te maken?
        return props.thrownDice.reduce(reducer, 0)
    } else{
        return 0
    }
}) 
//Four times the same dice
let carre = computed(()=> {
    if(props.freq.includes(4)){
        return props.thrownDice.reduce(reducer, 0)
    } else{
        return 0
    }
})

// Three and two of the same number
let fullHouse = computed(()=> {
    if(props.freq.includes(3) && props.freq.includes(2)){
        return 25
    } else{
        return 0
    }

}) 

//Four dice in numerical sequence

// TODO :: ik heb hem iets korter gemaakt voor je :)
let smallStreet = computed(()=> countConsequtives(props.thrownDice) == 4 ? 30 : 0) 

//Five dice in numerical sequence
let largeStreet = computed(()=> {
    let i = countConsequtives(props.thrownDice)
    return i == 5 ? 40 : 0
}) 

//Five times the same dice
let yahtzee = computed(()=> {
    if(props.freq.includes(5)){
        return 50
    } else{
        return 0
    }
}) 

//Any combination of dice
let chance = computed(()=> {
    return props.thrownDice.reduce(reducer, 0)
}) 

let scoreTwo = computed(()=> {
    return chance.value + largeStreet.value + threeOfAKind.value + carre.value + fullHouse.value + smallStreet.value + yahtzee.value
    // return 0+ threeOfAKind() + carre() + fullHouse() + smallStreet() + largeStreet() + yahtzee() + chance()
})


</script>

<template>
    <table>
        <tr>
            <th>Deel 1</th>
            <th>Puntentelling</th>
            <th>Punten</th>
        </tr>
        <tr>
            <td>Enen</td>
            <td>Tel alle enen op</td>
            <td class="dieTotal score one">{{ props.freq[0] * 1 }}</td>
        </tr>
        <tr>
            <td>Tweeen</td>
            <td>Tel alle tweeen op</td>
            <td class="dieTotal score one">{{ props.freq[1] * 2 }}</td>
        </tr>
        <tr>
            <td>Drieen</td>
            <td>Tel alle drieen op</td>
            <td class="dieTotal score one">{{ props.freq[2] * 3  }}</td>
        </tr>
        <tr>
            <td>Vieren</td>
            <td>Tel alle vieren op</td>
            <td class="dieTotal score one">{{ props.freq[3] * 4 }}</td>
        </tr>
        <tr>
            <td>Vijfen</td>
            <td>Tel alle vijven op</td>
            <td class="dieTotal score one">{{ props.freq[4] * 5 }}</td>
        </tr>
        <tr>
            <td>Zessen</td>
            <td>Tel alle zessen op</td>
            <td class="dieTotal score one">{{ props.freq[5] * 6 }}</td>
        </tr>
        <tr>
            <td colspan="2">Totaal aantal punten</td>
            <td id="totalPartOneBeforeBonus">{{ scoreOne }}</td>
        </tr>
        <tr>
            <td>Extra bonus <i>als puntentotaal 63 of meer is</i></td>
            <td>35 punten</td>
            <td id="bonus">{{ bonus }}</td>
        </tr>
        <tr>
            <td colspan="2">Totaal <i>van de bovenste helft</i></td>
            <td class="totalPartOne">{{scoreOne + bonus}}</td>
        </tr>
        <tr>
            <th colspan="3">Deel 2</th>
        </tr>
        <tr>
            <td>Three of a kind</td>
            <td>Totaal v.d. 5 stenen</td>
            <td id="threeOfAKind" class="score two">{{ threeOfAKind }}</td>
        </tr>
        <tr>
            <td>Carre</td>
            <td>Totaal v.d. 5 stenen</td>
            <td id="carre" class="score two">{{ carre }}</td>
        </tr>
        <tr>
            <td>Full house</td>
            <td>25 punten</td>
            <td id="fullHouse" class="score two">{{ fullHouse }}</td>
        </tr>
        <tr>
            <td>Kleine straat</td>
            <td>30 punten</td>
            <td id="smallStreet" class="score two">{{ smallStreet }}</td>
        </tr>
        <tr>
            <td>Grote straat</td>
            <td>40 punten</td>
            <td id="largeStreet" class="score two">{{ largeStreet }}</td>
        </tr>
        <tr>
            <td>Yahtzee</td>
            <td>50 punten</td>
            <td id="yahtzee" class="score two">{{ yahtzee }}</td>
        </tr>
        <tr>
            <td>Chance</td>
            <td>Totaal v.d. 5 stenen</td>
            <td id="chance" class="score two">{{ chance }}</td>
        </tr>
        <tr>
            <td colspan="2">Totaal <i>Deel 2</i></td>
            <td id="totalPartTwo">{{scoreTwo}}</td>
        </tr>
        <tr>
            <td colspan="2">Totaal <i>Deel 1</i></td>
            <td class="totalPartOne">{{scoreOne + bonus}}</td>
        </tr>
        <tr>
            <td colspan="2">Totaal</td>
            <td id="total">{{ scoreOne + scoreTwo + bonus }}</td>
        </tr>
    </table>
</template>