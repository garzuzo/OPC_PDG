<template>
  <v-row justify="center">
    <v-col cols="12">
      <v-form class="form pa-5">
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

        <div class="form-group">
          <label for="passwordConfirmation">Confirmar contraseña*</label>
          <v-text-field
            v-model="passwordConfirmation"
            :error-messages="passwordConfirmationErrors"
            outlined
            color="#0C186D"
            height="16"
            required
            type="password"
            name="passwordConfirmation"
            class="input"
            @input="$v.passwordConfirmation.$touch()"
          ></v-text-field>
        </div>
        
        <v-btn :ripple="false" class="ma-5 login" tile color="#673AB7" dark @click="register">Guardar</v-btn>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
import { required, email, minLength, sameAs } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";
import { helpers } from "vuelidate/lib/validators";

const upperCase = helpers.regex("upperCase", /[A-Z]/);
const number = helpers.regex("number", /[0-9]/);

export default {
  mixins: [validationMixin],

  validations: {
    email: { required, email },
    password: { required, minLength: minLength(6), upperCase, number },
    passwordConfirmation: { required, sameAsPassword: sameAs('password') }
  },
  props:{
    dialog: Boolean
  },
  data() {
    return {
      email: "",
      password: "",
      passwordConfirmation: ""
    };
  },
  methods: {
    register() {
      this.$v.$touch();
      if (this.$v.$anyError) {
        this.submitStatus = "Error";
        console.log("Errorrrr")
      } else {
          console.log("Entreeee")
        this.submitStatus = "";
        let data = {
          username: this.email,
          password: this.password
        };

        this.$store
        .dispatch("register", data)
        .then(() => {
          console.log("Registerrr")
          this.$router.push("/login")
        })
        .catch(err => {
          console.log(err);
        });
      }
    }
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email &&
        errors.push("El email debe tener una dirección valida");
      !this.$v.email.required && errors.push("Email es requerido.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.minLength &&
        errors.push("Contraseña debe tener mínimo 6 caracteres");
      !this.$v.password.required && errors.push("Contraseña es requerido.");
      !this.$v.password.upperCase &&
        errors.push("Contraseña debe tener una letra mayuscula.");
      !this.$v.password.number &&
        errors.push("Contraseña debe tener un número.");
      // !this.$v.password.specialCharacter && errors.push('Contraseña debe tener un caracter especial.')
      return errors;
    },
    passwordConfirmationErrors() {
    const errors = [];
    if (!this.$v.passwordConfirmation.$dirty) return errors;
    !this.$v.passwordConfirmation.required &&
      errors.push("Contraseña es requerido.");
    /*!this.$v.passwordConfirmed.minLength &&
      errors.push("Contraseña debe tener mínimo 6 caracteres");
    
    !this.$v.passwordConfirmed.upperCase &&
      errors.push("Contraseña debe tener una letra mayuscula.");
    !this.$v.passwordConfirmed.number &&
      errors.push("Contraseña debe tener un número.");*/
    !this.$v.passwordConfirmation.sameAsPassword && errors.push('Esta contraseña no coincide con la anterior.')
    // !this.$v.password.specialCharacter && errors.push('Contraseña debe tener un caracter especial.')
    return errors;
  }
  }
};
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