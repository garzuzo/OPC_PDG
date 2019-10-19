<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container>
        <!--INITIAL IMAGE -->
        <v-row>
          <v-col cols="7">
            <br />
            <h1>¡Construyamos Paz!</h1>
            <br />
            <br />
            <p>El proyecto “Narrativas de Paz” tiene como propósito realizar mediciones de la percepción de la paz para cada individuo con el fin de aportar información valiosa para las campañas en curso de proyectos alineados a la construcción de paz y cultura ciudadana.</p>
            <br />
            <br />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <!-- STEPPER -->
      <v-row align="center" justify="center">
        <v-col cols="8" md="7">
          <v-stepper v-model="e1">
            <!--TABS -->
            <v-stepper-header>
              <v-stepper-step color="#0C186D" class="input" :complete="e1 > 1" step="1">Personal</v-stepper-step>

              <v-divider></v-divider>

              <v-stepper-step color="#0C186D" class="input" :complete="e1 > 2" step="2">Territorio</v-stepper-step>

              <v-divider></v-divider>

              <v-stepper-step color="#0C186D" class="input" :complete="e1 > 3" step="3">Educación</v-stepper-step>
            </v-stepper-header>

            <!-- ITEMS INSIDE EACH TAB-->
            <v-stepper-items>
              <v-stepper-content step="1">
                <personal-form-component v-on:nameToParent="onNameClick" v-on:lastnameToParent="onLastnameClick" v-on:ageToParent="onAgeClick" v-on:genderToParent="onGenderClick"></personal-form-component>
               
                <v-container>
                  <v-row justify="end">
                    <v-col cols="2">
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outlined
                        color="#673ab7"
                        @click="e1 = 2"
                      >Siguiente</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-stepper-content>

              <v-stepper-content step="2">
                <territory-form-component></territory-form-component>

                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="2">
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outlined
                        color="#673ab7"
                        @click="e1 = 1"
                      >Anterior</v-btn>
                    </v-col>
                    <v-col cols="2">
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outlined
                        color="#673ab7"
                        @click="e1 = 3"
                      >Siguiente</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-stepper-content>

              <v-stepper-content step="3">
                <education-form-component></education-form-component>

                <v-btn
                  :ripple="false"
                  class="ma-2 next"
                  outlined
                  color="#673ab7"
                  @click="e1 = 2"
                >Anterior</v-btn>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-col>
      </v-row>

      <!-- NARRATIVE -->
      <br />
       HERE ARE THE NEW THINGS:
       {{age}} 
       {{gender}}
       {{name}}
       {{lastname}}
      <v-row align="center" justify="center">
        <v-col cols="8">
          <h3>Con un texto ayudanos a responder la pregunta:</h3>
          <br />
          <div class="form-group">
            <label for="narrative">Para ti, ¿Qué si es paz?</label>
            <v-textarea
              v-model="narrative"
              outlined
              name="narrative"
              counter="500"
              color="#0C186D"
              class="input"
            ></v-textarea>
          </div>
        </v-col>
      </v-row>
       
      <!--KEYWORDS -->
      <v-row align="center" justify="center">
        <v-col cols="8">
          <h3>Dinos 5 palabras que para ti reflejen Qué si es paz</h3>
        </v-col>
      </v-row>

      <v-row align="center" justify="space-between">
        <v-col cols="2">
          <v-text-field
            v-model="word1"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word1"
            class="input"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word2"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word2"
            class="input"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word3"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word3"
            class="input"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word4"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word4"
            class="input"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word5"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word5"
            class="input"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row align="center" justify="center" no-gutters>
        <v-col cols="2">
          <v-btn :ripple="false" class="ma-2 save" color="#673ab7" dark>Finalizar</v-btn>
        </v-col>
        <v-col cols="2">
          <p>¿Deseas guardar tus datos para una próxima ocasión? </p>
          <v-btn :ripple="false" class="ma-2 save" color="#673ab7" dark>Crea tu cuenta</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "BuildPeace",
  data() {
    return {
      e1: 0,
      narrative: "",
      word1: "",
      word2: "",
      word3: "",
      word4: "",
      word5: "",
      //PERSONAL COMPONENT
      age: 0,
      gender: "",
      name: "",
      lastname: ""
    };
  },
  methods:{
    onAgeClick (value) {
      this.age = value
    },
    onGenderClick (value){
      this.gender = value
    },
    onNameClick(value){
      this.name = value
    },
    onLastnameClick(value){
      this.lastname = value
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

label {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  text-align: center;
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
  letter-spacing: normal !important;
}

.save {
  text-transform: none;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 33px;
  display: flex;
  align-items: center;
  text-align: center;
}
.input {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 36px;
}
</style>
