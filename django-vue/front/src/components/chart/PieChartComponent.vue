<template>
<div>
    <v-row>

        <v-col cols=4>

            <ve-pie :data="chartData"></ve-pie>
        </v-col>
  <v-col cols=8>
 <ve-bar :data="chartData1" :settings="chartSettings"></ve-bar>
        </v-col>
    </v-row>
  
  </div>
</template>

<script>

//charts
import VePie from 'v-charts/lib/pie.common'
import VeBar from 'v-charts/lib/bar.common'

  export default {
      components: { VePie, VeBar },
    data () {
        this.chartSettings =  {
        legendName: {
          'cost': 'costmoney'
        }
      }
      return {
        chartData: {
          columns: ['date', 'cost', 'profit'],
          rows: [
            { 'date': '01/01', 'cost': 123, 'profit': 3 },
            { 'date': '01/02', 'cost': 1223, 'profit': 6 },
            { 'date': '01/03', 'cost': 2123, 'profit': 90 },
            { 'date': '01/04', 'cost': 4123, 'profit': 12 },
            { 'date': '01/05', 'cost': 3123, 'profit': 15 },
            { 'date': '01/06', 'cost': 7123, 'profit': 20 }
          ]
        },
        chartData1: {
          columns: ['date', 'cost', 'profit'],
          rows: [
            { 'date': '01/01', 'cost': 123, 'profit': 300 },
            { 'date': '01/02', 'cost': 1223, 'profit': 600 },
            { 'date': '01/03', 'cost': 2123, 'profit': 9000 },
            { 'date': '01/04', 'cost': 4123, 'profit': 1200 },
            { 'date': '01/05', 'cost': 3123, 'profit': 1500 },
            { 'date': '01/06', 'cost': 7123, 'profit': 2000 }
          ]
        }
      }
    }
  }
</script>