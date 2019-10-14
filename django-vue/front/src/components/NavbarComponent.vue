<template>
  <v-toolbar color="#E1E1E9" height="84">
    <v-toolbar-title>
      <img src="@/assets/bird.png" width="51" height="49" class="d-inline-block" alt />
      <h1>Narrativas de paz</h1>
    </v-toolbar-title>

    <v-spacer></v-spacer>
    <v-toolbar-items>
      <v-btn
        :ripple="false"        
        depressed
        color="#E1E1E9"
        class="btn"
        to="/construirpaz"
      >Construir paz</v-btn>
      <v-btn :ripple="false" depressed color="#E1E1E9" class="btn"  to="/sobrenosotros">Sobre nosotros</v-btn>
      <v-btn :ripple="false" depressed color="#E1E1E9" class="btn">Visualiza</v-btn>
      <v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/campañas">Campañas</v-btn>
      <v-btn :ripple="false" depressed color="#E1E1E9" class="btn">Datos abiertos</v-btn>
    </v-toolbar-items>

    <v-btn :ripple="false" class="ma-2 login" tile color="#673AB7" dark>Log in</v-btn>
  </v-toolbar>
</template>

<script>
export default {};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap');

h1 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  color: #0c186d;
  font-size: 24px;
  line-height: 36px;
  display: inline-block;
  position: absolute;
  top: 20px;
}

.btn {
  text-transform: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  color: #0c186d;
  font-size: 16px;
  line-height: 24px;
}

.login {
  border-radius: 5px;
  text-transform: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
}
</style>