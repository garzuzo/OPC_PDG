<template>
  <div>
    <v-row align="center" justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="5">
        <div class="form-group">
          <label for="name">Nombre*</label>
          <v-text-field
            v-model="name"
            :error-messages="nameErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="name"
            class="input"
            @input="$v.name.$touch()"
          ></v-text-field>
        </div>
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
      <v-col cols="5">
        <div class="form-group">
          <label for="lastname">Apellidos*</label>
          <v-text-field
            v-model="lastname"
            :error-messages="lastnameErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="lastname"
            class="input"
            @input="$v.lastname.$touch()"
          ></v-text-field>
        </div>

        <div class="form-group">
          <label for="gender">Género*</label>
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
      <div v-if="submitStatus!=''" class="px-5 alert alert-danger" role="alert">
          Revisa las advertencias. Tienes algún error en los campos
      </div>
      <v-row justify="end">
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
import { required, minLength, minValue} from 'vuelidate/lib/validators'
import { validationMixin } from 'vuelidate'

function dateMaxValue (date) {
      //const validator = minValue(new Date())
      const dateSplit = date.split("-")
      date = new Date(parseInt(dateSplit[0]), parseInt(dateSplit[1])-1, parseInt(dateSplit[2]))
      console.log(date)
      return date < new Date()
}

const requiredObject = (value) => value.typeGender != ''
export default {
  name: "PersonalForm",
  mixins: [validationMixin],
  
  validations: {
    
    name: { required, minLength: minLength(3) },
    lastname : {required, minLength: minLength(3)},
    age : {required, dateMaxValue},
    gender : {typeGender: {required}}
  },

  data() {
    return {
      name: "",
      lastname: "",
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
        console.log(this.genders);
      })
      .catch(err => console.log(err));
  },
  methods: {
    emitAllToParent(event) {
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Error"
      }else{
        let data = [this.age, this.gender, this.name, this.lastname, "2"];
        this.submitStatus = ""
        this.$emit("allToParent", data);
      }
      
    }
  }, 
  computed: {
    nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.minLength && errors.push('Nombre debe tener mínimo 3 caracteres')
        !this.$v.name.required && errors.push('Nombre es requerido.')
        return errors
      }, 
    lastnameErrors(){
      const errors = []
        if (!this.$v.lastname.$dirty) return errors
        !this.$v.lastname.minLength && errors.push('Apellido debe tener mínimo 3 caracteres')
        !this.$v.lastname.required && errors.push('Apellido es requerido.')
        return errors
    },
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
