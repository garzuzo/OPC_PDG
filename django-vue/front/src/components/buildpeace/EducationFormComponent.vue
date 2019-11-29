<template>
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
          :items="levelsEd"
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
      <div v-if="submitStatus!=''" class="px-5 alert alert-danger" role="alert">
          {{submitStatus}}
      </div>
      <v-row justify="space-between">
        <v-col cols="4" sm="4" md="2">
          <v-btn :ripple="false" class="ma-2 next" outlined color="#673ab7" @click="emitBeforeToParent">Anterior</v-btn>
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
import { required } from 'vuelidate/lib/validators'
import { validationMixin } from 'vuelidate'

export default {
  name: "PersonalForm",
  mixins: [validationMixin],

  validations: {
    higherEducation: {name: {required}},
    level : {name: {required}}
  },
  data() {
    return {
      higherEducation: { id: 0, name: '' },
      level: { id: 0, name: '' },
      education: [],
      levels: [],
      submitStatus: "",
    };
  },
  created() {
    api
      .getLevelsEducation()
      .then(response => {
        this.education = response;
      })
      .catch(err => {
        console.log(err);
      });
  },
  computed: {
    levelsEd() {
      if(this.higherEducation.name != ""){
        api
        .getAchievedLevel(this.higherEducation.name)
        .then(response => {
          this.levels = response;
        })
        .catch(err => {
          console.log(err);
        });
      }
      return this.levels;
    },
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
  },
  methods: {
    emitAllToParent(event){
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo."
      }else{
        let data = [this.higherEducation, this.level, "5"];
        this.submitStatus = ""
        this.$emit("allToParent", data);
      } 
    },
    emitBeforeToParent(event){
      this.$emit("before", 3)
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
</style>
