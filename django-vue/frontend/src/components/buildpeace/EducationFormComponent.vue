<template>
<div>
    <v-layout column align-start>
      <v-flex xs4>
        <div class="form-group">
          <label for="higherEducation">Nivel educativo más alto alcanzado*</label>
          <v-select
          :items="education"
          solo
          v-model="higherEducation"
          required
          class="input"
          name="higherEducation"
        ></v-select>
         
        </div>
      </v-flex>

      <v-flex xs5>
        <div class="form-group">
          <label for="level">Nivel más alto alcanzado en el anterior nivel*</label>
          <v-text-field
              v-model="level"
              solo
              single-line
              color="#000000"
              height="16"
              required
              name="level"
              class="input"
            ></v-text-field>
        </div>
      </v-flex>
    </v-layout>
</div>
</template>

<script>
export default {
  name: "PersonalForm",
  //inject: ["$validator"],
  data() {
    return {
      higherEducation: '',
      level: '',
      education:['Preescolar','Primaria', 'Bachillerato', 'Técnico', 'Tecnologo', 'Universitaria', 'Universitaria o superior','Ninguno']
    };
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
