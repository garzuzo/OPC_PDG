<template>
  <div>
    <v-row align="center" justify="space-around">
      <!--FIRST COLUMN-->
      <v-col cols="5">
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
            v-on:keyup="emitNameToParent"
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
            outlined
            color="#0C186D"
            height="16"
            required
            name="age"
            class="input"
            readonly
            v-on="on"
            v-on:keyup="emitAgeToParent"
          ></v-text-field>
      </template>
          <v-date-picker v-model="age" color="#0C186D"  @input="menu2 = false"></v-date-picker>
          </v-menu>
        </div>
      </v-col>

      <!--SECOND COLUMN -->
      <v-col cols="5">
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
            v-on:keyup="emitLastnameToParent"
          ></v-text-field>
        </div>

        <div class="form-group">
          <label for="gender">Género*</label>
          <v-select
            :items="genders"
            item-text = "typeGender"
            item-value = "typeGender"
            outlined
            v-model="gender"
            required
            class="input"
            color="#0C186D"
            v-on:change="emitGenderToParent"
          ></v-select>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import api from "../../axios.js";

export default {
  name: "PersonalForm",
  data() {
    return {
      name: "",
      lastname: "",
      age: new Date().toISOString().substr(0, 10),
      gender: "",
      genders: [], 
      menu2 : false
    };
  }, 
  created(){
    api.getGender().then( response => {
      this.genders = response
      console.log(this.genders )
    }).catch(err => console.log(err));
  }, 
  methods:{
    emitAgeToParent(event){
      this.$emit('ageToParent', this.age)
    },
    emitGenderToParent(event){
      this.$emit('genderToParent', this.gender)
    },
    emitNameToParent(event){
      this.$emit('nameToParent', this.name)
    },
    emitLastnameToParent(event){
      this.$emit('lastnameToParent', this.lastname)
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
</style>
