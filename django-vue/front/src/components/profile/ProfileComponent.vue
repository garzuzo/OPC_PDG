<template>
  <div>
    <navbar-component></navbar-component>

    <div class="init">
      <h3 align="center">Tu perfil</h3>
      <br />
      <div class="profile">
        <img src="@/assets/profile.png" />
        <h3 align="center">Johnatan Garzón</h3>
        <v-btn :ripple="false" rounded class="ma-2 ml-5 edit" color="#ffffff">Editar información</v-btn>
      </div>
    </div>

    <v-row justify="space-around"> 
        <v-col cols="5">
            <h2 align="center">Campañas activas </h2>
            <v-col v-for="n in 2" :key="n" class="d-flex child-flex">
                <campaign-item-component></campaign-item-component>
            </v-col>
        </v-col>

        <v-col cols="5">
            <h2 align="center">Campañas pasadas </h2>
            <v-col v-for="n in 5" :key="n" class="d-flex child-flex">
                <campaign-item-component></campaign-item-component>
            </v-col>
        </v-col>   
    </v-row>    
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.init {
  background-color: #673ab7;
}

.profile {
  margin: 0 auto;
  width: 20%;
}

h3 {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 36px;
  line-height: 66px;

  color: #ffffff;
}

h2{
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  font-size: 36px;
  line-height: 96px;
  color: #0c186d;

}
.edit {
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
  text-transform: none !important;
}
</style>