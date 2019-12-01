<template>
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

        <div class="form-group" v-bind:v-if="currentZone.zoneType == zones[1].zoneType & currentCity.name == 'Cali'">
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

        <div class="form-group"  v-bind:v-if="currentZone.zoneType == zones[0].zoneType & currentCity.name == 'Cali'">
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
            return-object
            :error-messages="currentCityErrors"
            required
            class="input"
            color="#0C186D"
            name="currentCity"
            @change="$v.currentCity.$touch()"
          ></v-select>
        </div>

        <div class="form-group"  v-bind:v-if="currentZone.zoneType == zones[1].zoneType & currentCity.name == 'Cali'">
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

        <div class="form-group"  v-bind:v-if="currentZone.zoneType == zones[0].zoneType & currentCity.name == 'Cali'">
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
    <v-divider> </v-divider>
    <v-row justify="center">
      <v-col cols="12" sm="12" md="8">
        <h3>Territorio de origen</h3>
        <v-checkbox
          v-model="checkbox"
          label="¿Tu territorio de origen es igual al territorio donde vives?"
          @change="check($event)"
        ></v-checkbox>
      </v-col>
    </v-row>
    <!--ORIGIN TERRITORY -->
    <v-row justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="6" sm="6" md="5">
        <div class="form-group">
          <label for="originZone">Zona*</label>
          <v-select
            :items="zones"
            item-text="zoneType"
            item-value="zoneType"
            outlined
            v-bind:disabled="disabled"
            v-model="originZone"
            return-object
            :error-messages="originZoneErrors"
            required
            class="input"
            color="#0C186D"
            name="originZone"
            @change="$v.originZone.$touch()"
          ></v-select>
        </div>

        <div class="form-group">
          <label for="originState">Departamento*</label>
          <v-select
            :items="states"
            item-text="name"
            item-value="name"
            outlined
            v-bind:disabled="disabled"
            v-model="originState"
            return-object
            :error-messages="originStateErrors"
            required
            class="input"
            color="#0C186D"
            name="originState"
            @change="$v.originState.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone.zoneType == zones[1].zoneType & originCity.name == 'Cali'">
          <label for="originComuna">Comuna*</label>
          <v-select
            :items="comunasCali"
            item-text="name"
            item-value="name"
            outlined
            v-bind:disabled="disabled"
            v-model="originComuna"
            return-object
            :error-messages="originComunaErrors"
            required
            class="input"
            color="#0C186D"
            name="originComuna"
            @change="$v.originComuna.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone.zoneType == zones[0].zoneType & originCity.name == 'Cali'">
          <label for="originCorregimiento">Corregimiento*</label>
          <v-select
            :items="corregimientosCali"
            item-text="name"
            item-value="name"
            outlined
            v-bind:disabled="disabled"
            v-model="originCorregimiento"
            return-object
            :error-messages="originCorregimientoErrors"
            required
            class="input"
            color="#0C186D"
            name="originCorregimiento"
            @change="$v.originCorregimiento.$touch()"
          ></v-select>
        </div>
      </v-col>

      <!--SECOND COLUMN -->
      <v-col align-self="end" cols="6" sm="6" md="5">
        <div class="form-group">
          <label for="originCity">Municipio*</label>
          <v-select
            :items="originCities"
            item-text="name"
            item-value="name"
            outlined
            v-bind:disabled="disabled"
            v-model="originCity"
            return-object
            :error-messages="originCityErrors"
            required
            class="input"
            color="#0C186D"
            name="originCity"
            @change="$v.originCity.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone.zoneType == zones[1].zoneType & originCity.name == 'Cali'">
          <label for="originNeighborhood">Barrio*</label>
          <v-select
            :items="originNeighborhoodsCali"
            item-text="name"
            item-value="name"
            outlined
            v-bind:disabled="disabled"
            v-model="originNeighborhood"
            return-object
            :error-messages="originNeighborhoodErrors"
            required
            class="input"
            color="#0C186D"
            name="originNeighborhood"
            @change="$v.originNeighborhood.$touch()"
          ></v-select>
        </div>
        
        <div class="form-group" v-if="originZone.zoneType == zones[0].zoneType & originCity.name == 'Cali'">
          <label for="originVereda">Vereda*</label>
          <v-select
            :items="originVeredasCali"
            item-text="name"
            item-value="name"
            outlined
            v-bind:disabled="disabled"
            v-model="originVereda"
            return-object
            :error-messages="originVeredaErrors"
            required
            class="input"
            color="#0C186D"
            name="originVereda"
            @change="$v.originVereda.$touch()"
          ></v-select>
        </div>
      </v-col>
    </v-row>

    <v-container>
      <div v-if="submitStatus!=''" class="pa-5 alert alert-danger" role="alert">
          {{submitStatus}}
      </div>
      <v-row justify="space-between">
        <v-col cols="4" sm="3" md="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitBeforeToParent"
          >Anterior</v-btn>
        </v-col>
        <v-col cols="4" sm="3" md="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitAllToParent"
          >Siguiente</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import api from "../../axios.js";
