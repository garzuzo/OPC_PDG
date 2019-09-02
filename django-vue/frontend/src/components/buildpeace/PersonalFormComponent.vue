<template>
<div>
    <v-layout row align-center justify-space-around>
      <v-flex xs4>
        <div class="form-group">
          <label for="name">Nombre*</label>
         <v-text-field
              v-model="name"
              solo
              single-line
              color="#000000"
              height="16"
              required
              name="name"
              class="input"
            ></v-text-field>
        </div>
      </v-flex>

      <v-flex xs4>
        <div class="form-group">
          <label for="lastname">Apellidos*</label>
          <v-text-field
              v-model="lastname"
              solo
              single-line
              color="#000000"
              height="16"
              required
              name="lastname"
              class="input"
            ></v-text-field>
        </div>
      </v-flex>
    </v-layout>

    <br>

    <v-layout row align-center justify-space-around>
      <v-flex xs4>
        <div class="form-group">
          <label for="age">Edad*</label>
          <v-text-field
              v-model="age"
              solo
              single-line
              color="#000000"
              height="16"
              required
              name="age"
              class="input"
            ></v-text-field>
        </div>
      </v-flex>

      <v-flex xs4>
        <div class="form-group">
          <label for="gender">Género*</label>
          <v-select
          :items="genders"
          solo
          v-model="gender"
          required
          class="input"
        ></v-select>
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
      name: "",
      lastname: "",
      age: "",
      gender: "",
      genders:['Femenino', 'Masculino']
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
