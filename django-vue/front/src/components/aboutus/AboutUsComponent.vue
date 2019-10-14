<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container>
        <!--INITIAL IMAGE -->
        <v-row>
          <v-col cols="7">
            <br />
            <h1>Sobre nosotros</h1>
            <br />
            <br />
            <p>El Observatorio de Paz y Cultura Ciudadana no ha tenido la capacidad, con el taller actual de Narrativas de Paz.</p>
            <br />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <v-row align="center" justify="space-around">
        <v-col cols="6">
          <h3>Problema</h3>
          <p
            class="paragraph"
          >El Observatorio de Paz y Cultura Ciudadana no ha tenido la capacidad, con el taller actual de Narrativas de Paz, de mejorar la representatividad y la cobertura en las zonas de interés del mandato ciudad-región para poder analizar los datos de paz desde diferentes enfoques</p>
        </v-col>

        <v-col cols="6">
          <v-img
            src="https://picsum.photos/id/11/500/300"
            lazy-src="https://picsum.photos/id/11/10/6"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>
      </v-row>

      <v-row align="center" justify="space-around">
        <v-col align-self="start" cols="6">
          <v-img
            src="https://picsum.photos/id/11/500/300"
            lazy-src="https://picsum.photos/id/11/10/6"
            aspect-ratio="1"
            max-width="500"
            max-height="300"
          ></v-img>
        </v-col>

        <v-col cols="6">
          <h3>Solución</h3>
          <p
            class="paragraph"
          >Esta plataforma digital “Narrativas de Paz” permitirá hacer, primero, la recolección de datos de percepción de paz a través de un formulario para conocer datos específicos de la persona y un espacio para construir una narrativa respondiendo “Para ti, ¿Qué si es Paz?”. Posteriormente, se haría un análisis de datos enfocado a la minería de texto y, por último, una retribución inmediata al ciudadano a través de visualizaciones de datos.</p>
        </v-col>
      </v-row>

      <h3 align="center">Nuestro equipo</h3>

      <v-row justify="center">
        <v-col v-for="n in 4" :key="n" class="d-flex child-flex" cols="5">
          <member-item-component></member-item-component>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
body {
  background-color: white;
}
.init {
  background-image: url("../../assets/handpeace.png");
  background-size: cover;
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