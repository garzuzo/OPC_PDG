<template>
  <div>
    <v-toolbar color="#E1E1E9" height="84">
      <v-toolbar-title>
        <v-btn class="ma-2 btn" :ripple="false" depressed text icon to="/home">
          <v-icon>fas fa-dove</v-icon>
          <!--<img src="@/assets/bird.png" width="51" height="49" class="d-inline-block" alt />-->
        </v-btn>

        <!--<v-btn class="ma-2 btn"  :ripple="false" depressed text icon to="/home">
          <v-avatar size="20px">
            <img src="@/assets/bird.png" class="d-inline-block" alt />
          </v-avatar>
        </v-btn>-->
        <h1>Narrativas de paz</h1>
      </v-toolbar-title>

      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn
          :ripple="false"
          depressed
          color="#E1E1E9"
          class="btn"
          to="/construirpaz"
        >Construir paz</v-btn>
        <v-btn
          v-if="!isLoggedIn"
          :ripple="false"
          depressed
          color="#E1E1E9"
          class="btn"
          to="/sobrenosotros"
        >Sobre nosotros</v-btn>
        <v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/visualiza">Visualiza</v-btn>
        <v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/campañas">Campañas</v-btn>
        <v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/datosabiertos">Datos abiertos</v-btn>
      </v-toolbar-items>

      <v-btn v-if="isLoggedIn" class="ml-4 btn" :ripple="false" depressed text icon to="/perfil">
        <v-icon>fas fa-user</v-icon>
      </v-btn>
      <v-btn
        v-if="!isLoggedIn"
        :ripple="false"
        class="ma-2 login hidden-sm-and-down"
        tile
        color="#673AB7"
        dark
        to="/login"
      >Log in</v-btn>
      <v-btn
        v-if="isLoggedIn"
        :ripple="false"
        class="ma-2 login hidden-sm-and-down"
        tile
        color="#673AB7"
        dark
        @click="logout"
      >Salir</v-btn>
      <v-btn
        v-if="!isLoggedIn"
        :ripple="false"
        class="ma-2 login hidden-sm-and-down"
        tile
        color="#673AB7"
        dark
        to="/construirpaz"
      >Registrar</v-btn>

      <v-menu class="hidden-md-and-up">
      <template v-slot:activator="{ on }">
        <v-btn class="ma-2 btn hidden-md-and-up" :ripple="false" v-on="on" depressed icon>
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      
      <v-card color="#E1E1E9">
        <v-card-actions>
          <v-row justify="center">
            <v-col cols="12">
              <div>
                <v-btn
              :ripple="false"
              depressed
              color="#E1E1E9"
              class="btn"
              to="/construirpaz"
            >Construir paz</v-btn>
              </div>

             <div> <v-btn
          v-if="!isLoggedIn"
          :ripple="false"
          depressed
          color="#E1E1E9"
          class="btn"
          to="/sobrenosotros"
        >Sobre nosotros</v-btn> </div>
        <div><v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/visualiza">Visualiza</v-btn> </div>
        <div><v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/campañas">Campañas</v-btn></div>
        <div><v-btn :ripple="false" depressed color="#E1E1E9" class="btn" to="/datosabiertos">Datos abiertos</v-btn></div>

              <div>
                <v-btn
            v-if="!isLoggedIn"
            :ripple="false"
            class="ma-2 login"
            tile
            color="#673AB7"
            dark
            to="/login"
          >Log in</v-btn>
              </div>
              <div>
                <v-btn
            v-if="isLoggedIn"
            :ripple="false"
            class="ma-2 login"
            tile
            color="#673AB7"
            dark
            @click="logout"
          >Salir</v-btn>
              </div>
              <div>
                <v-btn
            v-if="!isLoggedIn"
            :ripple="false"
            class="ma-2 login"
            tile
            color="#673AB7"
            dark
            to="/construirpaz"
          >Registrar</v-btn>
              </div>
            </v-col>
          </v-row>
          
          
          
        </v-card-actions>
      </v-card>
    </v-menu>
    </v-toolbar>

    
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoggedIn: this.$store.getters.isLoggedIn
    };
  },
  methods: {
    logout() {
      this.$store
        .dispatch("logout")
        .then(resp => {
          this.$router.push("/home");
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Poppins|Roboto&display=swap");

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
  text-decoration: none !important;
  font-family: "Poppins";
  font-style: normal;
  font-weight: bold;
}
</style>