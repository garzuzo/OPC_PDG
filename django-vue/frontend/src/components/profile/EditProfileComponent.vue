<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12" md="8">
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
            <!--PERSONAL -->
            <v-stepper-content step="1">
              <v-container>
                <v-row>
                  <v-col cols="8" sm="8" md="5">
                    <div class="form-group">
                      <label for="gender">Sexo*</label>
                      <v-select
                        :items="genders"
                        item-text="typeGender"
                        item-value="typeGender"
                        outlined
                        v-model="gender"
                        :error-messages="genderErrors"
                        required
                        return-object
                        class="input"
                        color="#0C186D"
                        @change="$v.gender.$touch()"
                      ></v-select>
                    </div>
                  </v-col>
                </v-row>
                <v-container>
                  <div
                    v-if="submitStatus!=''"
                    class="pa-5 alert alert-danger"
                    role="alert"
                  >Revisa las advertencias. Tienes algún error en los campos</div>
                  <v-row justify="end">
                    <v-col cols="4" sm="4" md="2">
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outlined
                        color="#673ab7"
                        @click="checkPersonal"
                      >Siguiente</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-container>
            </v-stepper-content>

            <!--TERRITORY -->
            <v-stepper-content step="2">
              <v-container>
                <div>
                  <h3>Territorio donde vives</h3>
                  <v-row justify="space-around">
                    <!--FIRST COLUMN-->

                    <v-col cols="6" sm="6" md="5">
                      <div class="form-group">
                        <label for="currentZone">Zona*</label>
                        <v-select
                          :items="zones"
                          item-text="zoneType"
                          item-value="zoneType"
                          outlined
                          v-model="currentZone"
                          return-object
                          :error-messages="currentZoneErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentZone"
                          @change="$v.currentZone.$touch()"
                        ></v-select>
                      </div>

                      <div class="form-group">
                        <label for="currentState">Departamento*</label>
                        <v-select
                          :items="states"
                          item-text="name"
                          item-value="name"
                          outlined
                          v-model="currentState"
                          return-object
                          :error-messages="currentStateErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentState"
                          @change="$v.currentState.$touch()"
                        ></v-select>
                      </div>

                      <div
                        class="form-group"
                        v-if="currentZone.zoneType == zones[1].zoneType & currentCity.name == 'Cali'"
                      >
                        <label for="currentComuna">Comuna*</label>
                        <v-select
                          :items="comunasCali"
                          item-text="name"
                          item-value="name"
                          outlined
                          v-model="currentComuna"
                          return-object
                          :error-messages="currentComunaErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentComuna"
                          @change="$v.currentComuna.$touch()"
                        ></v-select>
                      </div>

                      <div
                        class="form-group"
                        v-if="currentZone.zoneType == zones[0].zoneType & currentCity.name == 'Cali'"
                      >
                        <label for="currentCorregimiento">Corregimiento*</label>
                        <v-select
                          :items="corregimientosCali"
                          item-text="name"
                          item-value="name"
                          outlined
                          v-model="currentCorregimiento"
                          return-object
                          :error-messages="currentCorregimientoErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentCorregimiento"
                          @change="$v.currentCorregimiento.$touch()"
                        ></v-select>
                      </div>
                    </v-col>

                    <!--SECOND COLUMN -->
                    <v-col align-self="end" cols="6" sm="6" md="5">
                      <div class="form-group">
                        <label for="currentCity">Municipio*</label>
                        <v-select
                          :items="currentCities"
                          item-text="name"
                          item-value="name"
                          outlined
                          v-model="currentCity"
                          :value="currentCity"
                          return-object
                          :error-messages="currentCityErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentCity"
                          @change="$v.currentCity.$touch()"
                        ></v-select>
                      </div>

                      <div
                        class="form-group"
                        v-if="currentZone.zoneType == zones[1].zoneType & currentCity.name == 'Cali'"
                      >
                        <label for="currentNeighborhood">Barrio*</label>
                        <v-select
                          :items="currentNeighborhoodsCali"
                          item-text="name"
                          item-value="name"
                          outlined
                          v-model="currentNeighborhood"
                          return-object
                          :error-messages="currentNeighborhoodErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentNeighborhood"
                          @change="$v.currentNeighborhood.$touch()"
                        ></v-select>
                      </div>

                      <div
                        class="form-group"
                        v-if="currentZone.zoneType == zones[0].zoneType & currentCity.name == 'Cali'"
                      >
                        <label for="currentVereda">Vereda*</label>
                        <v-select
                          :items="currentVeredasCali"
                          item-text="name"
                          item-value="name"
                          outlined
                          v-model="currentVereda"
                          return-object
                          :error-messages="currentVeredaErrors"
                          required
                          class="input"
                          color="#0C186D"
                          name="currentVereda"
                          @change="$v.currentVereda.$touch()"
                        ></v-select>
                      </div>
                    </v-col>
                  </v-row>

                  <v-container>
                    <div
                      v-if="submitStatus!=''"
                      class="pa-5 alert alert-danger"
                      role="alert"
                    >Revisa las advertencias. Tienes algún error en los campos</div>
                    <v-row justify="space-between">
                      <v-col cols="4" sm="4" md="2">
                        <v-btn
                          :ripple="false"
                          class="ma-2 next"
                          outlined
                          color="#673ab7"
                          @click="beforeTerritory"
                        >Anterior</v-btn>
                      </v-col>
                      <v-col cols="4" sm="4" md="2">
                        <v-btn
                          :ripple="false"
                          class="ma-2 next"
                          outlined
                          color="#673ab7"
                          @click="checkTerritory"
                        >Siguiente</v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
                </div>
              </v-container>
            </v-stepper-content>

            <!--EDUCACIÓN -->
            <v-stepper-content step="3">
              <div>
                <v-col cols="12" sm="12" md="5">
                  <div class="form-group">
                    <label for="higherEducation">Nivel educativo más alto alcanzado*</label>
                    <v-select
                      :items="education"
                      :error-messages="higherEducationErrors"
                      item-text="name"
                      item-value="name"
                      outlined
                      v-model="higherEducation"
                      return-object
                      required
                      class="input"
                      color="#0C186D"
                      name="higherEducation"
                      @change="$v.higherEducation.$touch()"
                    ></v-select>
                  </div>

                  <div class="form-group">
                    <label for="level">Nivel más alto alcanzado en el anterior nivel*</label>
                    <v-select
                      :items="levels"
                      :error-messages="levelErrors"
                      item-text="name"
                      item-value="name"
                      outlined
                      v-model="level"
                      return-object
                      required
                      class="input"
                      color="#0C186D"
                      name="level"
                      @change="$v.level.$touch()"
                    ></v-select>
                  </div>
                </v-col>
                <v-container>
                  <div
                    v-if="submitStatus!=''"
                    class="px-5 alert alert-danger"
                    role="alert"
                  >Revisa las advertencias. Tienes algún error en los campos</div>
                  <div
                    v-if="succes!=''"
                    class="px-5 alert alert-success"
                    role="alert"
                  >{{succes}}</div>
                  <v-row justify="space-between">
                    <v-col cols="4" sm="4" md="2">
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outlined
                        color="#673ab7"
                        @click="beforeEducation"
                      >Anterior</v-btn>
                    </v-col>

                    <v-col cols="4" sm="4" md="2">
                      <v-btn
                        :ripple="false"
                        class="ma-2 next"
                        outlined
                        color="#673ab7"
                        @click="editProfile"
                      >Finalizar</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </div>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from "../../axios.js";
