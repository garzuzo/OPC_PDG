<template>
  <v-container>
    <v-row justify="center">
        <v-col cols="4">
            <h3>   Personal   </h3>
        </v-col>
      <v-row justify="center">
        <v-col cols="3">
          <div class="form-group">
            <label for="name">Nombre*</label>
            <v-text-field
              v-model="profile.name"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>
        <v-col cols="3">
          <div class="form-group">
            <label for="name">Apellido*</label>
            <v-text-field
              v-model="profile.lastname"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>

        <v-col cols="3">
          <div class="form-group">
            <label for="name">Genero*</label>
            <v-text-field
              v-model="profile.gender"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>

        <v-col cols="3">
          <div class="form-group">
            <label for="name">Fecha de nacimiento*</label>
            <v-text-field
              v-model="profile.age"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>
      </v-row>
    </v-row>

    <v-row justify="center">
        <v-col cols="4">
            <h3>Educación</h3>
        </v-col>
      <v-row justify="center">
        <v-col cols="6">
          <div class="form-group">
            <label for="name">Nivel más alto alcanzado*</label>
            <v-text-field
              v-model="profile.higherEducation"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>
        <v-col cols="6">
          <div class="form-group">
            <label for="name">Nivel alcanzado en el anterior nivel*</label>
            <v-text-field
              v-model="profile.level"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>
      </v-row>
    </v-row>

    <v-row justify="center">
        <v-col cols="4">
            <h3>Territorio actual</h3>
        </v-col>
      <v-row justify="center">
        <v-col cols="3">
          <div class="form-group">
            <label for="name">Zona*</label>
            <v-text-field
              v-model="profile.currentZone"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>
        <v-col cols="3">
          <div class="form-group">
            <label for="name">Departamento*</label>
            <v-text-field
              v-model="profile.currentState"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>

        <v-col cols="3">
          <div class="form-group">
            <label for="name">Ciudad*</label>
            <v-text-field
              v-model="profile.currentCity"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>

        <v-col cols="3">
          <div class="form-group">
            <label for="name">Comuna*</label>
            <v-text-field
              v-model="profile.currentComuna"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>

        <v-col cols="3">
          <div class="form-group">
            <label for="name">Barrio*</label>
            <v-text-field
              v-model="profile.currentNeighborhood"
              outlined
              color="#0C186D"
              height="16"
              required
              name="name"
              class="input"
              @input="$v.name.$touch()"
            ></v-text-field>
          </div>
        </v-col>
      </v-row>
    </v-row>
    
  </v-container>
</template>

<script>
export default {
  props: {
    profile: Object
  }
};
</script>
<style scoped>
h3{
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 36px;
  line-height: 96px;
  color: #0c186d;

}
</style>