<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="6">
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

        <v-col cols="6">
          <h3>Los conceptos de percepción de paz más relevantes identificados en esta campaña son:</h3>
          <ve-wordcloud :data="wordData" :textStyle="textStyle"></ve-wordcloud>
        </v-col>
      </v-row>

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
      /*var data = [campaign.id, i]*/
      /*api.getPeopleByCampaignAndComuna(data)*/
      object.mujeres = 50;
      object.hombres = 100;
      /*api.getRangesOfAgeByCampaignAndComuna(data)*/
      object.adolescencia = 150;
      object.juventud = 230;
      object.adultez = 320;
      object.vejez = 13;
      this.chartData.rows.push(object);
    }
    /*api.getNarratives(campaign.id);*/
    this.randomNumber =
      Math.floor(Math.random() * this.narratives.length) + 1 - 1;
    this.percentage =
      (campaign.accumulatedNarratives / campaign.narrativesGoal) * 100;
  }
};
</script>


<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");


</style>