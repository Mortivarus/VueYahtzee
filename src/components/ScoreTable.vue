<script setup>
import {ref, reactive} from 'vue'

let scorePartOne = reactive({
    numOne: 10,
    numTwo: 5,
    numThree: 2,
    numFour: 8,
    numFive: 10,
    numSix: 18
})

function sumValues(obj){
    Object.values(obj).reduce((a, b)=> a+b, 0)
}

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
            <td class="dieTotal score one">{{ scorePartOne.numOne }}</td>
        </tr>
        <tr>
            <td>Tweeen</td>
            <td>Tel alle tweeen op</td>
            <td class="dieTotal score one">{{ scorePartOne.numTwo }}</td>
        </tr>
        <tr>
            <td>Drieen</td>
            <td>Tel alle drieen op</td>
            <td class="dieTotal score one">{{ scorePartOne.numThree }}</td>
        </tr>
        <tr>
            <td>Vieren</td>
            <td>Tel alle vieren op</td>
            <td class="dieTotal score one">{{ scorePartOne.numFour }}</td>
        </tr>
        <tr>
            <td>Vijfen</td>
            <td>Tel alle vijven op</td>
            <td class="dieTotal score one">{{ scorePartOne.numFive }}</td>
        </tr>
        <tr>
            <td>Zessen</td>
            <td>Tel alle zessen op</td>
            <td class="dieTotal score one">{{ scorePartOne.numSix }}</td>
        </tr>
        <tr>
            <td colspan="2">Totaal aantal punten</td>
            <td id="totalPartOneBeforeBonus">0</td>
        </tr>
        <tr>
            <td>Extra bonus <i>als puntentotaal 63 of meer is</i></td>
            <td>35 punten</td>
            <td id="bonus">0</td>
        </tr>
        <tr>
            <td colspan="2">Totaal <i>van de bovenste helft</i></td>
            <td class="totalPartOne">0</td>
        </tr>
        <tr>
            <th colspan="3">Deel 2</th>
        </tr>
        <tr>
            <td>Three of a kind</td>
            <td>Totaal v.d. 5 stenen</td>
            <td id="threeOfAKind" class="score two">0</td>
        </tr>
        <tr>
            <td>Carre</td>
            <td>Totaal v.d. 5 stenen</td>
            <td id="carre" class="score two">0</td>
        </tr>
        <tr>
            <td>Full house</td>
            <td>25 punten</td>
            <td id="fullHouse" class="score two">0</td>
        </tr>
        <tr>
            <td>Kleine straat</td>
            <td>30 punten</td>
            <td id="smallStreet" class="score two">0</td>
        </tr>
        <tr>
            <td>Grote straat</td>
            <td>40 punten</td>
            <td id="largeStreet" class="score two">0</td>
        </tr>
        <tr>
            <td>Yahtzee</td>
            <td>50 punten</td>
            <td id="yahtzee" class="score two">0</td>
        </tr>
        <tr>
            <td>Chance</td>
            <td>Totaal v.d. 5 stenen</td>
            <td id="chance" class="score two">0</td>
        </tr>
        <tr>
            <td colspan="2">Totaal <i>Deel 2</i></td>
            <td id="totalPartTwo">0</td>
        </tr>
        <tr>
            <td colspan="2">Totaal <i>Deel 1</i></td>
            <td class="totalPartOne">0</td>
        </tr>
        <tr>
            <td colspan="2">Totaal</td>
            <td id="total">0</td>
        </tr>
    </table>
</template>