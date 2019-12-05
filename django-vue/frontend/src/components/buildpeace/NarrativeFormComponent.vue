<template>

<div>
<!-- NARRATIVE -->
      <v-row align="center" justify="start">
        <v-col sm="12"> 
          <div id="text" class="form-group">
            <label for="narrative">Con un texto ayudanos a responder la pregunta: Para ti, ¿Qué si es paz?</label>
            <v-textarea
              v-model="narrative"
              :error-messages="narrativeErrors"
              outlined
              name="narrative"
              counter="500"
              color="#0C186D"
              class="input"
              @input="$v.narrative.$touch()"
            ></v-textarea>
          </div>
        </v-col>
      </v-row>

      <!--KEYWORDS -->
      <v-row align="center" justify="start">
        <v-col cols="12" sm="12" md="8">
          <p>Danos 5 palabras que para ti reflejen Qué si es paz</p>
        </v-col>
      </v-row>

      <v-row align="center" justify="start">
        <v-col cols="6" sm="6" md="4">
          <v-text-field
            v-model="word1"
            :error-messages="word1Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word1"
            class="input"
            @input="$v.word1.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="6" sm="6" md="4">
          <v-text-field
            v-model="word2"
            :error-messages="word2Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word2"
            class="input"
            @input="$v.word2.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="6" sm="6" md="4">
          <v-text-field
            v-model="word3"
            :error-messages="word3Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word3"
            class="input"
            @input="$v.word3.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="6" sm="6" md="4">
          <v-text-field
            v-model="word4"
            :error-messages="word4Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word4"
            class="input"
            @input="$v.word4.$touch()"
          ></v-text-field>
        </v-col>

        <v-col cols="6" sm="6" md="4">
          <v-text-field
            v-model="word5"
            :error-messages="word5Errors"
            outlined
            color="#0C186D"
            height="16"
            required
            name="word5"
            class="input"
            @input="$v.word5.$touch()"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-container>
      <div v-if="submitStatus!=''" class="px-5 alert alert-danger" role="alert">
          {{submitStatus}}
      </div>
      <div v-if="succes!=''" class="pa-5 alert alert-success" role="alert">
           {{succes}}
      </div>
      <v-row justify="end">
        <v-col cols="4" sm="4" md="2">
          <v-btn v-if="!isLoggedIn"
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitAllToParent"
          >Siguiente</v-btn>
          <v-btn v-if="isLoggedIn"
            :disabled="disabled"
            :ripple="false"
            class="ma-2 next"
            outlined
            color="#673ab7"
            @click="emitAllToParent"
          >Finalizar</v-btn>
        </v-col>
      </v-row>
    </v-container>
</div>
</template>

<script>
import { required, minLength, maxLength } from "vuelidate/lib/validators";
import { validationMixin } from "vuelidate";

function differents(word) {
  if (word == this.word1) {
    return (
      word != this.word2 &&
      word != this.word3 &&
      word != this.word4 &&
      word != this.word5
    );
  }
  if (word == this.word2) {
    return (
      word != this.word1 &&
      word != this.word3 &&
      word != this.word4 &&
      word != this.word5
    );
  }
  if (word == this.word3) {
    return (
      word != this.word1 &&
      word != this.word2 &&
      word != this.word4 &&
      word != this.word5
    );
  }
  if (word == this.word4) {
    return (
      word != this.word1 &&
      word != this.word2 &&
      word != this.word3 &&
      word != this.word5
    );
  }
  if (word == this.word5) {
    return (
      word != this.word1 &&
      word != this.word2 &&
      word != this.word3 &&
      word != this.word4
    );
  }
}

export default {
    mixins: [validationMixin],

  validations: {
    narrative: { required, minLength: minLength(3), maxLength: maxLength(500) },
    word1: { required, minLength: minLength(3), differents },
    word2: { required, minLength: minLength(3), differents },
    word3: { required, minLength: minLength(3), differents },
    word4: { required, minLength: minLength(3), differents },
    word5: { required, minLength: minLength(3), differents }
  },
  props:{
    succes: String,
    disabled: Boolean
  },
  data(){
      return{
        narrative: "",
        word1: "",
        word2: "",
        word3: "",
        word4: "",
        word5: "",
        submitStatus: "",
        isLoggedIn: this.$store.getters.isLoggedIn
      }
  },
  methods: {
    emitAllToParent(event) {
      this.$v.$touch()
      if(this.$v.$anyError){
        this.submitStatus = "Revisa las advertencias. Tienes algún error en los campos. Intenta de nuevo."
      }else{
        let data= []
        if(!this.isLoggedIn){
          data = [this.narrative, this.word1, this.word2, this.word3, this.word4,this.word5, "2"];
        }else{
          data = [this.narrative, this.word1, this.word2, this.word3, this.word4,this.word5, "0"];
        }        
        this.submitStatus = ""
        this.$emit("allToParent", data);
      }
    }
  }, 
  computed: {
    narrativeErrors() {
      const errors = [];
      if (!this.$v.narrative.$dirty) return errors;
      !this.$v.narrative.minLength &&
        errors.push("La narrative debe tener mínimo 3 caracteres");
      !this.$v.narrative.required && errors.push("La narrativa es requerida.");
      !this.$v.narrative.maxLength &&
        errors.push("La narrativa debe tener máximo 500 caracteres.");
      return errors;
    },
    word1Errors() {
      const errors = [];
      if (!this.$v.word1.$dirty) return errors;
      !this.$v.word1.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word1.required && errors.push("La palabra es requerida.");
      !this.$v.word1.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word2Errors() {
      const errors = [];
      if (!this.$v.word2.$dirty) return errors;
      !this.$v.word2.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word2.required && errors.push("La palabra es requerida.");
      !this.$v.word2.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word3Errors() {
      const errors = [];
      if (!this.$v.word3.$dirty) return errors;
      !this.$v.word3.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word3.required && errors.push("La palabra es requerida.");
      !this.$v.word3.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word4Errors() {
      const errors = [];
      if (!this.$v.word4.$dirty) return errors;
      !this.$v.word4.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word4.required && errors.push("La palabra es requerida.");
      !this.$v.word4.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    },
    word5Errors() {
      const errors = [];
      if (!this.$v.word5.$dirty) return errors;
      !this.$v.word5.minLength &&
        errors.push("La palabra debe tener mínimo 3 caracteres");
      !this.$v.word5.required && errors.push("La palabra es requerida.");
      !this.$v.word5.differents &&
        errors.push("La palabra debe ser diferente a las demás.");
      return errors;
    }
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");
label {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  text-align: center;
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
.input {
  font-family: "Roboto";
  font-style: normal;
  font-weight: normal;
  font-size: 16px;
  line-height: 36px;
}
</style>