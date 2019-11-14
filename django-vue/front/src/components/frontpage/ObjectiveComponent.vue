<template>

<div class="objective"> 

<v-container>

  <v-row justify="center" style="padding-top: 20vh; padding-bottom: 20vh;">
      <v-col justify="center" cols="7">
        <h3> {{subtitle}} </h3>
        <h2>{{title}}</h2>
        <br>
        <p>{{description}} </p>
      </v-col>
      <v-col cols="4">
        <v-img
            :src="require('@/assets/objective.png')"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
      </v-col>
  </v-row>
</v-container>
    </div> 


</template>



<script>
export default {
  name: "Objective",
  data() {
    return {
        subtitle:"Objetivo",
        title:"Construir paz entre todos",
        description:"Las Narrativas de Paz son relatos construidos colectivamente que tienen como objetivo la construcción de deficiones de paz desde Cali a partir de la pregunta 'Para ti, ¿Qué sí es paz?'. De esta manera, contribuye a la toma de decisiones públicas efectivas a partir de los enfoques de territorio, diferencial, desarrollo de capacidades y tiempo, facilita datos abiertos y colaboraciones abiertas en materia de construcción de paz y cultura ciudadana. "     };
  }
};
</script>

<style scoped>

.objective{
  background-color: #673ab7;
}

h3{
  font-family: Poppins;
font-style: normal;
font-weight: bold;
font-size: 24px;
line-height: 36px;
text-align: justify;

color: #000000;
}

h2{
  font-family: Poppins;
font-style: normal;
font-weight: bold;
font-size: 48px;
line-height: 72px;
color: #ffffff
}

p{
  font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 18px;
line-height: 21px;

color:#ffffff;
}
</style>