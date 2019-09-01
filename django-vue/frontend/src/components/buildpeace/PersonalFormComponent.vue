<template>
  <v-container>
    <v-layout row align-center justify-space-around>
      <v-flex xs4>
        <div class="form-group">
          <label for="name">Nombre*</label>
         <v-text-field
              v-model="name"
              solo
              single-line
              class="inpt"
              color="#000000"
            ></v-text-field>
        </div>
      </v-flex>

      <v-flex xs4>
        <div class="form-group">
          <label for="lastname">Apellidos*</label>
          <v-text-field v-model="lastname" name="name" type="text" required outline single-line/>
        </div>
      </v-flex>
    </v-layout>

    <br>

    <v-layout row align-center justify-space-around>
      <v-flex xs4>
        <div class="form-group">
          <label for="age">Edad*</label>
          <input v-model="age" name="name" type="text" required class="input"/>
        </div>
      </v-flex>

      <v-flex xs4>
        <div class="form-group">
          <label for="gender">Género*</label>
          <br>
          <select v-model="gender" name="gender" class="form-control input" required>
            <option>Femenino</option>
            <option>Masculino</option>
          </select>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
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
      gender: ""
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
  background: #ffffff;
  border: 1px solid #000000;
  box-sizing: border-box;
  border-radius: 5px;
}

.v-input__slot{
  height: 20px !important;
}
</style>
