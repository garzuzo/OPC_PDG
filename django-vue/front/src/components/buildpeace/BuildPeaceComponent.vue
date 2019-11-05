<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <v-container  class="fill-height" style="min-height: 100%">
        <!--INITIAL IMAGE -->
        <v-row>
          <v-col cols="7">
            <br />
            <h1>¡Construyamos Paz!</h1>
            <br />
            <br />
            <p>Para el Observatorio de Paz y Cultura Ciudadana es de vital importancia conocer la percepción de paz de los ciudadanos con el fin de aportar información valiosa para las campañas en curso de proyectos alineados a la construcción de paz y cultura ciudadana.
              ¡Ayudános a construir más paz!
            </p>
            <br />
            <br />
          </v-col>
        </v-row>
      </v-container>
    </div>

    <v-container>
      <!-- ACTIVE CAMPAIGN -->
      <v-container style="padding-top: 20vh;">>
        <v-row justify="center">
          <v-col cols="5">
            <div class="form-group">
              <p for="campaign">Selecciona la campaña en la que deseas participar</p>
              <v-select
                :items="campaigns"
                :error-messages="campaignErrors"
                item-text="title"
                item-value="title"
                outlined
                v-model="campaign"
                return-object
                required
                class="input"
                color="#0C186D"
                name="campaign"
                @change="$v.campaign.$touch()"
              ></v-select>
            </div>
          </v-col>
        </v-row>
      </v-container>
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
                <personal-form-component v-on:allToParent="allFromPersonalChildClick"></personal-form-component>
              </v-stepper-content>

              <v-stepper-content step="2">
                <territory-form-component
                  v-on:allToParent="allFromTerritoryChildClick"
                  v-on:before="beforeTerritory"
                ></territory-form-component>
              </v-stepper-content>

              <v-stepper-content step="3">
                <education-form-component
                  v-on:allToParent="allFromEducationChildClick"
                  v-on:before="beforeEducation"
                ></education-form-component>
              </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-col>
      </v-row>

      <!-- NARRATIVE -->
      <v-row align="center" justify="center" style="padding-top: 10vh;">>
        <v-col cols="8">
          <h3>Con un texto ayudanos a responder la pregunta:</h3>
          <br />
          <div id="text" class="form-group">
            <label for="narrative">Para ti, ¿Qué si es paz?</label>
            <v-textarea
              v-model="narrative"
              :error-messages="narrativeErrors"
              outlined
              name="narrative"
              counter="500"
              color="#0C186D"
              class="input"
              @input="$v.narrative.$touch()"
            ></v-textarea>
          </div>
        </v-col>
      </v-row>

      <!--KEYWORDS -->
      <v-row align="center" justify="center" style="padding-top: 10vh;">
        <v-col cols="8">
          <h3>Dinos 5 palabras que para ti reflejen Qué si es paz</h3>
        </v-col>
      </v-row>

      <v-row align="center" justify="space-between">
        <v-col cols="2">
          <v-text-field
            v-model="word1"
            :error-messages="word1Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word1"
            class="input"
            @input="$v.word1.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word2"
            :error-messages="word2Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word2"
            class="input"
            @input="$v.word2.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word3"
            :error-messages="word3Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word3"
            class="input"
            @input="$v.word3.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word4"
            :error-messages="word4Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word4"
            class="input"
            @input="$v.word4.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="2">
          <v-text-field
            v-model="word5"
            :error-messages="word5Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word5"
            class="input"
            @input="$v.word5.$touch()"
          ></v-text-field>
        </v-col>
      </v-row>


      <v-row align="center" justify="center">
        <v-col cols="2">
         <div v-if="submitStatus!=''" class="pa-5 alert alert-danger" role="alert">
          Revisa las advertencias. Tienes algún error en los campos
      </div>
        </v-col>

        <v-col cols="5">
          <v-checkbox
          v-model="checkbox"
          label="¿Deseas guardar tus datos para una próxima ocasión?"
          @change="check($event)"
        ></v-checkbox>
        </v-col>
        <v-col cols="4">
          <v-btn v-if="checkbox==false" :ripple="false" class="ma-2 save" color="#673ab7" dark @click="saveData">Finalizar</v-btn>

          <v-dialog v-model="dialog" persistent max-width="400px" v-bind:scrollable="scroll">
          <template v-slot:activator="{ on }">
            <v-btn  v-if="checkbox" :ripple="false" class="ma-2 save" color="#673ab7" v-on="on" dark>Crea tu cuenta</v-btn>
            <!--<v-btn color="primary" dark v-on="on">Open Dialog</v-btn>-->
          </template>
          <v-card>
            <v-toolbar dark color="#0C186D">
              <v-btn icon dark @click="dialog = false">
                <v-icon>mdi-close</v-icon>
              </v-btn>
               <v-toolbar-title>Crear cuenta</v-toolbar-title>
            </v-toolbar>
            <register-component :dialog="dialog"> </register-component>
          </v-card>
        </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import api from "../../axios.js";
