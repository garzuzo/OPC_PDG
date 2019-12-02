<template>

<div class="objective"> 

<v-container>
  <v-row justify="center" style="padding-top: 20vh; padding-bottom: 20vh;"> 
    <v-col cols="10" sm="10" md="5">
        <v-img
            :src="require('@/assets/person.png')"
            aspect-ratio="1"
            max-width="600"
            max-height="300"
          ></v-img>
      </v-col>
      
      <v-col cols="10" sm="10" md="7">
        <h3> {{subtitle}} </h3>
        <h2>{{title}}</h2>
        <br>
        <p>{{description}} </p>
        
      <v-row justify="start">
        <v-col cols="7" sm="7" md="5">
          <v-btn
            :ripple="false"
            class=" btn"
            color="#ffffff"
            depressed 
            rounded  
            light
            to="/campanas"
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
        title:"Narrativas que buscan construir definiciones de Paz",
        description:"Las campañas son narradas  por una diversidad de personas en los territorios denominados de la ciudad-región que desean contribuir a las mediciones de la percepción de paz de los ciudadanos con el fin de tener definiciones de qué si es paz y les ayude en los proyectos de cultura ciudadana que se lleven a cabo."
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
font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
text-align: justify;

color: #000000;
}

h2{
  font-family: Poppins;
font-style: normal;
font-weight: bold;
font-size: calc(24px + (48 - 24) * ((100vw - 300px) / (1600 - 300)));
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