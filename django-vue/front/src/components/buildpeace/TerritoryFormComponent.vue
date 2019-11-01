<template>
  <div>
    <v-row justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="5">
        <h3>Territorio donde vives</h3>
        <div class="form-group">
          <label for="currentZone">Zona*</label>
          <v-select
            :items="zones"
            item-text="zoneType"
            item-value="zoneType"            
            outlined
            v-model="currentZone"
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
            :error-messages="currentStateErrors"
            required
            class="input"
            color="#0C186D"
            name="currentState"
            @change="$v.currentState.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="currentZone == zones[1].zoneType & currentCity == 'Cali'">
          <label for="currentComuna">Comuna*</label>
          <v-select
            :items="comunasCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="currentComuna"
            :error-messages="currentComunaErrors"
            required
            class="input"
            color="#0C186D"
            name="currentComuna"
            @change="$v.currentComuna.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="currentZone == zones[0].zoneType & currentCity == 'Cali'">
          <label for="currentCorregimiento">Corregimiento*</label>
          <v-select
            :items="corregimientosCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="currentCorregimiento"
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
      <v-col align-self="end" cols="5">
        <div class="form-group">
          <label for="currentCity">Ciudad*</label>
          <v-select
            :items="currentCities"
            item-text="name"
            item-value="name" 
            outlined
            v-model="currentCity"
            :error-messages="currentCityErrors"
            required
            class="input"
            color="#0C186D"
            name="currentCity"
            @change="$v.currentCity.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="currentZone == zones[1].zoneType & currentCity == 'Cali'">
          <label for="currentNeighborhood">Barrio*</label>
          <v-select
            :items="neighborhoodsCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="currentNeighborhood"
            :error-messages="currentNeighborhoodErrors"
            required
            class="input"
            color="#0C186D"
            name="currentNeighborhood"
            @change="$v.currentNeighborhood.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="currentZone == zones[0].zoneType & currentCity == 'Cali'">
          <label for="currentVereda">Vereda*</label>
          <v-select
            :items="veredasCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="currentVereda"
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

    <!--ORIGIN TERRITORY -->
    <v-row justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="5">
        <h3>Territorio de origen</h3>
        <v-checkbox
          v-model="checkbox"
          label="¿Tu territorio de origen es igual al territorio donde vives?"
          @change="check($event)"
        ></v-checkbox>

        <div class="form-group">
          <label for="originZone">Zona*</label>
          <v-select
            :items="zones"
            item-text="zoneType"
            item-value="zoneType"   
            outlined
            v-model="originZone"
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
            v-model="originState"
            :error-messages="originStateErrors"
            required
            class="input"
            color="#0C186D"
            name="originState"
            @change="$v.originState.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone == zones[1].zoneType & originCity == 'Cali'">
          <label for="originComuna">Comuna*</label>
          <v-select
            :items="comunasCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="originComuna"
            :error-messages="originComunaErrors"
            required
            class="input"
            color="#0C186D"
            name="originComuna"
            @change="$v.originComuna.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone == zones[0].zoneType & originCity == 'Cali'">
          <label for="originCorregimiento">Corregimiento*</label>
          <v-select
            :items="corregimientosCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="originCorregimiento"
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
      <v-col align-self="end" cols="5">
        <div class="form-group">
          <label for="originCity">Ciudad*</label>
          <v-select
            :items="originCities"
            item-text="name"
            item-value="name" 
            outlined
            v-model="originCity"
            :error-messages="originCityErrors"
            required
            class="input"
            color="#0C186D"
            name="originCity"
            @change="$v.originCity.$touch()"
          ></v-select>
        </div>


        <div class="form-group" v-if="originZone == zones[1].zoneType & originCity == 'Cali'">
          <label for="originNeighborhood">Barrio*</label>
          <v-select
            :items="neighborhoodsCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="originNeighborhood"
            :error-messages="originNeighborhoodErrors"
            required
            class="input"
            color="#0C186D"
            name="originNeighborhood"
            @change="$v.originNeighborhood.$touch()"
          ></v-select>
        </div>

        <div class="form-group" v-if="originZone == zones[0].zoneType & originCity == 'Cali'">
          <label for="originVereda">Vereda*</label>
          <v-select
            :items="veredasCali"
            item-text="name"
            item-value="name" 
            outlined
            v-model="originVereda"
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
      <p v-if="submitStatus!=''">Revisa las advertencias. Tienes algún error en los campos</p>
      <v-row justify="space-between">
        <v-col cols="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitBeforeToParent"
          >Anterior</v-btn>
        </v-col>
        <v-col cols="2">
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
import { required } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";

