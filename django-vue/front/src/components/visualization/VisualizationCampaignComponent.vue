<template>
    <div>
        <v-container>
        <v-row>
            <!--MAP -->
            <v-col cols="6">
                <choropleth-map-component></choropleth-map-component>
            </v-col>

            <!--VISUALIZATION-->
            <v-col cols="6">
                <h3>En la campaña {{campaign}}, para ti la paz está asociada a los siguientes conceptos:</h3>
                <ve-wordcloud :data="wordData" :textStyle="textStyle" :events="chartEvents"></ve-wordcloud>
                <h3>Escoge una de tus palabras:  {{name.toUpperCase()}}</h3>
            </v-col> 
        </v-row>

        
            <v-row justify="center">
                    <v-col cols="4">
                        <h3>Sexo</h3>
                          <ve-pie id="pie" :data="pieData" :settings="pieSettings"></ve-pie>
                    </v-col>

                    <v-col cols="4">
                        <h3>Edad</h3>
                        <ve-bar :data="ageData"></ve-bar>
                    </v-col>

                    <v-col cols="4">
                        <h3>Educación</h3>
                        <ve-bar :data="educationData"></ve-bar>
                    </v-col> 
                </v-row>
        
        </v-container>
    </div>
</template>

<script>
import echarts from 'echarts'

export default {
    data() {
    this.pieSettings = {
        dimension: 'gender',
        metrics: 'frequency'
      };
    
    this.dataZoom = [
      {
        type: "slider",
        start: 0,
        end: 23
      }
    ];
    this.textStyle = { fontFamily: "Poppins" };
    this.timeline= {
        data: ['2017-01-01', '2018-01-01', '2019-01-01']
    };
    var self = this
    this.chartEvents = {
        click: function (e) {
          self.name = e.name
          self.changeData(self.name)
          console.log(e)
        }
      }
    return {
      ageData: {
        columns: ['range','frequency'],
        rows: [
            { 'range': '0-5', 'frequency': 60 },
            { 'range': '6-11', 'frequency': 80 }
        ]
      },
      pieData: {
          columns: ['gender', 'frequency'],
          rows: [
            { 'gender': 'mujeres', 'frequency': 60 },
            { 'gender': 'hombres', 'frequency': 20 },
          ]
        },
         educationData: {
          columns: ['education', 'frequency'],
          rows: [
            { 'education': 'primaria', 'frequency': 60 },
            { 'education': 'secundaria', 'frequency': 20 },
          ]
        },
      wordData: {
        columns: ["word", "count"],
        rows: [
          { word: "tranquilidad", count: 2199 },
          { word: "familia", count: 1288 },
          { word: "amor", count: 14000 },
          { word: "cultura", count: 10000 },
          { word: "paz", count: 10388 }
        ]
      },
      narratives: [
        "Para mi la paz es sentir que el río está limpio",
        "Para mi la paz es que la gente no tire basuras al río"
      ],
      randomNumber: 0,
      percentage: 0.0,
      campaign: "Ríos de mi ciudad",
      name
    };
  },
  methods:{
    changeData(word){
      if(word == "tranquilidad"){
        this.ageData.rows.length = 0
        this.ageData.rows.push({ 'range': '12-17', 'frequency': 70 })
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'mujeres', 'frequency': 60 })
        this.pieData.rows.push({ 'gender': 'hombres', 'frequency': 80 })
        this.educationData.rows.length = 0
        this.educationData.rows.push({ 'education': 'primaria', 'frequency': 15 })
        this.educationData.rows.push({ 'education': 'secundaria', 'frequency': 20 })
      }
      if(word == "familia"){
        this.ageData.rows.length = 0         
        this.ageData.rows.push({ 'range': '0-5', 'frequency': 60 })    
        this.ageData.rows.push({ 'range': '6-11', 'frequency': 80 })
        this.ageData.rows.push({ 'range': '12-17', 'frequency': 70 })
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'mujeres', 'frequency': 70 })
        this.pieData.rows.push({ 'gender': 'hombres', 'frequency': 20 })
        this.educationData.rows.length = 0
        this.educationData.rows.push({ 'education': 'primaria', 'frequency': 50 })
        this.educationData.rows.push({ 'education': 'secundaria', 'frequency': 20 })
      }
      if( word == "amor"){
        this.ageData.rows.length = 0         
        this.ageData.rows.push({ 'range': '0-5', 'frequency': 60 })    
        this.ageData.rows.push({ 'range': '6-11', 'frequency': 80 })
        this.ageData.rows.push({ 'range': '12-17', 'frequency': 70 })
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'mujeres', 'frequency': 70 })
        this.pieData.rows.push({ 'gender': 'hombres', 'frequency': 20 })
        this.educationData.rows.length = 0
        this.educationData.rows.push({ 'education': 'primaria', 'frequency': 50 })
        this.educationData.rows.push({ 'education': 'secundaria', 'frequency': 20 })
      }
      if( word == "cultura"){
        this.ageData.rows.length = 0         
        this.ageData.rows.push({ 'range': '0-5', 'frequency': 20 })    
        this.ageData.rows.push({ 'range': '6-11', 'frequency': 12 })
        this.ageData.rows.push({ 'range': '12-17', 'frequency': 70 })
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'mujeres', 'frequency': 50 })
        this.pieData.rows.push({ 'gender': 'hombres', 'frequency': 70 })
        this.educationData.rows.length = 0
        this.educationData.rows.push({ 'education': 'primaria', 'frequency': 30 })
        this.educationData.rows.push({ 'education': 'secundaria', 'frequency': 20 })
      }
      if( word == "paz"){
        this.ageData.rows.length = 0         
        this.ageData.rows.push({ 'range': '0-5', 'frequency': 70 })    
        this.ageData.rows.push({ 'range': '6-11', 'frequency': 80 })
        this.ageData.rows.push({ 'range': '12-17', 'frequency': 60 })
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'mujeres', 'frequency': 80 })
        this.pieData.rows.push({ 'gender': 'hombres', 'frequency': 80 })
        this.educationData.rows.length = 0
        this.educationData.rows.push({ 'education': 'primaria', 'frequency': 10 })
        this.educationData.rows.push({ 'education': 'secundaria', 'frequency': 80 })
      }
    }
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  color: #0c186d;
}
</style>