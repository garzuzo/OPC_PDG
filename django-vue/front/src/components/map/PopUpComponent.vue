<template>
  <div>
      HOLAAAAAA
    <h3>{{comuna}} </h3>  
    <p>Mujeres: {{object.mujeres}}</p>
    <p>hombres: {{object.hombres}}</p>
    <p>Adolescentes: {{object.adolescencia}}</p>
    <p>Jóvenes: {{object.juventud}}</p>
    <p>Adultos: {{object.adultez}}</p>
    <p>Tercera edad: {{object.vejez}}</p>
  </div>
</template>

<script>
export default {
  props: {
    campaign: Object,
    comuna: String
  },
  data(){
      return{
          object:{
            mujeres: 0,
            hombres: 0,
            adolescencia: 0,
            juventud: 0,
            adultez: 0,
            vejez: 0
          }
      }
  },
  created(){
      var data = [this.campaign.id, this.comuna]
      api.getPeopleByCampaignAndComuna(data).then(response => {
        this.object.mujeres = response.women;
        this.object.hombres = response.men;
      }).catch(err => console.log(err))

      /*api.getRangesOfAgeByCampaignAndComuna(data).then(response => {
        this.object.adolescencia = response.adolescencia;
        this.object.juventud = response.juventud;
        this.object.adultez = response.adultez;
        this.object.vejez = response.vejez;
      })*/
  }
};
</script>