export default {
  name: "PersonalForm",
  mixins: [validationMixin],

  validations: {
    currentZone: { required },
    currentState: { required },
    currentCity: { required },
    currentComuna: { required },
    currentNeighborhood: { required },
    currentCorregimiento: { required },
    currentVereda: { required },
    originZone: { required },
    originState: { required },
    originCity: { required },
    originComuna: { required },
    originNeighborhood: { required },
    originCorregimiento: { required },
    originVereda: { required }
  },
  data() {
    return {
      currentZone: "",
      currentState: "",
      currentCity: "",
      currentComuna: "",
      currentNeighborhood: "",
      currentCorregimiento: "",
      currentVereda: "",
      originZone: "",
      originState: "",
      originCity: "",
      originComuna: "",
      originNeighborhood: "",
      originCorregimiento: "",
      originVereda: "",
      zones: [],
      currentCitiesComputed: [],
      originCitiesComputed: [],
      states: [],
      comunasCali: [],
      neighborhoodsCali: [],
      corregimientosCali: [],
      veredasCali: [],
      checkbox: false,
      submitStatus: ""
    };
  },
  created() {
    api
      .getZones()
      .then(response => {
        this.zones = response;
        console.log(response)
      })
      .catch(err => console.log(err));

    api
      .getStates("COLOMBIA")
      .then(response => {
        this.states = response;
      })
      .catch(err => console.log(err));

    let dataComunaNeighborhood = ["Cali", "Urbana"];
      api.getCorregimientosComunas(dataComunaNeighborhood)
          .then(response => {
            this.comunasCali = response;
          })
          .catch(err => {
            console.log(err);
          });

    let dataCorregimientoVereda = ["Cali", "Rural"];
    api.getCorregimientosComunas(dataCorregimientoVereda)
          .then(response => {
            this.corregimientosCali = response;
          })
          .catch(err => {
            console.log(err);
          });

    api.getNeighborhoodsVeredas(dataComunaNeighborhood).then(response=>{
      this.neighborhoodsCali = response
    }).catch(err => console.log(err));

    api.getNeighborhoodsVeredas(dataCorregimientoVereda).then(response=>{
      this.veredasCali = response
    }).catch(err => console.log(err))
  },
  computed: {
    currentCities() {
      if(this.currentState != ""){
        api
        .getCities(this.currentState)
        .then(response => {
          this.currentCitiesComputed = response;
        })
        .catch(err => {
          console.log(err);
        });
      }
      return this.currentCitiesComputed
    },
    originCities(){
      if(this.originState != ""){
        api
        .getCities(this.originState)
        .then(response => {
          this.originCitiesComputed = response;
        })
        .catch(err => {
          console.log(err);
        });
      }
      return this.originCitiesComputed
    },
    currentZoneErrors(){
      const errors = []
        if (!this.$v.currentZone.$dirty) return errors
        !this.$v.currentZone.required && errors.push('Zona actual es requerido.')
        return errors
    },
    currentStateErrors(){
      const errors = []
        if (!this.$v.currentState.$dirty) return errors
        !this.$v.currentState.required && errors.push('Departamento actual es requerido.')
        return errors
    },
    currentCityErrors(){
      const errors = []
        if (!this.$v.currentCity.$dirty) return errors
        !this.$v.currentCity.required && errors.push('Ciudad actual es requerido.')
        return errors
    },
    currentComunaErrors(){
      const errors = []
        if (!this.$v.currentComuna.$dirty) return errors
        !this.$v.currentComuna.required && errors.push('Comuna actual es requerido.')
        return errors
    },
    currentNeighborhoodErrors(){
      const errors = []
        if (!this.$v.currentNeighborhood.$dirty) return errors
        !this.$v.currentNeighborhood.required && errors.push('Barrio actual es requerido.')
        return errors
    },
    currentCorregimientoErrors(){
      const errors = []
        if (!this.$v.currentCorregimiento.$dirty) return errors
        !this.$v.currentCorregimiento.required && errors.push('Corregimiento actual es requerido.')
        return errors
    },
    currentVeredaErrors(){
      const errors = []
        if (!this.$v.currentVereda.$dirty) return errors
        !this.$v.currentVereda.required && errors.push('Vereda actual es requerido.')
        return errors
    },
    originZoneErrors(){
      const errors = []
        if (!this.$v.originZone.$dirty) return errors
        !this.$v.originZone.required && errors.push('Zona de origen es requerido.')
        return errors
    },
    originStateErrors(){
      const errors = []
        if (!this.$v.originState.$dirty) return errors
        !this.$v.originState.required && errors.push('Departamento de origen es requerido.')
        return errors
    },
    originCityErrors(){
      const errors = []
        if (!this.$v.originCity.$dirty) return errors
        !this.$v.originCity.required && errors.push('Ciudad de origen es requerido.')
        return errors
    },
    originComunaErrors(){
      const errors = []
        if (!this.$v.originComuna.$dirty) return errors
        !this.$v.originComuna.required && errors.push('Comuna de origen es requerido.')
        return errors
    },
    originNeighborhoodErrors(){
      const errors = []
        if (!this.$v.originNeighborhood.$dirty) return errors
        !this.$v.originNeighborhood.required && errors.push('Barrio de origen es requerido.')
        return errors
    },
    originCorregimientoErrors(){
      const errors = []
        if (!this.$v.originCorregimiento.$dirty) return errors
        !this.$v.originCorregimiento.required && errors.push('Corregimiento de origen es requerido.')
        return errors
    },
    originVeredaErrors(){
      const errors = []
        if (!this.$v.originVereda.$dirty) return errors
        !this.$v.originVereda.required && errors.push('Vereda de origen es requerido.')
        return errors
    },
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
      } else {
        this.originZone = "";
        this.originState = "";
        this.originCity = "";
        this.originComuna = "";
        this.originNeighborhood = "";
        this.originCorregimiento = "";
        this.originVereda = "";
      }
    },
    emitAllToParent(event) {
      this.$v.$touch();
      if (this.$v.$anyError) {
        this.submitStatus = "Error";
      }else{
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
        "3"
      ];
      this.$emit("allToParent", data);
      }
    },
    emitBeforeToParent(event) {
      this.$emit("before", 1);
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
