<template>
    <v-container>
        <v-row>
        <v-col cols="12" sm="12" md="12">
          <v-checkbox
          v-model="checkbox"
          label="¿Deseas guardar tus datos para una próxima ocasión?"
          @change="check($event)"
        ></v-checkbox>
        </v-col>
        </v-row>

        <v-row v-if="checkbox">
            <v-col cols="12" sm="12" md="4">
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
            </v-col>
            <v-col cols="12" sm="12" md="4">
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
            </v-col>
            <v-col cols="12" sm="12" md="4">
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
            </v-col>
        </v-row>
        <div v-if="submitStatus!=''" class="pa-5 alert alert-danger" role="alert">
          {{submitStatus}}
      </div>

        <v-row justify="space-between">
          <v-col cols="4" sm="4" md="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitBeforeToParent"
          >Anterior</v-btn>
        </v-col>
            <v-col cols="4" sm="4" md="2">
          <v-btn
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitAllToParent"
          >Finalizar</v-btn>
        </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { required, requiredIf, email, minLength, sameAs } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";
import { helpers } from "vuelidate/lib/validators";

const upperCase = helpers.regex("upperCase", /[A-Z]/);
const number = helpers.regex("number", /[0-9]/);

export default {
     mixins: [validationMixin],

  validations: {
    email: { required: requiredIf(function () {
        return this.checkbox
      }), email },
    password: { required: requiredIf(function () {
        return this.checkbox
      }), minLength: minLength(6), upperCase, number },
    passwordConfirmation: { required: requiredIf(function () {
        return this.checkbox
      }), sameAsPassword: sameAs('password') }
  },
    data(){
        return{
            email: "",
            password: "",
            passwordConfirmation: "",
            submitStatus:"",
            dialog:false,
            checkbox:false,
            scroll:false
        }
    },
    methods:{
      emitBeforeToParent(event){
         this.$emit("before", "4");
      },
        emitAllToParent(event){
            let data=[]
        this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo. "
      }else{
          this.submitStatus = ""
          if(this.checkbox){
              //register
               data=["register",this.email, this.password];
               this.$emit("allToParent", data);
          }else{
              //save data without register
             data= ["save"]
            this.$emit("allToParent", data);
          }        
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
        errors.push("Contraseña debe tener una letra mayúscula.");
      !this.$v.password.number &&
        errors.push("Contraseña debe tener un número.");
      return errors;
    },
    passwordConfirmationErrors() {
    const errors = [];
    if (!this.$v.passwordConfirmation.$dirty) return errors;
    !this.$v.passwordConfirmation.required &&
      errors.push("Contraseña es requerido.");
    !this.$v.passwordConfirmation.sameAsPassword && errors.push('Esta contraseña debe coincidir con la anterior.')
    return errors;
  }
}
}
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

.next {
  text-transform: none;
  font-family: "Roboto";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 33px;
  display: flex;
  align-items: center;
  text-align: center;
  letter-spacing: normal !important;
}

.save {
  text-transform: none;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 16px;
  line-height: 33px;
  display: flex;
  align-items: center;
  text-align: center;
}
</style>