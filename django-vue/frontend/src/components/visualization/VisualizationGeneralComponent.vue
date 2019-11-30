<template>
  <div>
    <navbar-component></navbar-component>
    <v-container>
      <v-row>
        <!--{{idCampaign}} - {{idUser}}-->
        <!--MAP -->
        <v-col cols="12" sm="12" md="6">
            <map-general-component :filter="filter"></map-general-component>
        </v-col>

        <!--VISUALIZATION-->
        <v-col cols="12" sm="12" md="6">
          <h3>La paz está asociada a los siguientes conceptos:</h3>

          <v-row justify="center">
              <v-col cols="6" sm="6" md="6">
                  <ve-wordcloud
            :data="topicOneData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicOneEvents"
            width="400px" height="350px"
          ></ve-wordcloud>
              </v-col>
              <v-col cols="6" sm="6" md="6">
                  <ve-wordcloud
            :data="topicTwoData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicTwoEvents"
            width="400px" height="350px"
          ></ve-wordcloud>
              </v-col>
              <v-col cols="6" sm="6" md="6">
                  <ve-wordcloud
            :data="topicThreeData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicThreeEvents"
            width="400px" height="350px"
          ></ve-wordcloud>
              </v-col>
              <v-col cols="6" sm="6" md="6">
                  <ve-wordcloud
            :data="topicFourData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicFourEvents"
            width="400px" height="350px"
          ></ve-wordcloud>
              </v-col>
              <v-col cols="6" sm="6" md="6">
                  <ve-wordcloud
            :data="topicFiveData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicFiveEvents"
            width="400px" height="350px"
          ></ve-wordcloud>
              </v-col>
          </v-row>
          
          
        </v-col>
      </v-row>
      <h3>Selecciona opciones para filtrar en el mapa</h3>
      <v-row justify="start">
        
        <v-col cols="2">
          <v-checkbox
            v-model="checkboxTopicOne"
            label="Topico 1"
            @change="checkTopicOne($event)"
          ></v-checkbox>
        </v-col>
        <v-col cols="2">
          <v-checkbox
            v-model="checkboxTopicTwo"
            label="Topico 2"
            @change="checkTopicTwo($event)"
          ></v-checkbox>
        </v-col>
        <v-col cols="2">
          <v-checkbox
            v-model="checkboxTopicThree"
            label="Topico 3"
            @change="checkTopicThree($event)"
          ></v-checkbox>
        </v-col>
        <v-col cols="2">
          <v-checkbox
            v-model="checkboxTopicFour"
            label="Topico 4"
            @change="checkTopicFour($event)"
          ></v-checkbox>
        </v-col>
        <v-col cols="2">
          <v-checkbox
            v-model="checkboxTopicFive"
            label="Topico 5"
            @change="checkTopicFive($event)"
          ></v-checkbox>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="4">
          <h3>Sexo</h3>
          <ve-pie id="pie" :data="pieData" :settings="pieSettings" :events="sexEvents"></ve-pie>
          {{sex.toUpperCase()}}
        </v-col>

        <v-col cols="4">
          <h3>Edad</h3>
          <ve-pie :data="ageData" :settings="ageSettings" :events="ageEvents"></ve-pie>
          {{age.toUpperCase()}}
          <!--<ve-bar :data="ageData"></ve-bar>-->
        </v-col>

        <v-col cols="4">
          <h3>Educación</h3>
          <ve-pie :data="educationData" :settings="educationSettings" :events="educationEvents"></ve-pie>
          {{education.toUpperCase()}}
          <!--<ve-bar :data="educationData"></ve-bar>-->
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
    this.wordSettings={
        sizeMin: 14,
        sizeMax: 30
    }
    this.dataZoom = [
      {
        type: "slider",
        start: 0,
        end: 23
      }
    ];
    this.textStyle = { fontFamily: "Poppins" };
    this.timeline = {
      data: ["2017-01-01", "2018-01-01", "2019-01-01"]
    };
    var self = this;
    this.topicOneEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicOne();
        console.log(e);
      }
    };
    this.topicTwoEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicTwo();
        console.log(e);
      }
    };
    this.topicThreeEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicThree();
        console.log(e);
      }
    };
    this.topicFourEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicFour();
        console.log(e);
      }
    };
    this.topicFiveEvents = {
      click: function(e) {
        //self.name = e.name;
        self.filterTopicFive();
        console.log(e);
      }
    };
    this.ageEvents = {
      click: function(e) {
        //self.age = e.name;
        self.filterAge(e.name);
        console.log(e);
      }
    };
    this.sexEvents = {
      click: function(e) {
        //self.sex = e.name;
        self.filterSex(e.name);
        console.log(e);
      }
    };
    this.educationEvents = {
      click: function(e) {
        //self.education = e.name;
        self.filterEducation(e.name);
        console.log(e);
      }
    };
    return {
      tooltip: false,
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
      sex:"",
      age:"",
      education:"",
      topicOne: 0,
      topicTwo: 0,
      topicThree: 0,
      topicFour: 0,
      topicFive: 0,
      checkboxTopicOne: false, 
      checkboxTopicTwo: false,
      checkboxTopicThree: false,
      checkboxTopicFour: false,
      checkboxTopicFive: false,
      filter:{
        topicGeneral:0,
        sex: '',
        age:'',
        education:''
      }
    };
  },
  created() {

    api.getAllTopics()
      .then(response => {
        this.topicOne = response[0].id;
        this.topicTwo = response[1].id;
        this.topicThree = response[2].id;
        this.topicFour = response[3].id;
        this.topicFive = response[4].id;

        let array= response[0].concepts.split(', ')
        let array2= response[1].concepts.split(', ')
        let array3= response[2].concepts.split(', ')
        let array4= response[3].concepts.split(', ')
        let array5= response[4].concepts.split(', ')

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

     this.init() 
  },
  methods: {
    init(){
      let data= {id:this.idCampaign}
      api.getAllPeople()
      .then(response => {
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'Femenino', 'frequency': response.women })
        this.pieData.rows.push({ 'gender': 'Masculino', 'frequency': response.men })
        this.pieData.rows.push({ 'gender': 'Intersexual', 'frequency': response.intersexual })
      })
      .catch(err => console.log(err));   

    api.getAllRangesOfAge().then(response => {
      this.ageData.rows.length = 0
      this.ageData.rows.push({ 'range': 'Primera infancia', 'frequency': response.primeraInfancia })
      this.ageData.rows.push({ 'range': 'Infancia', 'frequency': response.infancia })
      this.ageData.rows.push({ 'range': 'Adolescencia', 'frequency': response.adolescencia })
      this.ageData.rows.push({ 'range': 'Juventud', 'frequency': response.juventud })
      this.ageData.rows.push({ 'range': 'Adultez', 'frequency': response.adultez })
      this.ageData.rows.push({ 'range': 'Vejez', 'frequency': response.vejez })
    }).catch(err => console.log(err));
    
    api.getAllEducation().then(response => {
      this.educationData.rows.length = 0
      this.educationData.rows.push({ 'education': 'Primaria', 'frequency': response.primaria })
      this.educationData.rows.push({ 'education': 'Secundaria', 'frequency': response.secundaria })
      this.educationData.rows.push({ 'education': 'Técnica y Tecnológica', 'frequency': response.tyt })
      this.educationData.rows.push({ 'education': 'Universitaria', 'frequency': response.universitaria })
      this.educationData.rows.push({ 'education': 'Postgrado', 'frequency': response.postgrado })
    }).catch(err => console.log(err));
    },
    filterTopicOne(){
      let data= {id:this.topicOne, type:'General'}
      this.filter.topicGeneral = this.topicOne
      this.filterTopic(data)
    },
    filterTopicTwo(){
      let data= {id:this.topicTwo, type:'General'}
      this.filter.topicGeneral = this.topicTwo
      this.filterTopic(data)
    },
    filterTopicThree(){
      let data= {id:this.topicThree, type:'General'}
      this.filter.topicGeneral = this.topicThree
      this.filterTopic(data)
    },
    filterTopicFour(){
      let data= {id:this.topicFour, type:'General'}
      this.filter.topicGeneral = this.topicFour
      this.filterTopic(data)
    },
    filterTopicFive(){
      let data= {id:this.topicFive, type:'General'}
      this.filter.topicGeneral = this.topicFive
      this.filterTopic(data)
    },
    filterTopic(data){
        api.getPeopleByTopic(data)
      .then(response => {
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'Femenino', 'frequency': response.women })
        this.pieData.rows.push({ 'gender': 'Masculino', 'frequency': response.men })
        this.pieData.rows.push({ 'gender': 'Intersexual', 'frequency': response.intersexual })
      })
      .catch(err => console.log(err));   

    api.getRangesOfAgeByTopic(data).then(response => {
      this.ageData.rows.length = 0
      this.ageData.rows.push({ 'range': 'Primera infancia', 'frequency': response.primeraInfancia })
      this.ageData.rows.push({ 'range': 'Infancia', 'frequency': response.infancia })
      this.ageData.rows.push({ 'range': 'Adolescencia', 'frequency': response.adolescencia })
      this.ageData.rows.push({ 'range': 'Juventud', 'frequency': response.juventud })
      this.ageData.rows.push({ 'range': 'Adultez', 'frequency': response.adultez })
      this.ageData.rows.push({ 'range': 'Vejez', 'frequency': response.vejez })
    }).catch(err => console.log(err));
    
    api.getEducationByTopic(data).then(response => {
      this.educationData.rows.length = 0
      this.educationData.rows.push({ 'education': 'Primaria', 'frequency': response.primaria })
      this.educationData.rows.push({ 'education': 'Secundaria', 'frequency': response.secundaria })
      this.educationData.rows.push({ 'education': 'Técnica y Tecnológica', 'frequency': response.tyt })
      this.educationData.rows.push({ 'education': 'Universitaria', 'frequency': response.universitaria })
      this.educationData.rows.push({ 'education': 'Postgrado', 'frequency': response.postgrado })
    }).catch(err => console.log(err));
    },
    filterSex(name){
      if(this.sex==name){
        this.sex=""
      }else{
        this.sex = name
      }
      this.filter.sex = this.sex
    },
    filterEducation(name){
      if(this.education==name){
        this.education=""
      }else{
        this.education = name
      }
      this.filter.education = this.education
    },
    filterAge(name){
      if(this.age==name){
        this.age=""
      }else{
        this.age = name
      }
      this.filter.age = this.age
    },
    checkTopicOne(event){
      if(this.checkboxTopicOne){
        this.filter.topicGeneral = this.topicOne
      }else{
        this.filter.topicGeneral = 0
      }
    },
    checkTopicTwo(event){
      if(this.checkboxTopicTwo){
        this.filter.topicGeneral = this.topicTwo
      }else{
        this.filter.topicGeneral = 0
      }
    },
    checkTopicThree(event){
      if(this.checkboxTopicThree){
        this.filter.topicGeneral = this.topicThree
      }else{
        this.filter.topicGeneral = 0
      }
    },
    checkTopicFour(event){
      if(this.checkboxTopicFour){
        this.filter.topicGeneral = this.topicFour
      }else{
        this.filter.topicGeneral = 0
      }
    },
    checkTopicFive(event){
      if(this.checkboxTopicFive){
        this.filter.topicGeneral = this.topicFive
      }else{
        this.filter.topicGeneral = 0
      }
    },
  }
};
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