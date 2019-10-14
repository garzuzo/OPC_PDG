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
          <v-col cols="6">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col cols="4">
            <h2>01 </h2>
            <h3>Responde ¿Para tí, ¿qué es la paz? </h3>
            <p> Las Narrativas de Paz son relatos construidos colectivamente para definir lo que sí es la paz para los caleños.</p>
          </v-col>

          <v-col cols="6">
            <h2>02 </h2>
            <h3>Comparate con personas </h3>
            <p> Las Narrativas de Paz son relatos construidos colectivamente para definir lo que sí es la paz para los caleños.</p>
          </v-col>

          <v-col cols="4">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col cols="6">
            <img src="@/assets/steps.png" />
          </v-col>

          <v-col cols="4">
            <h2>03 </h2>
            <h3>Comparte a tus conocidos </h3>
            <p> Las Narrativas de Paz son relatos construidos colectivamente para definir lo que sí es la paz para los caleños.</p>
          </v-col>

          <v-col cols="6">
            <h2>04 </h2>
            <h3>Construye Proyectos alineados a la paz y cultura ciudadana</h3>
            <p> Las Narrativas de Paz son relatos construidos colectivamente para definir lo que sí es la paz para los caleños.</p>
          </v-col>

          <v-col cols="4">
            <img src="@/assets/steps.png" />
          </v-col>
        </v-row>

      </v-container>

    </div>


</template>


<script>
export default {
  data() {
    return {
      subtitle:"Cómo funciona",
      title:"Construir paz entre todos",
      description:"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam egestas, metus ac dignissim mattis, metus risus pretium ligula, ut mattis purus eros at nisl."
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

</style>