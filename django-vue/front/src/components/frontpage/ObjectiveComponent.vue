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
        description:"Las Narrativas de Paz son relatos construidos colectivamente que tienen como objetivo la construcción de una definición de qué sí es la paz para los caleños, de esta manera la toma de decisiones públicas será más acertada según los enfoques de territorio, capacidad y diferencial."
        };
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