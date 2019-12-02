<template>
  <div>
    <h3>{{name}}</h3>

  <div>
    <p>Sexo</p>
        <ve-pie :data="pieData" :settings="pieSettings"></ve-pie>
  </div>

  <div>
    <p>Edad</p>
        <ve-pie  :data="ageData" :settings="ageSettings"></ve-pie>
       <!-- <ve-bar :data="ageData"></ve-bar>-->
  </div>

  <div>
    <p>Educación</p>
        <ve-pie :data="educationData" :settings="educationSettings"></ve-pie>
       <!-- <ve-bar :data="educationData"></ve-bar>-->
  </div>
  </div>
</template>

<script>
import api from "../../axios.js";

export default {
  props: {
    campaign: Object,
    name: String,
    id: Number
  },
  data() {
    this.pieSettings = {
        dimension: 'gender',
        metrics: 'frequency'
      };
    this.ageSettings = {
        dimension: 'range',
        metrics: 'frequency'
      };
    this.educationSettings = {
        dimension: 'education',
        metrics: 'frequency'
      };    
    return {
      ageData: {
        columns: ['range','frequency'],
        rows: []
      },
      pieData: {
          columns: ['gender', 'frequency'],
          rows: []
        },
         educationData: {
          columns: ['education', 'frequency'],
          rows: []
        },
    };
  },
  created() {
    var data={id:this.campaign.id, territory:'', idTerritory:this.id}
    if(this.id <=22){
      data.territory = 'comuna'
    }else{
      data.territory = 'corregimiento'
    }
   
    api
      .getPeopleByCampaignAndTerritory(data)
      .then(response => {
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'Femenino', 'frequency': response.women })
        this.pieData.rows.push({ 'gender': 'Masculino', 'frequency': response.men })
        this.pieData.rows.push({ 'gender': 'Intersexual', 'frequency': response.intersexual })
      })
      .catch(err => console.log(err));
   

    api.getRangesOfAgeByCampaignAndTerritory(data).then(response => {
      this.ageData.rows.length = 0
      this.ageData.rows.push({ 'range': 'Primera infancia', 'frequency': response.primeraInfancia })
      this.ageData.rows.push({ 'range': 'Infancia', 'frequency': response.infancia })
      this.ageData.rows.push({ 'range': 'adolescencia', 'frequency': response.adolescencia })
      this.ageData.rows.push({ 'range': 'juventud', 'frequency': response.juventud })
      this.ageData.rows.push({ 'range': 'adultez', 'frequency': response.adultez })
      this.ageData.rows.push({ 'range': 'vejez', 'frequency': response.vejez })
    }).catch(err => console.log(err));
    
    api.getEducationByCampaignAndTerritory(data).then(response => {
      this.educationData.rows.length = 0
      this.educationData.rows.push({ 'education': 'Primaria', 'frequency': response.primaria })
      this.educationData.rows.push({ 'education': 'Pecundaria', 'frequency': response.secundaria })
      this.educationData.rows.push({ 'education': 'Técnica y tecnología', 'frequency': response.tyt })
      this.educationData.rows.push({ 'education': 'Universitaria', 'frequency': response.universitaria })
      this.educationData.rows.push({ 'education': 'Postgrado', 'frequency': response.postgrado })
    }).catch(err => console.log(err));
    

  }
};
</script>

<style scoped>
h3{
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  /*color: #0c186d;*/
}
p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 24px;
}
</style>