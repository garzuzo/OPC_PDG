<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12" sm="12" md="6">
            <choropleth-map-report-component :campaign="campaign"></choropleth-map-report-component>
        </v-col>

      <v-col cols="12" sm="12" md="6">
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

          <h3>Los conceptos de percepción de paz más relevantes identificados en esta campaña son:</h3>
          <v-row justify="center">
          <ve-wordcloud width="400px" height="350px" :data="wordData" :textStyle="textStyle" :settings="wordSettings"></ve-wordcloud>
          </v-row>
        </v-col>   
        <v-col cols="12">
          
        </v-col>
      </v-row>
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
    this.wordSettings={
        sizeMin: 14,
        sizeMax: 24
    }
    this.textStyle = { fontFamily: "Poppins" };

    return {
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
    const number = (this.campaign.accumulatedNarratives / this.campaign.narrativesGoal);
    this.percentage = Math.round(number * 1000) / 1000
  }
};
</script>


<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 24px;
}
span{
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 24px;
}

h3{
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  /*color: #0c186d;*/
}
</style>