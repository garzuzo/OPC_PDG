<template>
  <div>
    <navbar-component v-if="!logged"></navbar-component>
    <v-container>
      <v-row>
        <!--{{idCampaign}} - {{idUser}}-->
        <!--MAP -->
        <v-col cols="12" sm="12" md="6">
            <v-switch class="hidden-sm-and-down" v-model="switch1" label="Mapa de departamentos"></v-switch>
          <map-campaign-component class="hidden-sm-and-down" v-if="!switch1" :filter="filter"></map-campaign-component>
          <map-states-campaign-component v-if="switch1" :filter="filter"></map-states-campaign-component>
        </v-col>

        <!--VISUALIZATION-->
        <v-col cols="12" sm="12" md="6">
          <h3>En la campaña "{{campaign}}", para ti la paz está asociada a las 2 nubes de palabras que presentan el lenguaje utilizado para referirse a la Paz.</h3>
           <p>Al dar click sobre los conceptos agrupados en las nubes de palabras, el mapa presentará la afinidad con dicha nube representada por colores y la variación en los gráficos de sexo, edad y educación.</p> 
          <ve-wordcloud
            :data="topicOneData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicOneEvents"
            width="400px" height="350px"
            shape="diamond"
          ></ve-wordcloud>
          <ve-wordcloud
            :data="topicTwoData"
            :tooltip-visible="tooltip"
            :textStyle="textStyle"
            :settings="wordSettings"
            :events="topicTwoEvents"
            width="400px" height="350px"
            shape="diamond"
          ></ve-wordcloud>
        </v-col>
      </v-row>
      <h3>Dimensiones para filtrar en el mapa</h3>
      <p>Los siguientes 3 gráficos presentan atributos de los enfoques población diferencial y desarrollo de capacidades. Al dar click sobre sexo, edad y/o situación educativa, el mapa cambiará para mostrar la afinidad con el grupo, también si escoges una opción de nube de palabra.
        Recuerda que puedes combinar las dimensiones. 
      </p>
      <v-row justify="start">
        
        <v-col cols="6" sm="6" md="3">
          <v-checkbox
            v-model="checkboxTopicOne"
            label="Nube primaria"
            @change="checkTopicOne($event)"
          ></v-checkbox>
        </v-col>
        <v-col cols="6" sm="6" md="3">
          <v-checkbox
            v-model="checkboxTopicTwo"
            label="Nube secundaria"
            @change="checkTopicTwo($event)"
          ></v-checkbox>
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
          <!--<ve-bar :data="ageData"></ve-bar>-->
        </v-col>

        <v-col cols="12" sm="12" md="4">
          <h3>Educación</h3>
          <ve-pie :data="educationData" :settings="educationSettings" :events="educationEvents"></ve-pie>
          <!--<ve-bar :data="educationData"></ve-bar>-->
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
    </v-container>
  </div>
</template>

<script>
import echarts from "echarts";
import api from "../../axios";

