<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container>
        <!--INITIAL IMAGE -->
        <v-layout row>
          <v-flex xs7>
            <br />
            <h1>¡Construyamos Paz!</h1>
            <br />
            <br />
            <p>El proyecto “Narrativas de Paz” tiene como propósito realizar mediciones de la percepción de la paz para cada individuo con el fin de aportar información valiosa para las campañas en curso de proyectos alineados a la construcción de paz y cultura ciudadana.</p>
            <br />
            <br />
          </v-flex>
        </v-layout>
      </v-container>
    </div>

    <!-- STEPPER -->

    <v-container>
      <v-layout row align-center justify-center>
        <v-flex xs12 md7>
          <v-stepper v-model="e1">
            <!--TABS -->
            <v-stepper-header>
              <v-stepper-step :complete="e1 > 1" step="1">Personal</v-stepper-step>

              <v-divider></v-divider>

              <v-stepper-step :complete="e1 > 2" step="2">Territorio</v-stepper-step>

              <v-divider></v-divider>

              <v-stepper-step :complete="e1 > 3" step="3">Educación</v-stepper-step>
            </v-stepper-header>

            <!-- ITEMS INSIDE EACH TAB-->
            <v-stepper-items>
              <v-stepper-content step="1">
                <personal-form-component></personal-form-component>

                <v-btn :ripple="false" class="ma-2 next" outline color="#673ab7"  @click="e1 = 2">Siguiente</v-btn>
              </v-stepper-content>

              <v-stepper-content step="2">
                <territory-form-component></territory-form-component>

                <v-btn :ripple="false" class="ma-2 next" outline color="#673ab7"  @click="e1 = 1">Anterior</v-btn>
                <v-btn :ripple="false" class="ma-2 next" outline color="#673ab7"  @click="e1 = 3">Siguiente</v-btn>
              </v-stepper-content>

              <v-stepper-content step="3">
                <education-form-component></education-form-component>

                <v-btn :ripple="false" class="ma-2 next" outline color="#673ab7"  @click="e1 = 2">Anterior</v-btn>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "BuildPeace",
  data() {
    return {
      e1: 0
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

.init {
  background-image: url("../assets/handpeace.png");
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

.next {
  text-transform: none;
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 33px;
  display: flex;
  align-items: center;
  text-align: center;
}
</style>
