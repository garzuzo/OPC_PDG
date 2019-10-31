<template>
  <div>
    <v-col cols="5">
      <div class="form-group">
        <label for="higherEducation">Nivel educativo más alto alcanzado*</label>
        <v-select
          :items="education"
          :error-messages="higherEducationErrors"
          item-text="name"
          item-value="name"
          outlined
          v-model="higherEducation"
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
          required
          class="input"
          color="#0C186D"
          name="level"
          @change="$v.level.$touch()"
        ></v-select>
        {{this.higherEducation}}
        HERE GOES{{levelsEd}}
      </div>
    </v-col>

    <v-container>
      <p v-if="submitStatus!=''">Revisa las advertencias. Tienes algún error en los campos</p>
      <v-row justify="space-between">
        <v-col cols="2">
          <v-btn :ripple="false" class="ma-2 next" outlined color="#673ab7" @click="emitBeforeToParent">Anterior</v-btn>
        </v-col>
        <v-col cols="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitAllToParent"
          >Finalizar</v-btn>
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
    higherEducation: { required },
    level : { required }
  },
  data() {
    return {
      higherEducation: "",
      level: "",
      education: [],
      levels: [],
      submitStatus: ""
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

    /*api.getAchievedLevel(this.higherEducation).then(response => {
      console.log("ESTA ES PRIMARIA")
      console.log(response)
      this.levels = response.data
    }).catch(err => {
      console.log(err)
    })*/
  },
  computed: {
    levelsEd() {
      if(this.higherEducation != ""){
        api
        .getAchievedLevel(this.higherEducation)
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
        !this.$v.higherEducation.required && errors.push('Nivel más alto alcanzado es requerido.')
        return errors
    },
    levelErrors(){
      const errors = []
        if (!this.$v.level.$dirty) return errors
        !this.$v.level.required && errors.push('Nivel alcanzado en el anterior nivel es requerido.')
        return errors
    }
  },
  methods: {
    emitAllToParent(event){
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Error"
      }else{
        let data = [this.higherEducation, this.level, "done"];
        this.submitStatus = ""
        this.$emit("allToParent", data);
      } 
    },
    emitBeforeToParent(event){
      this.$emit("before", 2)
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
