<template>
    <div>
      <v-row justify="center">
      <v-col cols="8" sm="8" md="6"> 
        <h3> {{subtitle}} </h3>
        <h2>{{title}}</h2>
        <p>{{description}} </p>
      </v-col> 
      </v-row>

      <v-container>

        <v-row justify="center"> 

          <v-col class="hidden-sm-and-down" md="5">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col  cols="10" sm="10" md="5">
            <h2>01 </h2>
            <h3>Responde ¿Para tí, qué es la paz? </h3>
            <p> Es importante que te cuestiones para ti,¿Qué sí es la Paz? escribiendo un texto corto y 5 palabras clave. 

Con esta información contribuyes a definir tu Paz, indicadores y grupos para establecer el impacto de los proyectos y las iniciativas de Construcción de Paz.</p>
          </v-col>

          <v-col cols="10" sm="10" md="5">
            <h2>02 </h2>
            <h3>Comparate con personas </h3>
            <p> Podrás comparar tu percepción de paz con la de los demás participantes en diferentes enfoques como el territorio, el diferencial, el desarrollo de capacidades y el tiempo.</p>
          </v-col>

          <v-col  class="hidden-sm-and-down" md="5">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col class="hidden-sm-and-down" md="5">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col  cols="10" sm="10" md="5">
            <h2>03 </h2>
            <h3>Comparte con tus conocidos </h3>
            <p> Construir paz significa comprender que incluso las personas mas cercanas definen su Paz de una manera diferente a la nuestra. 

                <br>Usa esta herramienta para construir múltiples definiciones de Paz en tu hogar, en tu ciudad y en tu región. Incluso con tus amigos que ahora visitan el país e incluso con los que se fueron y que volverán.</p>
          </v-col>

          <v-col cols="10" sm="10" md="5">
            <h2>04 </h2>
            <h3>Contribuye a medir el impacto de la Construcción de Paz</h3>
            <p> Tu Narrativa de Paz es un insumo clave que contribuye a 
recopilar información referente a la percepción de la Paz y la Construcción de Paz; a definir indicadores y grupos para establecer el impacto de un proyecto o iniciativa de Construcción de paz.</p>
          </v-col>

          <v-col  class="hidden-sm-and-down" md="5">
            <img src="@/assets/steps.png" />
          </v-col>
        </v-row>

        <v-container>
      <v-row justify="end">
        <v-col cols="10" sm="10" md="5">
          <v-btn
            :ripple="false"
            class="mx-2 pa-5 btn peace"
            color="#673AB7"
            depressed 
            rounded  
            dark
            to="/construirpaz"
          >Quiero construir paz</v-btn>
        </v-col>
      </v-row>
    </v-container>

      </v-container>

    </div>


</template>


<script>
export default {
  data() {
    return {
      subtitle:"Cómo funciona",
      title:"Construir paz es definir la paz entre todos",
      description:"El propósito de medir las percepciones de paz de los ciudadanos es que entre todos logremos construir multiples definiciones de paz que varian según diferentes enfoques como el territorio, el diferencial, el desarrollo de capacidades y el tiempo."
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap');


.init{
  margin: 0 auto;
  width: 30%;
}

h3{
  font-family: Poppins;
font-style: normal;
font-weight: bold;
font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
text-align: justify;

color: #0C186D;
}

h2{
  font-family: Poppins;
font-style: normal;
font-weight: bold;
font-size: calc(24px + (48 - 24) * ((100vw - 300px) / (1600 - 300)));
}

p{
  font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 18px;
line-height: 21px;

color: #000000;
}

.peace{
  text-transform: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1600 - 300)));
  line-height: 24px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

</style>