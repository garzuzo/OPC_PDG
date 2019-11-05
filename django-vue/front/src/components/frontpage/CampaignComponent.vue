<template>

<div class="objective"> 

<v-container>
  <v-row justify="center" style="padding-top: 20vh; padding-bottom: 20vh;"> 
    <v-col cols="5">
        <v-img
            :src="require('@/assets/person.png')"
            aspect-ratio="1"
            max-width="600"
            max-height="300"
          ></v-img>
      </v-col>
      
      <v-col cols="7">
        <h3> {{subtitle}} </h3>
        <h2>{{title}}</h2>
        <br>
        <p>{{description}} </p>
        
      <v-row justify="start">
        <v-col cols="5">
          <v-btn
            :ripple="false"
            class=" btn"
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
</v-container>
  
    </div> 


</template>



<script>
export default {
  name: "Objective",
  data() {
    return {
        subtitle:"Campañas",
        title:"Narrativas que buscan construir Paz",
        description:"Las campañas son realizadas por diferentes personas de la ciudad-región que desean contribuir a las mediciones de la percepción de paz de los ciudadanos con el fin de tener una definición de qué si es paz y les ayude en los proyectos de cultura ciudadana que se lleven a cabo."
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

.btn{
  text-transform: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 24px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>