import { required, minLength, maxLength } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";

function differents(word) {
  if (word == this.word1) {
    return (
      word != this.word2 &&
      word != this.word3 &&
      word != this.word4 &&
      word != this.word5
    );
  }
  if (word == this.word2) {
    return (
      word != this.word1 &&
      word != this.word3 &&
      word != this.word4 &&
      word != this.word5
    );
  }
  if (word == this.word3) {
    return (
      word != this.word1 &&
      word != this.word2 &&
      word != this.word4 &&
      word != this.word5
    );
  }
  if (word == this.word4) {
    return (
      word != this.word1 &&
      word != this.word2 &&
      word != this.word3 &&
      word != this.word5
    );
  }
  if (word == this.word5) {
    return (
      word != this.word1 &&
      word != this.word2 &&
      word != this.word3 &&
      word != this.word4
    );
  }
}
export default {
  name: "BuildPeace",
  mixins: [validationMixin],

  validations: {
    narrative: { required, minLength: minLength(3), maxLength: maxLength(500) },
    word1: { required, minLength: minLength(3), differents },
    word2: { required, minLength: minLength(3), differents },
    word3: { required, minLength: minLength(3), differents },
    word4: { required, minLength: minLength(3), differents },
    word5: { required, minLength: minLength(3), differents },
    campaign : { title: {required} }
  },
  data() {
    return {
      e1: 0,
      narrative: "",
      word1: "",
      word2: "",
      word3: "",
      word4: "",
      word5: "",
      campaign: {id: 0, title:''},
      campaigns: [],
      submitStatus: "",
      dialog: false,
      scroll: false, 
      checkbox: false,
      //PERSONAL COMPONENT
      age: 0,
      gender: {id: 0, name:''},
      name: "",
      lastname: "",
      //EDUCATION COMPONENT
      level: {id: 0, name:''},
      higherEducation: {id: 0, name:''},
      //TERRITORY COMPONENT
      currentZone: {id: 0, name:''},
      currentState: {id: 0, name:''},
      currentCity: {id: 0, name:''},
      currentComuna: {id: 0, name:''},
      currentNeighborhood: {id: 0, name:''},
      currentCorregimiento: {id: 0, name:''},
      currentVereda: {id: 0, name:''},
      originZone: {id: 0, name:''},
      originState: {id: 0, name:''},
      originCity: {id: 0, name:''},
      originComuna: {id: 0, name:''},
      originNeighborhood: {id: 0, name:''},
      originCorregimiento: {id: 0, name:''},
      originVereda: {id: 0, name:''}
    };
  },
  created() {
    api
      .getActiveCampaigns()
      .then(response => {
        this.campaigns = response;
      })
      .catch(err => console.log(err));
  },
  methods: {
    //PROPS FROM CHILDREN
    //Personal
    allFromPersonalChildClick(value) {
      this.age = value[0];
      this.gender = value[1];
      this.name = value[2];
      this.lastname = value[3];
      this.e1 = parseInt(value[4]);
    },
    //Education
    allFromEducationChildClick(value) {
      this.higherEducation = value[0];
      this.level = value[1];
    },
    beforeEducation(value) {
      this.e1 = value;
    },
    //Territory
    allFromTerritoryChildClick(value) {
      this.currentZone = value[0];
      this.currentState = value[1];
      this.currentCity = value[2];
      this.currentComuna = value[3];
      this.currentNeighborhood = value[4];
      this.currentCorregimiento = value[5];
      this.currentVereda = value[6];
      this.originZone = value[7];
      this.originState = value[8];
      this.originCity = value[9];
      this.originComuna = value[10];
      this.originNeighborhood = value[11];
      this.originCorregimiento = value[12];
      this.originVereda = value[13];
      this.e1 = parseInt(value[14]);
    },
    beforeTerritory(value) {
      this.e1 = value;
    },
    logout(){
      this.$store
        .dispatch("logout")
        .then((resp) => {
          this.$router.push("/profile")
        })
        .catch(err => {
          console.log(err);
        });
    },

    //REAL HANDLE OF METHODS
    saveData() {
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Error"
      }else{
        this.submitStatus = ""
        let data = {
        campaign : this.campaign.id,
        age: this.age,
        gender: this.gender.id,
        name: this.name,
        lastname: this.lastname,
        level: this.level.id,
        higherEducation: this.higherEducation.id,
        currentZone: this.currentZone.id,
        currentState: this.currentState.id,
        currentCity: this.currentCity.id,
        currentComuna: this.currentComuna.id,
        currentNeighborhood: this.currentNeighborhood.id,
        currentCorregimiento: this.currentCorregimiento.id,
        currentVereda: this.currentVereda.id,
        originZone: this.originZone.id,
        originState: this.originState.id,
        originCity: this.originCity.id,
        originComuna: this.originComuna.id,
        originNeighborhood: this.originNeighborhood.id,
        originCorregimiento: this.originCorregimiento.id,
        originVereda: this.originVereda.id,
        narrative: this.narrative,
        word1: this.word1,
        word2: this.word2,
        word3: this.word3,
        word4: this.word4,
        word5: this.word5
      };
      console.log(data)
     // api.saveData(data);
      }
      
    }
  },
  computed: {
    campaignErrors() {
      const errors = [];
      if (!this.$v.campaign.$dirty) return errors;
      !this.$v.campaign.title.required && errors.push("La campaña es requerida.");
      return errors;
    },
    narrativeErrors() {
      const errors = [];
      if (!this.$v.narrative.$dirty) return errors;
      !this.$v.narrative.minLength &&
        errors.push("La narrative debe tener mínimo 3 caracteres");
      !this.$v.narrative.required && errors.push("La narrativa es requerida.");
      !this.$v.narrative.maxLength &&
        errors.push("La narrativa debe tener máximo 500 caracteres.");
      return errors;
    },
    word1Errors() {
      const errors = [];
      if (!this.$v.word1.$dirty) return errors;
      !this.$v.word1.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word1.required && errors.push("La palabra es requerida.");
      !this.$v.word1.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word2Errors() {
      const errors = [];
      if (!this.$v.word2.$dirty) return errors;
      !this.$v.word2.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word2.required && errors.push("La palabra es requerida.");
      !this.$v.word2.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word3Errors() {
      const errors = [];
      if (!this.$v.word3.$dirty) return errors;
      !this.$v.word3.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word3.required && errors.push("La palabra es requerida.");
      !this.$v.word3.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word4Errors() {
      const errors = [];
      if (!this.$v.word4.$dirty) return errors;
      !this.$v.word4.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word4.required && errors.push("La palabra es requerida.");
      !this.$v.word4.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word5Errors() {
      const errors = [];
      if (!this.$v.word5.$dirty) return errors;
      !this.$v.word5.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word5.required && errors.push("La palabra es requerida.");
      !this.$v.word5.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
body {
  background-color: #ffffff;
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
