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

    <v-container>
      <!-- STEPPER -->
      <v-layout row align-center justify-center>
        <v-flex xs12 md7>
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
                <personal-form-component></personal-form-component>

                <v-container>
                  <v-layout row justify-end>
                    <v-flex xs2>
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outline
                        color="#673ab7"
                        @click="e1 = 2"
                      >Siguiente</v-btn>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-stepper-content>

              <v-stepper-content step="2">
                <territory-form-component></territory-form-component>

                <v-container>
                  <v-layout row justify-space-between>
                    <v-flex xs2>
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outline
                        color="#673ab7"
                        @click="e1 = 1"
                      >Anterior</v-btn>
                    </v-flex>
                    <v-flex xs2>
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outline
                        color="#673ab7"
                        @click="e1 = 3"
                      >Siguiente</v-btn>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-stepper-content>

              <v-stepper-content step="3">
                <education-form-component></education-form-component>

                <v-btn
                  :ripple="false"
                  class="ma-2 next"
                  outline
                  color="#673ab7"
                  @click="e1 = 2"
                >Anterior</v-btn>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-flex>
      </v-layout>

      <!-- NARRATIVE -->
      <br>

      <v-layout row align-center justify-center>
        <v-flex xs8>
          <h3>Con un texto ayudanos a responder la pregunta:</h3>
          <br>
          <div class="form-group">
            <label for="narrative">Para ti, ¿Qué si es paz?</label>
            <v-textarea
              v-model="narrative"
              outline
              name="narrative"
              single-line
              counter="500"
              color="#000000"
              class="input"
            ></v-textarea>
          </div>
        </v-flex>
      </v-layout>

      <!--KEYWORDS -->
      <v-layout column align-center justify-center>
          <v-flex xs8>
              <h3>Dinos 5 palabras que para ti reflejen Qué si es paz</h3>
          </v-flex> 
            <br>
          <v-layout row align-center justify-space-between>
              <v-flex xs2>
                  <v-text-field
              v-model="word1"
              outline
              single-line
              color="#000000"
              height="16"
              required
              name="word1"
              class="input"
            ></v-text-field>
              </v-flex> 

              <v-flex xs2>
                  <v-text-field
              v-model="word2"
              outline
              single-line
              color="#000000"
              height="16"
              required
              name="word2"
              class="input"
            ></v-text-field>
              </v-flex>  

              <v-flex xs2>
                  <v-text-field
              v-model="word3"
              outline
              single-line
              color="#000000"
              height="16"
              required
              name="word3"
              class="input"
            ></v-text-field>
              </v-flex>

              <v-flex xs2>
                  <v-text-field
              v-model="word4"
              outline
              single-line
              color="#000000"
              height="16"
              required
              name="word4"
              class="input"
            ></v-text-field>
              </v-flex>

              <v-flex xs2>
                  <v-text-field
              v-model="word5"
              outline
              single-line
              color="#000000"
              height="16"
              required
              name="word5"
              class="input"
            ></v-text-field>
              </v-flex>

          </v-layout>       
      </v-layout>   
    </v-container>
  </div>
</template>

<script>
export default {
  name: "BuildPeace",
  data() {
    return {
      e1: 0,
      narrative: '',
      word1:'',
      word2:'',
      word3:'',
      word4:'',
      word5:''
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
body{
    background-color: white;
}
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
}

.input {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 36px;
}
</style>
