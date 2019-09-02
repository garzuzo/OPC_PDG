<template>
  <div>
    <v-row align="center" justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="4">
        <div class="form-group">
          <label for="name">Nombre*</label>
          <v-text-field
            v-model="name"
            outlined
            color="#0C186D"
            height="16"
            required
            name="name"
            class="input"
          ></v-text-field>

          <div class="form-group">
            <label for="age">Edad*</label>
            <v-text-field
              v-model="age"
              outlined
              color="#0C186D"
              height="16"
              required
              name="age"
              class="input"
            ></v-text-field>
          </div>
        </div>
      </v-col>

      <!--SECOND COLUMN -->
      <v-col cols="4">
        <div class="form-group">
          <label for="lastname">Apellidos*</label>
          <v-text-field
            v-model="lastname"
            outlined
            color="#0C186D"
            height="16"
            required
            name="lastname"
            class="input"
          ></v-text-field>
        </div>

        <div class="form-group">
          <label for="gender">Género*</label>
          <v-select
            :items="genders"
            outlined
            v-model="gender"
            required
            class="input"
            color="#0C186D"
          ></v-select>
        </div>
      </v-col>
    </v-row>
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
      genders: ["Femenino", "Masculino"]
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
