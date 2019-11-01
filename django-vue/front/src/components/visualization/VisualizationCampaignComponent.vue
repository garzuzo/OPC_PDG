<template>
    <div>
        <v-container>
        <v-row>
            <!--MAP -->
            <v-col cols="4">
                <choropleth-map-component></choropleth-map-component>
            </v-col>

            <!--VISUALIZATION-->
            <v-col cols="8">
                <h3>En la campaña {{campaign}}, para ti la paz está asociada a los siguientes conceptos:</h3>
                <ve-wordcloud :data="wordData" :textStyle="textStyle"></ve-wordcloud>
                <h3>Escoge una de tus palabras: {{wordData.rows[0].word}}</h3>
            </v-col> 
        </v-row>

        
            <v-row justify="center">
                    <v-col cols="4">
                        <h3>Sexo</h3>
                          <ve-pie :data="pieData" :settings="pieSettings"></ve-pie>
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
      campaign: "Ríos de mi ciudad"
    };
  },
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
</style>