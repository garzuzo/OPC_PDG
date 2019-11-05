<template>
      <v-row justify="center">
    <v-col cols="12">
      <v-form class="form pa-5">
        <div class="form-group">
          <label for="email">Titulo*</label>
          <v-text-field
            v-model="title"
            :error-messages="emailErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="email"
            class="input"
            @input="$v.email.$touch()"
          ></v-text-field>
        </div>

        <div class="form-group">
          <label for="password">Descripción*</label>
          <v-text-field
            v-model="description"
            :error-messages="passwordErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="password"
            class="input"
            @input="$v.password.$touch()"
          ></v-text-field>
        </div>

        <div class="form-group">
          <label for="passwordConfirmation">Fecha de inicio*</label>
          <v-menu
            v-model="menuStart"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
            v-model="startDate"
            :error-messages="passwordConfirmationErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="passwordConfirmation"
            class="input"
            v-on="on"
            @input="$v.passwordConfirmation.$touch()"
          ></v-text-field>
            </template>
            <v-date-picker v-model="startDate" color="#0C186D" @input="menuStart = false"></v-date-picker>
          </v-menu>          
        </div>
        
        <div class="form-group">
          <label for="passwordConfirmation">Fecha de finalización*</label>
          <v-menu
            v-model="menuEnd"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
            v-model="endDate"
            :error-messages="passwordConfirmationErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="passwordConfirmation"
            class="input"
            v-on="on"
            @input="$v.passwordConfirmation.$touch()"
          ></v-text-field>
            </template>
            <v-date-picker v-model="endDate" color="#0C186D" @input="menuEnd = false"></v-date-picker>
          </v-menu>

          
        </div>

        <div class="form-group">
          <label for="passwordConfirmation">Meta de narrativas*</label>
          <v-text-field
            v-model="narrativesGoal"
            :error-messages="passwordConfirmationErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="passwordConfirmation"
            class="input"
            @input="$v.passwordConfirmation.$touch()"
          ></v-text-field>
        </div>

        <v-btn :ripple="false" class="ma-5 login" tile color="#673AB7" dark @click="register">Crear</v-btn>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
export default {
    data(){
        return{
            title: "", 
            description: "", 
            startDate: new Date().toISOString().substr(0, 10), 
            endDate: new Date().toISOString().substr(0, 10), 
            narrativesGoal: 0,
            menuStart: false, 
            menuEnd: false
        }
    }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
.col-form {
  background: #e1e1e9;
  height: 100vh;
}

.form {
  background: #ffffff;
}

.login {
  border-radius: 5px;
  text-transform: none !important;
  text-decoration: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  color: #0c186d;
}
</style>