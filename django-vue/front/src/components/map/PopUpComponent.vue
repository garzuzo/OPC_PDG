<template>
  <div>
    <h3>{{name}}</h3>
    <!--<p>Mujeres: {{object.mujeres}}</p>
    <p>hombres: {{object.hombres}}</p>
    <p>Adolescentes: {{object.adolescencia}}</p>
    <p>Jóvenes: {{object.juventud}}</p>
    <p>Adultos: {{object.adultez}}</p>
    <p>Tercera edad: {{object.vejez}}</p>-->

  <div>
    <p>Sexo</p>
        <ve-pie id="pie" :data="pieData" :settings="pieSettings"></ve-pie>
  </div>

  <div>
    <p>Edad</p>
        <ve-bar :data="ageData"></ve-bar>
  </div>

  <div>
    <p>Educación</p>
        <ve-bar :data="educationData"></ve-bar>
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
    return {
      object: {
        mujeres: 0,
        hombres: 0,
        primeraInfancia: 0,
        infancia: 0,
        adolescencia: 0,
        juventud: 0,
        adultez: 0,
        vejez: 0
      },
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
    };
  },
  created() {
    var data = [this.campaign.id, this.name];
    api
      .getPeopleByCampaignAndComuna(data)
      .then(response => {
        this.object.mujeres = response.women;
        this.object.hombres = response.men;
        this.pieData.rows.length = 0
        this.pieData.rows.push({ 'gender': 'mujeres', 'frequency': response.women })
        this.pieData.rows.push({ 'gender': 'hombres', 'frequency': response.men })
      })
      .catch(err => console.log(err));
   

    api.getRangesOfAgeByCampaignAndComuna(data).then(response => {
      this.object.primeraInfancia = response.primeraInfancia;
      this.object.infancia = response.infancia;
      this.object.adolescencia = response.adolescencia;
      this.object.juventud = response.juventud;
      this.object.adultez = response.adultez;
      this.object.vejez = response.vejez;
      this.ageData.rows.length = 0
      this.ageData.rows.push({ 'range': '0-5', 'frequency': response.primeraInfancia })
      this.ageData.rows.push({ 'range': '6-11', 'frequency': response.infancia })
      this.ageData.rows.push({ 'range': '12-18', 'frequency': response.adolescencia })
      this.ageData.rows.push({ 'range': '19-26', 'frequency': response.juventud })
      this.ageData.rows.push({ 'range': '27-59', 'frequency': response.adultez })
      this.ageData.rows.push({ 'range': '60 o más', 'frequency': response.vejez })
    });
    
    

  }
};
</script>