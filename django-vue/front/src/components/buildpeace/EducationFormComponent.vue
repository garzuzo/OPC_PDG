<template>
  <div>
    <v-col cols="5">
      <div class="form-group">
        <label for="higherEducation">Nivel educativo más alto alcanzado*</label>
        <v-select
          :items="education"
          outlined
          v-model="higherEducation"
          required
          class="input"
          color="#0C186D"
          name="higherEducation"
        ></v-select>
      </div>

      <div class="form-group">
        <label for="level">Nivel más alto alcanzado en el anterior nivel*</label>
        <v-select
          :items="levels"
          outlined
          v-model="level"
          required
          class="input"
          color="#0C186D"
          name="level"
        ></v-select>
      </div>
    </v-col>
  </div>
</template>

<script>
import api from "../../axios.js";

export default {
  name: "PersonalForm",
  //inject: ["$validator"],
  data() {
    return {
      higherEducation: "",
      level: "",
      education: [
        "Preescolar",
        "Primaria",
        "Bachillerato",
        "Técnico",
        "Tecnologo",
        "Universitaria",
        "Universitaria o superior",
        "Ninguno"
      ], 
      levels: ["En curso", "Terminado"]
    };
  }, 
  created() {
    
    api.getLevelsEducation().then(response => {
        this.education = response.data
      }).catch(err =>{
        console.log(err)
      });

    api.getAchievedLevel(this.higherEducation).then(response => {
      this.levels = response.data
    }).catch(err => {
      console.log(err)
    })
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
</style>
