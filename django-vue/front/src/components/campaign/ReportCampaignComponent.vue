<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="7">
            <choropleth-map-report-component :campaign="campaign"></choropleth-map-report-component>
        </v-col>

      <v-col cols="5">
        <v-row>
        <v-col cols="12">
          <p>
            <span>Descripción:</span>
            {{campaign.description}}
          </p>
          <p>
            <span>Fecha de inicio:</span>
            {{campaign.startDate}}
          </p>
          <p>
            <span>Fecha de finalización:</span>
            {{campaign.endDate}}
          </p>
          <p>
            <span>Cantidad de narrativas:</span>
            {{campaign.accumulatedNarratives}}
          </p>
          <p>
            <span>Meta de narrativas:</span>
            {{campaign.narrativesGoal}}
          </p>
          <p>
            <span>Porcentaje de cumplimiento de narrativas:</span>
            {{percentage}}%
          </p>
          <p>
            <span>Los participantes de esta campaña dicen:</span>
            "{{narratives[randomNumber]}}"
          </p>
        </v-col>
        <v-divider> </v-divider>       
        <v-col cols="12">
          <h3>Los conceptos de percepción de paz más relevantes identificados en esta campaña son:</h3>
          <ve-wordcloud :data="wordData" :textStyle="textStyle"></ve-wordcloud>
        </v-col>
      </v-row>
      </v-col>
      </v-row>
      <v-divider> </v-divider>
      <!-- <ve-wordcloud :data="wordData" :textStyle="textStyle"></ve-wordcloud> -->

      <v-row>
        <v-col cols="12">
          <ve-histogram
            :data="chartData"
            :settings="chartSettings"
            :data-zoom="dataZoom"
            :textStyle="textStyle"
          ></ve-histogram>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import api from "../../axios.js";

export default {
  props: {
    campaign: Object
  },
  data() {
    this.chartSettings = {
      metrics: [
        "mujeres",
        "hombres",
        "adolescencia",
        "juventud",
        "adultez",
        "vejez"
      ],
      dimension: ["comuna"]
    };
    this.dataZoom = [
      {
        type: "slider",
        start: 0,
        end: 23
      }
    ];
    this.textStyle = { fontFamily: "Poppins" };

    return {
      chartData: {
        columns: [
          "comuna",
          "mujeres",
          "hombres",
          "adolescencia",
          "juventud",
          "adultez",
          "vejez"
        ],
        rows: []
      },
      wordData: {
        columns: ["word", "count"],
        rows: []
      },
      narratives: [],
      randomNumber: 0,
      percentage: 0.0
    };
  },
  created() {
    for (var i = 1; i < 23; i++) {
      var object = {
        comuna: "Comuna " + i,
        mujeres: 0,
        hombres: 0,
        adolescencia: 0,
        juventud: 0,
        adultez: 0,
        vejez: 0
      };
      object.mujeres = 80;
      object.hombres = 100;
      object.adolescencia = 50;
      object.juventud = 20;
      object.adultez = 10;
      object.vejez = 30;
      var data = [this.campaign.id, object.comuna]
      api.getPeopleByCampaignAndComuna(data).then(response => {
        object.mujeres = response.women;
        object.hombres = response.men;
      }).catch(err => console.log(err))

      api.getRangesOfAgeByCampaignAndComuna(data).then(response => {
        object.adolescencia = response.adolescencia;
        object.juventud = response.juventud;
        object.adultez = response.adultez;
        object.vejez = response.vejez;
      })
      this.chartData.rows.push(object);
    }
    //console.log(campaign.id)
    api.getKeywords(this.campaign.id).then(response => {
        for(var i=0; i< response.length; i++){
          var act = { word: response[i].name, count: response[i].frequency }
          this.wordData.rows.push(act)
        }        
      }).catch(err=> console.log(err))

    api.getNarratives(this.campaign.id).then(response => {
      for(var i= 0; i< response.length; i++){
        var act = response[i].text
         this.narratives.push(act)
      }     
    }).catch(err => console.log(err));
    this.randomNumber =
      Math.floor(Math.random() * this.narratives.length) + 1 - 1;
    const number = (this.campaign.accumulatedNarratives / this.campaign.narrativesGoal) * 100;
    this.percentage = Math.round(number * 100) / 100
  }
};
</script>


<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 36px;
}
span{
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 36px;
}

h3{
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  color: #0c186d;
}
</style>