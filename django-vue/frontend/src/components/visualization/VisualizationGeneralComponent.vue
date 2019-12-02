<template>
  <div>
    <navbar-component></navbar-component>
    <v-container>
      <v-row>
        <!--{{idCampaign}} - {{idUser}}-->
        <!--MAP -->
        <v-col cols="12" sm="12" md="6">
          <v-switch class="hidden-sm-and-down" v-model="switch1" label="Mapa de departamentos"></v-switch>
          <map-general-component class="hidden-sm-and-down" v-if="!switch1" :filter="filter"></map-general-component>
          <map-states-general-component v-if="switch1" :filter="filter"></map-states-general-component>
        </v-col>

        <!--VISUALIZATION-->
        <v-col cols="12" sm="12" md="6">
          <h3>La paz está asociada a los siguientes conceptos:</h3>

          <v-row justify="center">
            <v-col cols="12" sm="12" md="6">
              <ve-wordcloud
                :data="topicOneData"
                :tooltip-visible="tooltip"
                :textStyle="textStyle"
                :settings="wordSettings"
                :events="topicOneEvents"
                width="400px"
                height="350px"
              ></ve-wordcloud>
            </v-col>
            <v-col cols="12" sm="12" md="6">
              <ve-wordcloud
                :data="topicTwoData"
                :tooltip-visible="tooltip"
                :textStyle="textStyle"
                :settings="wordSettings"
                :events="topicTwoEvents"
                width="400px"
                height="350px"
              ></ve-wordcloud>
            </v-col>
            <v-col cols="12" sm="12" md="6">
              <ve-wordcloud
                :data="topicThreeData"
                :tooltip-visible="tooltip"
                :textStyle="textStyle"
                :settings="wordSettings"
                :events="topicThreeEvents"
                width="400px"
                height="350px"
              ></ve-wordcloud>
            </v-col>
            <v-col cols="12" sm="12" md="6">
              <ve-wordcloud
                :data="topicFourData"
                :tooltip-visible="tooltip"
                :textStyle="textStyle"
                :settings="wordSettings"
                :events="topicFourEvents"
                width="400px"
                height="350px"
              ></ve-wordcloud>
            </v-col>
            <v-col cols="12" sm="12" md="6">
              <ve-wordcloud
                :data="topicFiveData"
                :tooltip-visible="tooltip"
                :textStyle="textStyle"
                :settings="wordSettings"
                :events="topicFiveEvents"
                width="400px"
                height="350px"
              ></ve-wordcloud>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <h3>Selecciona opciones para filtrar en el mapa</h3>
      <v-row justify="start">
        <v-col cols="12" sm="12" md="10">
          <v-radio-group row>
            <v-radio label="Topico 1" v-model="radioOne" value="1" @change="radioOneEvent($event)"></v-radio>
            <v-radio label="Topico 2" v-model="radioTwo" value="2" @change="radioTwoEvent($event)"></v-radio>
            <v-radio
              label="Topico 3"
              v-model="radioThree"
              value="3"
              @change="radioThreeEvent($event)"
            ></v-radio>
            <v-radio
              label="Topico 4"
              v-model="radioFour"
              value="4"
              @change="radioFourEvent($event)"
            ></v-radio>
            <v-radio
              label="Topico 5"
              v-model="radioFive"
              value="5"
              @change="radioFiveEvent($event)"
            ></v-radio>
          </v-radio-group>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="12" sm="12" md="4">
          <h3>Sexo</h3>
          <ve-pie id="pie" :data="pieData" :settings="pieSettings" :events="sexEvents"></ve-pie>
        </v-col>

        <v-col cols="12" sm="12" md="4">
          <h3>Edad</h3>
          <ve-pie :data="ageData" :settings="ageSettings" :events="ageEvents"></ve-pie>
        </v-col>

        <v-col cols="12" sm="12" md="4">
          <h3>Educación</h3>
          <ve-pie :data="educationData" :settings="educationSettings" :events="educationEvents"></ve-pie>
        </v-col>        
      </v-row>

      <h3> Filtros aplicados: </h3>
      <v-row justify="center">
        <v-col cols="12" sm="12" md="4">
          <p>{{sex.toUpperCase()}}</p>
        </v-col>

        <v-col cols="12" sm="12" md="4">
          <p>{{age.toUpperCase()}}</p>
        </v-col>

        <v-col cols="12" sm="12" md="4">
          <p>{{education.toUpperCase()}}</p>
        </v-col>
      </v-row>

      <v-row justify="start">
        <v-col cols="10" sm="10" md="4">
          <h3>Tiempo</h3>
          <form class="form-inline">
          <div class="form-group div-filter">
            <label for="filter" class="filter mr-2 mb-5">Año:</label>
            <v-select
              :items="years"
              outlined
              v-model="year"
              required
              class="input"
              color="#0C186D"
              name="filter"
            ></v-select>
          </div>
          </form>
        </v-col>
        <v-col cols="12" sm="12" md="10">
          <v-range-slider class="hidden-sm-and-down"
            :value="[0, 1]"
            v-model="month"
            :tick-labels="months"
            tick-size="4"
            min="0"
            max="11"
            ticks="always"
            track-color="blue"
            track-fill-color="blue"
          ></v-range-slider>
          <v-range-slider class="hidden-md-and-up"
            :value="[0, 1]"
            v-model="month"
            :tick-labels="months"
            v-bind:vertical="true"
            tick-size="4"
            min="0"
            max="11"
            v-bind:ticks="true"
            track-color="blue"
            track-fill-color="blue"
          ></v-range-slider>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import echarts from "echarts";
