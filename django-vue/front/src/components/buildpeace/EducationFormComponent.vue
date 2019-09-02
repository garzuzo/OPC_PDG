<template>
<div>
   <!-- <v-row align="start">
      
        
      </v-col>
    </v-row> -->

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
          <v-text-field
              v-model="level"
              outlined
              color="#0C186D"
              height="16"
              required
              name="level"
              class="input"
            ></v-text-field>
        </div>
</v-col>
    <!--<v-row align="start">
      <v-col cols="5">
        
      </v-col>
    </v-row> -->
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