export default {
  props:{
    logged:Boolean
  },
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
        sizeMin: 12,
        sizeMax: 24
    }
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
        rows: [
          /*{ word: "tranquilidad", count: 2199 },
          { word: "familia", count: 1288 },
          { word: "amor", count: 14000 },
          { word: "cultura", count: 10000 },
          { word: "paz", count: 10388 }*/
        ]
      },
      topicTwoData: {
        columns: ["word", "count"],
        rows: [
          /*{ word: "tranquilidad", count: 2199 },
          { word: "familia", count: 1288 },
          { word: "amor", count: 14000 },
          { word: "cultura", count: 10000 },
          { word: "paz", count: 10388 }*/
        ]
      },
      narratives: [
        "Para mi la paz es sentir que el río está limpio",
        "Para mi la paz es que la gente no tire basuras al río"
      ],
      campaign: "",
      sex:"",
      age:"",
      education:"",
      idCampaign: this.$store.state.campaign,
      idUser: this.$store.state.user,
      topicOne: 0,
      topicTwo: 0,
      checkboxTopicOne: false, 
      checkboxTopicTwo: false,
      switch1: false,
      filter:{
        topicOne:0,
        topicTwo:0,
        sex: '',
        age:'',
        education:'',
        idCampaign:0
      }
    };
  },
  created() {
    console.log(this.idCampaign)
    console.log(this.idUser)
    let campaign = { id: this.idCampaign };
    api
      .getCampaign(campaign)
      .then(response => {
        this.campaign = response.title;
      })
      .catch(err => console.log(err));

    this.filter.idCampaign = this.idCampaign
    
    let user = { id: this.idUser };
    api
      .getTwoTopicsByPerson(user)
      .then(response => {
        this.topicOne = response.id_primary;
        this.topicTwo = response.id_secondary;

        let array= response.topic_primary.split(', ')
        let array2= response.topic_secondary.split(', ')
        for (var i = 0; i < array.length; i++) {
          var actOne = { word: array[i], count: 2 };
          this.topicOneData.rows.push(actOne);
          var actTwo = { word: array2[i], count: 2 };
          this.topicTwoData.rows.push(actTwo);
        }
      })
      .catch(err => console.log(err));

      api.getTopicWordCount().then(response=>{
      for (var i = 0; i < this.topicOneData.rows.length; i++) {
          this.topicOneData.rows[i].count = parseInt(response.topic_percentage[this.topicOne-1][i]);
          this.topicTwoData.rows[i].count = parseInt(response.topic_percentage[this.topicTwo-1][i]);
        }
    }).catch(err=> console.log(err))


     this.init() 
  },
  methods: {
    init(){
      let data= {id:this.idCampaign}
      api.getPeopleByCampaign(data)
      .then(response => {
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'Femenino', 'frequency': response.women })
        this.pieData.rows.push({ 'gender': 'Masculino', 'frequency': response.men })
        this.pieData.rows.push({ 'gender': 'Intersexual', 'frequency': response.intersexual })
      })
      .catch(err => console.log(err));   

    api.getRangesOfAgeByCampaign(data).then(response => {
      this.ageData.rows.length = 0
      this.ageData.rows.push({ 'range': 'Primera infancia', 'frequency': response.primeraInfancia })
      this.ageData.rows.push({ 'range': 'Infancia', 'frequency': response.infancia })
      this.ageData.rows.push({ 'range': 'Adolescencia', 'frequency': response.adolescencia })
      this.ageData.rows.push({ 'range': 'Juventud', 'frequency': response.juventud })
      this.ageData.rows.push({ 'range': 'Adultez', 'frequency': response.adultez })
      this.ageData.rows.push({ 'range': 'Vejez', 'frequency': response.vejez })
    }).catch(err => console.log(err));
    
    api.getEducationByCampaign(data).then(response => {
      this.educationData.rows.length = 0
      this.educationData.rows.push({ 'education': 'Primaria', 'frequency': response.primaria })
      this.educationData.rows.push({ 'education': 'Secundaria', 'frequency': response.secundaria })
      this.educationData.rows.push({ 'education': 'Técnica y Tecnológica', 'frequency': response.tyt })
      this.educationData.rows.push({ 'education': 'Universitaria', 'frequency': response.universitaria })
      this.educationData.rows.push({ 'education': 'Postgrado', 'frequency': response.postgrado })
    }).catch(err => console.log(err));
    },
    filterTopicOne(){
      let data= {id:this.topicOne, type:'Primario'}
      this.filter.topicOne = this.topicOne
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

    filterTopicTwo(){
      let data= {id:this.topicTwo, type:'Secundario'}
      this.filter.topicTwo = this.topicTwo
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
        this.filter.topicOne = this.topicOne
      }else{
        this.filter.topicOne = 0
      }
    },
    checkTopicTwo(event){
      if(this.checkboxTopicTwo){
        this.filter.topicTwo = this.topicTwo
      }else{
        this.filter.topicTwo = 0
      }
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