import api from "../../axios";

export default {
  data() {
    this.pieSettings = {
      dimension: "gender",
      metrics: "frequency"
    };
    this.ageSettings = {
      dimension: "range",
      metrics: "frequency"
    };
    this.educationSettings = {
      dimension: "education",
      metrics: "frequency"
    };
    this.wordSettings = {
      sizeMin: 14,
      sizeMax: 30
    };
    this.textStyle = { fontFamily: "Poppins" };
    var self = this;
    this.topicOneEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicOne();
      }
    };
    this.topicTwoEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicTwo();
      }
    };
    this.topicThreeEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicThree();
      }
    };
    this.topicFourEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicFour();
      }
    };
    this.topicFiveEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicFive();
      }
    };
    this.ageEvents = {
      click: function(e) {
        //self.age = e.name;
        self.filterAge(e.name);
      }
    };
    this.sexEvents = {
      click: function(e) {
        //self.sex = e.name;
        self.filterSex(e.name);
      }
    };
    this.educationEvents = {
      click: function(e) {
        //self.education = e.name;
        self.filterEducation(e.name);
      }
    };
    return {
      tooltip: false,
      months: [
        "En",
        "Febr",
        "Mzo",
        "Abr",
        "My",
        "Jun",
        "Jul",
        "Agt",
        "Sept",
        "Oct",
        "Nov",
        "Dic"
      ],
      month: [0, 1],
      years: [2019, 2020, 2021, 2022],
      year: 2019,
      switch1: false,
      ageData: {
        columns: ["range", "frequency"],
        rows: [
          { range: "0-5", frequency: 60 },
          { range: "6-11", frequency: 80 }
        ]
      },
      pieData: {
        columns: ["gender", "frequency"],
        rows: [
          { gender: "mujeres", frequency: 60 },
          { gender: "hombres", frequency: 20 }
        ]
      },
      educationData: {
        columns: ["education", "frequency"],
        rows: [
          { education: "primaria", frequency: 60 },
          { education: "secundaria", frequency: 20 }
        ]
      },
      topicOneData: {
        columns: ["word", "count"],
        rows: []
      },
      topicTwoData: {
        columns: ["word", "count"],
        rows: []
      },
      topicThreeData: {
        columns: ["word", "count"],
        rows: []
      },
      topicFourData: {
        columns: ["word", "count"],
        rows: []
      },
      topicFiveData: {
        columns: ["word", "count"],
        rows: []
      },
      narratives: [
        "Para mi la paz es sentir que el río está limpio",
        "Para mi la paz es que la gente no tire basuras al río"
      ],
      sex: "",
      age: "",
      education: "",
      topicOne: 0,
      topicTwo: 0,
      topicThree: 0,
      topicFour: 0,
      topicFive: 0,
      radioOne: "",
      radioTwo: "",
      radioThree: "",
      radioFour: "",
      radioFive: "",
      filter: {
        topicGeneral: 0,
        sex: "",
        age: "",
        education: "",
        minDate: "",
        maxDate: ""
      }
    };
  },
  created() {
    api
      .getAllTopics()
      .then(response => {
        this.topicOne = response[0].id;
        this.topicTwo = response[1].id;
        this.topicThree = response[2].id;
        this.topicFour = response[3].id;
        this.topicFive = response[4].id;

        let array = response[0].concepts.split(", ");
        let array2 = response[1].concepts.split(", ");
        let array3 = response[2].concepts.split(", ");
        let array4 = response[3].concepts.split(", ");
        let array5 = response[4].concepts.split(", ");

        for (var i = 0; i < array.length; i++) {
          var actOne = { word: array[i], count: 2 };
          this.topicOneData.rows.push(actOne);
          var actTwo = { word: array2[i], count: 2 };
          this.topicTwoData.rows.push(actTwo);
          var actThree = { word: array3[i], count: 2 };
          this.topicThreeData.rows.push(actThree);
          var actFour = { word: array4[i], count: 2 };
          this.topicFourData.rows.push(actFour);
          var actFive = { word: array5[i], count: 2 };
          this.topicFiveData.rows.push(actFive);
        }
      })
      .catch(err => console.log(err));

    this.init();
  },
  watch: {
    month: {
      deep: true,
      handler(range) {
        this.filter.minDate = this.calculateDate(this.year, range[0], "min");
        this.filter.maxDate = this.calculateDate(this.year, range[1], "max");
      }
    }
  },
  methods: {
    calculateDate(year, month, typeDate) {
      if (typeDate == "min") {
        return year + "-" + (month + 1) + "-" + "01";
      } else {
        var day = new Date(year, month + 1, 0).getDate();
        return year + "-" + (month + 1) + "-" + day;
      }
    },
    init() {
      let data = { id: this.idCampaign };
      api
        .getAllPeople()
        .then(response => {
          this.pieData.rows.length = 0;
          this.pieData.rows.push({
            gender: "Femenino",
            frequency: response.women
          });
          this.pieData.rows.push({
            gender: "Masculino",
            frequency: response.men
          });
          this.pieData.rows.push({
            gender: "Intersexual",
            frequency: response.intersexual
          });
        })
        .catch(err => console.log(err));

      api
        .getAllRangesOfAge()
        .then(response => {
          this.ageData.rows.length = 0;
          this.ageData.rows.push({
            range: "Primera infancia",
            frequency: response.primeraInfancia
          });
          this.ageData.rows.push({
            range: "Infancia",
            frequency: response.infancia
          });
          this.ageData.rows.push({
            range: "Adolescencia",
            frequency: response.adolescencia
          });
          this.ageData.rows.push({
            range: "Juventud",
            frequency: response.juventud
          });
          this.ageData.rows.push({
            range: "Adultez",
            frequency: response.adultez
          });
          this.ageData.rows.push({ range: "Vejez", frequency: response.vejez });
        })
        .catch(err => console.log(err));

      api
        .getAllEducation()
        .then(response => {
          this.educationData.rows.length = 0;
          this.educationData.rows.push({
            education: "Primaria",
            frequency: response.primaria
          });
          this.educationData.rows.push({
            education: "Secundaria",
            frequency: response.secundaria
          });
          this.educationData.rows.push({
            education: "Técnica y Tecnológica",
            frequency: response.tyt
          });
          this.educationData.rows.push({
            education: "Universitaria",
            frequency: response.universitaria
          });
          this.educationData.rows.push({
            education: "Postgrado",
            frequency: response.postgrado
          });
        })
        .catch(err => console.log(err));
    },
    filterTopicOne() {
      let data = { id: this.topicOne, type: "General" };
      this.filter.topicGeneral = this.topicOne;
      this.filterTopic(data);
    },
    filterTopicTwo() {
      let data = { id: this.topicTwo, type: "General" };
      this.filter.topicGeneral = this.topicTwo;
      this.filterTopic(data);
    },
    filterTopicThree() {
      let data = { id: this.topicThree, type: "General" };
      this.filter.topicGeneral = this.topicThree;
      this.filterTopic(data);
    },
    filterTopicFour() {
      let data = { id: this.topicFour, type: "General" };
      this.filter.topicGeneral = this.topicFour;
      this.filterTopic(data);
    },
    filterTopicFive() {
      let data = { id: this.topicFive, type: "General" };
      this.filter.topicGeneral = this.topicFive;
      this.filterTopic(data);
    },
    filterTopic(data) {
      api
        .getPeopleByTopic(data)
        .then(response => {
          this.pieData.rows.length = 0;
          this.pieData.rows.push({
            gender: "Femenino",
            frequency: response.women
          });
          this.pieData.rows.push({
            gender: "Masculino",
            frequency: response.men
          });
          this.pieData.rows.push({
            gender: "Intersexual",
            frequency: response.intersexual
          });
        })
        .catch(err => console.log(err));

      api
        .getRangesOfAgeByTopic(data)
        .then(response => {
          this.ageData.rows.length = 0;
          this.ageData.rows.push({
            range: "Primera infancia",
            frequency: response.primeraInfancia
          });
          this.ageData.rows.push({
            range: "Infancia",
            frequency: response.infancia
          });
          this.ageData.rows.push({
            range: "Adolescencia",
            frequency: response.adolescencia
          });
          this.ageData.rows.push({
            range: "Juventud",
            frequency: response.juventud
          });
          this.ageData.rows.push({
            range: "Adultez",
            frequency: response.adultez
          });
          this.ageData.rows.push({ range: "Vejez", frequency: response.vejez });
        })
        .catch(err => console.log(err));

      api
        .getEducationByTopic(data)
        .then(response => {
          this.educationData.rows.length = 0;
          this.educationData.rows.push({
            education: "Primaria",
            frequency: response.primaria
          });
          this.educationData.rows.push({
            education: "Secundaria",
            frequency: response.secundaria
          });
          this.educationData.rows.push({
            education: "Técnica y Tecnológica",
            frequency: response.tyt
          });
          this.educationData.rows.push({
            education: "Universitaria",
            frequency: response.universitaria
          });
          this.educationData.rows.push({
            education: "Postgrado",
            frequency: response.postgrado
          });
        })
        .catch(err => console.log(err));
    },
    filterSex(name) {
      if (this.sex == name) {
        this.sex = "";
      } else {
        this.sex = name;
      }
      this.filter.sex = this.sex;
    },
    filterEducation(name) {
      if (this.education == name) {
        this.education = "";
      } else {
        this.education = name;
      }
      this.filter.education = this.education;
    },
    filterAge(name) {
      if (this.age == name) {
        this.age = "";
      } else {
        this.age = name;
      }
      this.filter.age = this.age;
    },
    radioOneEvent(event) {
      this.filter.topicGeneral = this.topicOne;
    },
    radioTwoEvent(event) {
      this.filter.topicGeneral = this.topicTwo;
    },
    radioThreeEvent(event) {
      this.filter.topicGeneral = this.topicThree;
    },
    radioFourEvent(event) {
      this.filter.topicGeneral = this.topicFour;
    },
    radioFiveEvent(event) {
      this.filter.topicGeneral = this.topicFive;
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
  color: #0c186d;
}

p{
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: calc(16px + (18 - 16) * ((100vw - 300px) / (1600 - 300)));
}
</style>