<template>

<div class="objective"> 

  <v-row justify="center"> 
    <v-col cols="4">
      <img src="@/assets/person.png"/>
      </v-col>
      <v-col cols="6">
        <h3> {{subtitle}} </h3>
        <h2>{{title}}</h2>
        <br>
        <p>{{description}} </p>
        
      <v-row justify="start">
        <v-col cols="5">
          <v-btn
            :ripple="false"
            class="ma-2 ml-5 btn"
            color="#ffffff"
            depressed 
            rounded  
            light
            to="/construirpaz"
          >Aprender más</v-btn>
        </v-col>
      </v-row>
      </v-col>
  </v-row>

  
    </div> 


</template>



<script>
export default {
  name: "Objective",
  data() {
    return {
        subtitle:"Campañas",
        title:"Narrativas que buscan construir Paz",
        description:"Las Narrativas de Paz son relatos construidos colectivamente para definir lo que sí es la paz para los caleños. Estos relatos surgen de talleres que funcionan como espacios de encuentro para la construcción de una definición de paz desde un enfoque territorial. "
        };
  }
};
</script>

<style scoped>

.objective{
  background-color: #673ab7;
  height: 500px;
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