<template>
  <div>
    <v-row align="center" justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="7" sm="7" md="5">
        <div class="form-group">
          <label for="age">Fecha de nacimiento*</label>
          <v-menu
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="age"
                :error-messages="dateErrors"
                outlined
                color="#0C186D"
                height="16"
                required
                name="age"
                class="input"
                readonly
                v-on="on"
                @change="$v.age.$touch()"
              ></v-text-field>
            </template>
            <v-date-picker v-model="age" color="#0C186D" @input="menu2 = false"></v-date-picker>
          </v-menu>
        </div>
      </v-col>

      <!--SECOND COLUMN -->
      <v-col cols="5" sm="5" md="5">
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
      <div v-if="submitStatus!=''" class="pa-5 alert alert-danger" role="alert">
         {{submitStatus}}
      </div>
      <v-row justify="space-between">
        <v-col cols="4" sm="4" md="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitBeforeToParent"
          >Anterior</v-btn>
        </v-col>
        <v-col cols="4" sm="4" md="2">
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
import { required, minLength, minValue} from 'vuelidate/lib/validators'
import { validationMixin } from 'vuelidate'

function dateMaxValue (date) {
      //const validator = minValue(new Date())
      const dateSplit = date.split("-")
      date = new Date(parseInt(dateSplit[0]), parseInt(dateSplit[1])-1, parseInt(dateSplit[2]))
      return date < new Date()
}

export default {
  name: "PersonalForm",
  mixins: [validationMixin],
  
  validations: {
    age : {required, dateMaxValue},
    gender : {typeGender: {required}}
  },

  data() {
    return {
      age: new Date().toISOString().substr(0, 10),
      gender: { id: 0, typeGender: '' },
      genders: [],
      menu2: false,
      submitStatus: ''
    };
  },
  created() {
    api
      .getGender()
      .then(response => {
        this.genders = response;
      })
      .catch(err => console.log(err));
  },
  methods: {
    emitAllToParent(event) {
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo."
      }else{
        let data = [this.age, this.gender,"3"];
        this.submitStatus = ""
        this.$emit("allToParent", data);
      }
      
    },
    emitBeforeToParent(event) {
      this.$emit("before", 1);
    }
  }, 
  computed: {
    dateErrors(){
      const errors = []
        if (!this.$v.age.$dirty) return errors
        !this.$v.age.required && errors.push('Fecha de nacimiento es requerido.')
        !this.$v.age.dateMaxValue && errors.push('Fecha de nacimiento debe ser menor a la fecha actual.')
        return errors
    },
    genderErrors(){
      const errors = []
        if (!this.$v.gender.$dirty) return errors
        !this.$v.gender.typeGender.required && errors.push('Genero es requerido.')
        return errors
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
