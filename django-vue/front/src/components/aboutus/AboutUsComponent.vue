<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row style="padding-top: 20vh; padding-bottom:20vh;">
          <v-col sm="12" md="7">
            <h1 style="padding-bottom:10vh;">Sobre nosotros</h1>
            <p>El Observatorio de Paz y Convivencia (OPC) tiene entre sus objetivos definir un marco de medición de Paz y cultura ciudadana en perspectiva de ciudad-región con los enfoques de territorio, diferencial, desarrollo de capacidades y tiempo, por esta razón ha surgido el método y los talleres de Narrativas de Paz.</p>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <v-row align="center" justify="center" style="padding-top: 20vh;">
        <v-col cols="12" sm="12" md="6">
          <h3>Problema</h3>
          <p>El Observatorio de Paz y Convivencia ha logrado una cobertura en las zonas de interés de la perspectiva ciudad-región, sin embargo se desea mejorar la representatividad y la cobertura en dicha perspectiva para poder analizar los datos de paz que proveen los ciudadanos desde diferentes enfoques (territorio, diferencial, desarrollo de capacidades y tiempo)</p>
        </v-col>

        <v-col cols="12" sm="12" md="6">
          <v-img
            :src="require('@/assets/problem.png')"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>
      </v-row>

      <v-row align="center" justify="center" style="padding-top: 20vh;">
        <v-col class="hidden-sm-and-down" align-self="start"  cols="12" sm="12" md="6">
          <v-img
            :src="require('@/assets/solution.png')"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>

        <v-col  cols="12" sm="12" md="6">
          <h3>Solución</h3>
          <p>La plataforma digital “Narrativas de Paz” permitirá ampliar el rango de cobertura del método de narrativas de Paz y proyectar el método para realizar talleres virtuales, por tanto su efecto es recolectar datos de narrativas, generar datos de percepción de paz y facilitar su comparación entre personas bajo los diferentes enfoques. El enfoque analítico de la solución incluye ciencia de datos, minería de texto e inteligencia artificial.</p>
        </v-col>

        <v-col class="hidden-md-and-up" align-self="start"  cols="12" sm="12" md="6">
          <v-img
            :src="require('@/assets/solution.png')"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>

      </v-row>

      <h3 align="center" style="padding-top: 20vh; padding-bottom:10vh;">Nuestro equipo</h3>

      <v-row justify="center">
        <v-col v-for="item in members" :key="item.name" class="d-flex child-flex"  cols="10" sm="10" md="5">
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
        {name:'Juan Carlos Muñoz, PhD', img:'sandra', profession: 'Profesor Ingeniería de Sistemas', place: 'Universidad Icesi'},
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
  /*calc([minimum size] + ([maximum size] - [minimum size]) * ((100vw - [minimum viewport width]) / ([maximum viewport width] - [minimum viewport width])));*/
  font-size: calc(32px + (64 - 32) * ((100vw - 300px) / (1600 - 300)));
  color: #0c186d;
}

p {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: calc(24px + (44 - 24) * ((100vw - 300px) / (1600 - 300)));
  /*font-size: 44px;
  line-height: 66px;*/
  color: #0c186d;
}

h4 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
  /*font-size: 24px;
  line-height: 36px;*/

  color: #0c186d;
}

h5{
    font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1600 - 300)));
  /*font-size: 20px;
  line-height: 36px;*/

  color: #000000;
}

/*.paragraph {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 36px;
}*/

.img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  margin-bottom:10px;
}
</style>