import {
  required,
  minLength,
  minValue,
  requiredIf
} from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";

export default {
  mixins: [validationMixin],

  validations: {
    //PERSONAL
    gender: { typeGender: { required } },
    //TERRITORY
    currentZone: { zoneType: { required } },
    currentState: { name: { required } },
    currentCity: { name: { required } },
    currentComuna: {
      name: {
        required: requiredIf(function() {
          return (
            this.currentZone.zoneType == "Urbana" &&
            this.currentCity.name == "Cali"
          );
        })
      }
    },
    currentNeighborhood: {
      name: {
        required: requiredIf(function() {
          return (
            this.currentZone.zoneType == "Urbana" &&
            this.currentCity.name == "Cali"
          );
        })
      }
    },
    currentCorregimiento: {
      name: {
        required: requiredIf(function() {
          return (
            this.currentZone.zoneType == "Rural" &&
            this.currentCity.name == "Cali"
          );
        })
      }
    },
    currentVereda: {
      name: {
        required: requiredIf(function() {
          return (
            this.currentZone.zoneType == "Rural" &&
            this.currentCity.name == "Cali"
          );
        })
      }
    },
    //EDUCATION
    higherEducation: {name: {required}},
    level : {name: {required}}
  },
  props: {
    profile: Object
  },
  data() {
    return {
      e1: 0,
      gender: this.profile.gender,
      higherEducation: this.profile.higherEducation,
      level: this.profile.level,
      currentZone: this.profile.currentZone,
      currentState: this.profile.currentState,
      currentCity: this.profile.currentCity,
      currentComuna:  this.profile.currentComuna,
      currentNeighborhood: this.profile.currentNeighborhood,
      currentCorregimiento: this.profile.currentCorregimiento ,
      currentVereda: this.profile.currentVereda,
      submitStatus: "",
      succes: "",
      genders: [],
      zones: ['Rural', 'Urbana'],
      currentCities: [],
      currentNeighborhoodsCali: [],
      currentVeredasCali: [],
      states: [],
      comunasCali: [],
      corregimientosCali: [],

      education: [],
      levels: [],
      neighborhoodVereda: 0,
      city: 0
    };
  },
  created() {
    api
      .getGender()
      .then(response => {
        this.genders = response;
        console.log(this.genders);
      })
      .catch(err => console.log(err));

    api
      .getZones()
      .then(response => {
        this.zones = response;
        console.log(response);
      })
      .catch(err => console.log(err));

    api
      .getStates("COLOMBIA")
      .then(response => {
        this.states = response;
      })
      .catch(err => console.log(err));

    let dataComuna = ["Cali", "Urbana"];
    api
      .getCorregimientosComunas(dataComuna)
      .then(response => {
        this.comunasCali = response;
      })
      .catch(err => {
        console.log(err);
      });

    let dataCorregimiento = ["Cali", "Rural"];
    api
      .getCorregimientosComunas(dataCorregimiento)
      .then(response => {
        this.corregimientosCali = response;
      })
      .catch(err => {
        console.log(err);
      });

      api
      .getLevelsEducation()
      .then(response => {
        this.education = response;
      })
      .catch(err => {
        console.log(err);
      });

      //init watch
      api
          .getCities(this.currentState.name)
          .then(response => {
            this.currentCities = response;
          })
          .catch(err => {
            console.log(err);
          });

      let dataComunaN = ["Cali", "Urbana", this.currentComuna.name];
        api
          .getNeighborhoodsVeredas(dataComunaN)
          .then(response => {
            this.currentNeighborhoodsCali = response;
          })
          .catch(err => console.log(err));
      let dataCorregimientoN = ["Cali", "Rural", this.currentCorregimiento.name];
        api
          .getNeighborhoodsVeredas(dataCorregimientoN)
          .then(response => {
            this.currentVeredasCali = response;
          })
          .catch(err => console.log(err));

         api
        .getAchievedLevel(this.higherEducation.name)
        .then(response => {
          this.levels = response;
        })
        .catch(err => {
          console.log(err);
        }); 
  },
  watch:{
    //CURRENT
    currentState(state){
      api
          .getCities(this.currentState.name)
          .then(response => {
            this.currentCities = response;
          })
          .catch(err => {
            console.log(err);
          });
    },
    currentComuna(comuna){
      let dataComuna = ["Cali", "Urbana", this.currentComuna.name];
        api
          .getNeighborhoodsVeredas(dataComuna)
          .then(response => {
            this.currentNeighborhoodsCali = response;
          })
          .catch(err => console.log(err));
    },
    currentCorregimiento(corregimiento){
      let dataCorregimiento = ["Cali", "Rural", this.currentCorregimiento.name];
        api
          .getNeighborhoodsVeredas(dataCorregimiento)
          .then(response => {
            this.currentVeredasCali = response;
          })
          .catch(err => console.log(err));
    },
    higherEducation(education){
        api
        .getAchievedLevel(this.higherEducation.name)
        .then(response => {
          this.levels = response;
        })
        .catch(err => {
          console.log(err);
        });
    }
  },  
  methods: {
    checkPersonal() {
      this.$v.$touch();
      if (this.$v.gender.$error) {
        this.submitStatus = "Error";
      } else {
        this.submitStatus = "";
        this.e1 = 2;
      }
    },
    beforeTerritory() {
      this.e1 = 1;
    },
    checkTerritory() {
      this.$v.$touch();
      if (
        this.$v.currentZone.$error ||
        this.$v.currentState.$error ||
        this.$v.currentCity.$error ||
        this.$v.currentComuna.$error ||
        this.$v.currentNeighborhood.$error ||
        this.$v.currentCorregimiento.$error ||
        this.$v.currentVereda.$error
      ) {
        this.submitStatus = "Error";
      } else {
        this.submitStatus = "";
        this.e1 = 3;
      }
    },
    beforeEducation(){
      this.e1 = 2
    },
    editProfile(){
      this.$v.$touch();
      if (
        this.$v.higherEducation.$error ||
        this.$v.level.$error
      ) {
        this.submitStatus = "Error";
        this.succes = ""
      } else {
        this.submitStatus = "";
        this.succes = ""
        if(this.currentZone.zoneType== "Urbana" && this.currentCity.name=="Cali"){
          this.neighborhoodVereda = this.currentNeighborhood.id
          this.currentCity.id = 0
        }
        else if(this.currentZone.zoneType == "Rural" && this.currentCity.name=="Cali"){
          this.neighborhoodVereda = this.currentVereda.id
          this.currentCity.id = 0
        }
        else if (this.currentCity.name!="Cali"){
          this.neighborhoodVereda = 0
        }

        let data= {
          achievedLevel : this.level.id,
          neighborhoodVeredaActual: this.neighborhoodVereda,
          cityActual : this.currentCity.id
        }
        api.editProfile(data).then(response=>{
          this.succes= "Tu perfil se actualizó correctamente."
          this.$emit("allToParent", data)
        }).catch(err=>console.log(err))
      }
    }
  },
  computed: {
    //PERSONAL
    genderErrors() {
      const errors = [];
      if (!this.$v.gender.$dirty) return errors;
      !this.$v.gender.typeGender.required &&
        errors.push("Genero es requerido.");
      return errors;
    },
    //TERRITORY
    currentZoneErrors() {
      const errors = [];
      if (!this.$v.currentZone.$dirty) return errors;
      !this.$v.currentZone.zoneType.required &&
        errors.push("Zona actual es requerido.");
      return errors;
    },
    currentStateErrors() {
      const errors = [];
      if (!this.$v.currentState.$dirty) return errors;
      !this.$v.currentState.name.required &&
        errors.push("Departamento actual es requerido.");
      return errors;
    },
    currentCityErrors() {
      const errors = [];
      if (!this.$v.currentCity.$dirty) return errors;
      !this.$v.currentCity.name.required &&
        errors.push("Ciudad actual es requerido.");
      return errors;
    },
    currentComunaErrors() {
      const errors = [];
      if (!this.$v.currentComuna.$dirty) return errors;
      !this.$v.currentComuna.name.required &&
        errors.push("Comuna actual es requerido.");

      return errors;
    },
    currentNeighborhoodErrors() {
      const errors = [];
      if (!this.$v.currentNeighborhood.$dirty) return errors;
      !this.$v.currentNeighborhood.name.required &&
        errors.push("Barrio actual es requerido.");

      return errors;
    },
    currentCorregimientoErrors() {
      const errors = [];
      if (!this.$v.currentCorregimiento.$dirty) return errors;
      !this.$v.currentCorregimiento.name.required &&
        errors.push("Corregimiento actual es requerido.");
      return errors;
    },
    currentVeredaErrors() {
      const errors = [];
      if (!this.$v.currentVereda.$dirty) return errors;
      !this.$v.currentVereda.name.required &&
        errors.push("Vereda actual es requerido.");

      return errors;
    },
    //EDUCATION
    higherEducationErrors(){
      const errors = []
        if (!this.$v.higherEducation.$dirty) return errors
        !this.$v.higherEducation.name.required && errors.push('Nivel más alto alcanzado es requerido.')
        return errors
    },
    levelErrors(){
      const errors = []
        if (!this.$v.level.$dirty) return errors
        !this.$v.level.name.required && errors.push('Nivel alcanzado en el anterior nivel es requerido.')
        return errors
    }
  }
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
h3 {
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  text-align: center;
}

.input {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 36px;
}

label {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
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
</style>