import { required, requiredIf} from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";

export default {
  //name: "PersonalForm",
  mixins: [validationMixin],

  
  validations: {
    currentZone: {zoneType: {required}},
    currentState: {name: {required}},
    currentCity: {name: {required}},
    currentComuna: {name: {
      required: requiredIf(function () {
        return this.currentZone.zoneType=="Urbana" && this.currentCity.name == "Cali"
      })
    }},
    currentNeighborhood: {name: {
      required: requiredIf(function () {
        return this.currentZone.zoneType=="Urbana" && this.currentCity.name == "Cali"
      })
    }},
    currentCorregimiento: {name: {
      required: requiredIf(function () {
        return this.currentZone.zoneType=="Rural" && this.currentCity.name == "Cali"
      })
    }},
    currentVereda: {name: {
      required: requiredIf(function () {
        return this.currentZone.zoneType=="Rural" && this.currentCity.name == "Cali"
      })
    }},
    originZone: {zoneType: {required}},
    originState: {name: {required}},
    originCity: {name: {required}},
    originComuna: {name: {
      required: requiredIf(function () {
        return this.originZone.zoneType=="Urbana" && this.originCity.name == "Cali"
      })
    }},
    originNeighborhood: {name: {
      required: requiredIf(function () {
        return this.originZone.zoneType=="Urbana" && this.originCity.name == "Cali"
      })
    }},
    originCorregimiento: {name: {
      required: requiredIf(function () {
        return this.originZone.zoneType=="Rural" && this.originCity.name == "Cali"
      })
    }},
    originVereda: {name: {
      required: requiredIf(function () {
        return this.originZone.zoneType=="Rural" && this.originCity.name == "Cali"
      })
    }}
  },
  data() {
    return {
      currentZone: { id: 0, zoneType: '' },
      currentState: { id: 0, name: '' },
      currentCity: { id: 0, name: '' },
      currentComuna: { id: 0, name: '' },
      currentNeighborhood: { id: 0, name: '' },
      currentCorregimiento: { id: 0, name: '' },
      currentVereda: { id: 0, name: '' },
      originZone: { id: 0, zoneType: '' },
      originState: { id: 0, name: '' },
      originCity: { id: 0, name: '' },
      originComuna: { id: 0, name: '' },
      originNeighborhood: { id: 0, name: '' },
      originCorregimiento: { id: 0, name: '' },
      originVereda: { id: 0, name: '' },
      zones: ['Rural', 'Urbana'],
      currentCities: [],
      originCities: [],

      currentNeighborhoodsCali: [],
      currentVeredasCali: [],

      originNeighborhoodsCali: [],
      originVeredasCali: [],
      
      states: [],
      comunasCali: [],
      corregimientosCali: [],
      /*neighborhoodsCali: [],
      corregimientosCali: [],
      origNeighborhoodsCali: [],
      veredasCali: [],
      origVeredasCali: [],
      currentCitiesComputed: [],
      originCitiesComputed: [],*/
      checkbox: false,
      submitStatus: "",
      disabled : false
    };
  },
  created() {
     api.getZones().then(response => {
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
    //ORIGIN
    originState(state){
      api
          .getCities(this.originState.name)
          .then(response => {
            this.originCities = response;
          })
          .catch(err => {
            console.log(err);
          });
    },
    originComuna(comuna){
      let dataComuna = ["Cali", "Urbana", this.originComuna.name];
        api
          .getNeighborhoodsVeredas(dataComuna)
          .then(response => {
            this.originNeighborhoodsCali = response;
          })
          .catch(err => console.log(err));
    },
    originCorregimiento(corregimiento){
      let dataCorregimiento = ["Cali", "Rural", this.originCorregimiento.name];
        api
          .getNeighborhoodsVeredas(dataCorregimiento)
          .then(response => {
            this.origVeredasCali = response;
          })
          .catch(err => console.log(err));
    }
  },
  computed: {
    /*currentCities() {
      if (this.currentState.name != "") {
        api
          .getCities(this.currentState.name)
          .then(response => {
            this.currentCitiesComputed = response;
          })
          .catch(err => {
            console.log(err);
          });
      }
      return this.currentCitiesComputed;
    },
    originCities() {
      if (this.originState.name != "") {
        api
          .getCities(this.originState.name)
          .then(response => {
            this.originCitiesComputed = response;
          })
          .catch(err => {
            console.log(err);
          });
      }
      return this.originCitiesComputed;
    },
    currentNeighborhoodsCali() {
      if (this.currentComuna.name != "") {
        let dataComuna = ["Cali", "Urbana", this.currentComuna.name];
        api
          .getNeighborhoodsVeredas(dataComuna)
          .then(response => {
            this.neighborhoodsCali = response;
          })
          .catch(err => console.log(err));
      }
      return this.neighborhoodsCali;
    },
    originNeighborhoodsCali() {
      if (this.originComuna.name != "") {
        let dataComuna = ["Cali", "Urbana", this.originComuna.name];
        api
          .getNeighborhoodsVeredas(dataComuna)
          .then(response => {
            this.origNeighborhoodsCali = response;
          })
          .catch(err => console.log(err));
      }
      return this.origNeighborhoodsCali;
    },
    currentVeredasCali() {
      if (this.currentCorregimiento.name != "") {
        let dataCorregimiento = ["Cali", "Rural", this.currentCorregimiento.name];
        api
          .getNeighborhoodsVeredas(dataCorregimiento)
          .then(response => {
            this.veredasCali = response;
          })
          .catch(err => console.log(err));
      }
      return this.veredasCali;
    },
    originVeredasCali() {
      if (this.originCorregimiento.name != "") {
        let dataCorregimiento = ["Cali", "Rural", this.originCorregimiento.name];
        api
          .getNeighborhoodsVeredas(dataCorregimiento)
          .then(response => {
            this.origVeredasCali = response;
          })
          .catch(err => console.log(err));
      }
      return this.origVeredasCali;
    },*/
    currentZoneErrors() {
      const errors = [];
      if (!this.$v.currentZone.$dirty) return errors;
      !this.$v.currentZone.zoneType.required && errors.push("Zona actual es requerido.");
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
    originZoneErrors() {
      const errors = [];
      if (!this.$v.originZone.$dirty) return errors;
      !this.$v.originZone.zoneType.required &&
        errors.push("Zona de origen es requerido.");
      return errors;
    },
    originStateErrors() {
      const errors = [];
      if (!this.$v.originState.$dirty) return errors;
      !this.$v.originState.name.required &&
        errors.push("Departamento de origen es requerido.");
      return errors;
    },
    originCityErrors() {
      const errors = [];
      if (!this.$v.originCity.$dirty) return errors;
      !this.$v.originCity.name.required &&
        errors.push("Ciudad de origen es requerido.");
      return errors;
    },
    originComunaErrors() {
      const errors = [];
      if (!this.$v.originComuna.$dirty) return errors;
      !this.$v.originComuna.name.required &&
        errors.push("Comuna de origen es requerido.");
       
      return errors;
    },
    originNeighborhoodErrors() {
      const errors = [];
      if (!this.$v.originNeighborhood.$dirty) return errors;
      !this.$v.originNeighborhood.name.required &&
        errors.push("Barrio de origen es requerido.");

      
      return errors;
    },
    originCorregimientoErrors() {
      const errors = [];
      if (!this.$v.originCorregimiento.$dirty) return errors;
      !this.$v.originCorregimiento.name.required &&
        errors.push("Corregimiento de origen es requerido.");
  
      return errors;
    },
    originVeredaErrors() {
      const errors = [];
      if (!this.$v.originVereda.$dirty) return errors;
      !this.$v.originVereda.name.required &&
        errors.push("Vereda de origen es requerido.");
        
      return errors;
    }
  },
  methods: {
    check(event) {
      if (this.checkbox) {
        this.originZone = this.currentZone;
        this.originState = this.currentState;
        this.originCity = this.currentCity;
        this.originComuna = this.currentComuna;
        this.originNeighborhood = this.currentNeighborhood;
        this.originCorregimiento = this.currentCorregimiento;
        this.originVereda = this.currentVereda;
        this.disabled = true
      }else{
        this.disabled = false
      } 
    },
    emitAllToParent(event) {
      this.$v.$touch();
      if (this.$v.$anyError) {
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo. ";
      } else {
        this.submitStatus = "";
        let data = [
          this.currentZone,
          this.currentState,
          this.currentCity,
          this.currentComuna,
          this.currentNeighborhood,
          this.currentCorregimiento,
          this.currentVereda,
          this.originZone,
          this.originState,
          this.originCity,
          this.originComuna,
          this.originNeighborhood,
          this.originCorregimiento,
          this.originVereda,
          "4"
        ];
        this.$emit("allToParent", data);
      }
    },
    emitBeforeToParent(event) {
      this.$emit("before", 2);
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

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

h3 {
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
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
</style>
