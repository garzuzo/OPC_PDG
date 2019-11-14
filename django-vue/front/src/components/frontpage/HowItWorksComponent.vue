<template>
    <div>
      <v-row justify="center">
      <v-col cols="6" > 
        <h3> {{subtitle}} </h3>
        <h2>{{title}}</h2>
        <p>{{description}} </p>
      </v-col> 
      </v-row>

      <v-container>

        <v-row justify="center"> 

          <v-col cols="4">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col offset="1" cols="4">
            <h2>01 </h2>
            <h3>Responde ¿Para tí, qué es la paz? </h3>
            <p> Es importante que te cuestiones qué es la paz para ti de manera que contribuyas a las mediciones de percepción de paz.</p>
          </v-col>

          <v-col cols="4">
            <h2>02 </h2>
            <h3>Comparate con personas </h3>
            <p> Podrás comparar tu percepción de paz con la de los demás participantes en diferentes enfoques como el territorio, el diferencial, el desarrollo de capacidades y el tiempo.</p>
          </v-col>

          <v-col offset="1" cols="4">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col cols="4">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col offset="1" cols="4">
            <h2>03 </h2>
            <h3>Comparte a tus conocidos </h3>
            <p> Ayudanos a que más personas contribuyan a la construcción de paz para la ciudad y región para que puedan compararse contigo y los demás.</p>
          </v-col>

          <v-col cols="4">
            <h2>04 </h2>
            <h3>Contribuye a proyectos alineados a la construcción de paz y convivencia</h3>
            <p> Narrativas de Paz es un insumo importante para definir proyectos alineados a la construcción de paz y convivencia puesto que ayuda a la toma de decisiones públicas para la ciudad y región.</p>
          </v-col>

          <v-col offset="1" cols="4">
            <img src="@/assets/steps.png" />
          </v-col>
        </v-row>

        <v-container>
      <v-row justify="end">
        <v-col cols="5">
          <v-btn
            :ripple="false"
            class="mx-2 btn peace"
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
      title:"Construir paz entre todos",
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
font-size: 24px;
line-height: 36px;
text-align: justify;

color: #0C186D;
}

h2{
  font-family: Poppins;
font-style: normal;
font-weight: bold;
font-size: 48px;
line-height: 72px;
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
  font-size: 20px;
  line-height: 24px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

</style>