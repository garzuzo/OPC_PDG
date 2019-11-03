<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row style="padding-top: 20vh; padding-bottom:20vh;">
          <v-col cols="7">
            <h1 style="padding-bottom:10vh;">Sobre nosotros</h1>
            <p>El Observatorio de Paz y Cultura Ciudadana (OPC) tiene como objetivo realizar mediciones de la percepción de Paz bajo el mandato ciudad-región de Cali y alrededores, por ende han surgido los Talleres de Narrativas de Paz.</p>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <v-row align="center" justify="center" style="padding-top: 20vh;">
        <v-col cols="6">
          <h3>Problema</h3>
          <p
            class="paragraph"
          >El Observatorio de Paz y Cultura Ciudadana no ha tenido la capacidad, con el taller actual de Narrativas de Paz, de mejorar la representatividad y la cobertura en las zonas de interés del mandato ciudad-región para poder analizar los datos de paz desde diferentes enfoques (tiempo, territorio,capacidades y diferencial)</p>
        </v-col>

        <v-col cols="6">
          <v-img
            :src="require('@/assets/problem.png')"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>
      </v-row>

      <v-row align="center" justify="center" style="padding-top: 20vh;">
        <v-col align-self="start" cols="6">
          <v-img
            :src="require('@/assets/solution.png')"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>

        <v-col cols="6">
          <h3>Solución</h3>
          <p
            class="paragraph"
          >La plataforma digital “Narrativas de Paz” permitirá hacer, primero, la recolección de datos de percepción de paz para conocer datos específicos de la persona y un espacio para construir una narrativa respondiendo “Para ti, ¿Qué si es Paz?”. Posteriormente, se haría un análisis de datos enfocado a la minería de texto y, por último, una retribución inmediata al ciudadano a través de visualizaciones de datos.</p>
        </v-col>
      </v-row>

      <h3 align="center" style="padding-top: 20vh; padding-bottom:10vh;">Nuestro equipo</h3>

      <v-row justify="center">
        <v-col v-for="item in members" :key="item.name" class="d-flex child-flex" cols="5">
          <member-item-component :member="item"></member-item-component>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data(){
    return {
      members:[
        {name:'Sandra Niño', img:'sandra', profession: 'Estudiante Ingeniería de Sistemas', place: 'Universidad Icesi'},
        {name:'Johnatan Garzón', img:'johnatan', profession: 'Estudiante Ingeniería de Sistemas', place: 'Universidad Icesi'},
        {name:'Juan Carlos Muñoz', img:'sandra', profession: 'Profesor Ingeniería de Sistemas', place: 'Universidad Icesi'},
        {name:'Mauricio Sedano', img:'sandra', profession: 'Contratista OPC', place: 'OPC-Alcaldía Santiago de Cali'},
      ]
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
body {
  background-color: white;
}
.init {
  background-image: url("../../assets/handpeace.png");
  background-size: cover;
  height: 100vh;
}

h1 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 64px;
  line-height: 96px;
  color: #0c186d;
}

p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 36px;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 44px;
  line-height: 66px;

  color: #0c186d;
}

h4 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 36px;

  color: #0c186d;
}

h5{
    font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 36px;

  color: #000000;
}

.paragraph {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 36px;
}

.img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin-bottom:10px;
}
</style>