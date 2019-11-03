<template>
<div>
 <v-container fluid class="fill-height col-form" style="min-height: 100%">
 <v-row align="center" justify="center">
   <v-col cols="4">
    <v-form class="form container pa-5" @submit.prevent="login">
      <h3>Iniciar Sesión </h3>

      <div class="form-group">
          <label for="email">Correo electrónico*</label>
          <v-text-field
            v-model="email"
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
          <label for="password">Contraseña*</label>
          <v-text-field
            v-model="password"
            :error-messages="passwordErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            ref="password"
            type="password"
            name="password"
            class="input"
            @input="$v.password.$touch()"
          ></v-text-field>
        </div>

    <v-btn :ripple="false" class="mx-2 login" tile color="#673AB7" dark @click="submit">Iniciar</v-btn>
  </v-form>
   </v-col>
 </v-row> 
 </v-container>

</div>
</template>

<script>
import { required, email, minLength} from 'vuelidate/lib/validators'
import { validationMixin } from 'vuelidate'
import { helpers } from 'vuelidate/lib/validators'

const upperCase = helpers.regex('upperCase', /[A-Z]/)
const number = helpers.regex('number', /[0-9]/)
//const specialCharacter = helpers.regex('specialCharacter',/[!@#$%^&*(),.?":{}|<>]/)
export default {
  mixins: [validationMixin],
  
  validations: {    
    email: { required, email },
    password : {required, minLength: minLength(6), upperCase, number }
  },
    data(){
      return{        
        email:"",
        password:""
      }
    },
    methods: {
      login() {
      this.$v.$touch();
      if (this.$v.$anyError) {
        this.submitStatus = "Error";
      } else {
        this.submitStatus = "";
        let data = {
          username: this.email,
          password: this.password
        };

        this.$store
        .dispatch("login", data)
        .then(() => {
          this.$router.push("/construirpaz")
        })
        .catch(err => {
          console.log(err);
        });
      }
    }
    }, 
    computed: {
    emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('El email debe tener una dirección valida')
        !this.$v.email.required && errors.push('Email es requerido.')
        return errors
      }, 
    passwordErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.minLength && errors.push('Contraseña debe tener mínimo 6 caracteres')
        !this.$v.password.required && errors.push('Contraseña es requerido.')
        !this.$v.password.upperCase && errors.push('Contraseña debe tener una letra mayuscula.')
        !this.$v.password.number && errors.push('Contraseña debe tener un número.')
       // !this.$v.password.specialCharacter && errors.push('Contraseña debe tener un caracter especial.')
        return errors
      }, 
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap');
.col-form {
  background: #E1E1E9;
  height: 100vh;
}

.form{
  background: #ffffff;
  box-shadow: 0px 2.45451px 24.5451px rgba(0, 0, 0, 0.4);
  border-radius: 6.13627px;
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