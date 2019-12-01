<template>
  <div>
    <h3 align="center">Qué opinan</h3>
    <h2 align="center">Un proyecto que dá de que hablar</h2>
    <v-container>
      <v-row justify="center">
        <v-col v-for="n in 3" :key="n" cols="10" sm="10" md="4">
          <v-card class="mx-auto" max-width="400">
            <v-card-text class="headline font-weight-bold">
              <p
                class="description"
              >Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.</p>
            </v-card-text>

            <v-card-actions>
              <v-list-item class="grow">
                <v-list-item-avatar color="grey darken-3">
                  <v-img
                    class="elevation-6"
                    :src="require('@/assets/objective.png')"
                  ></v-img>
                </v-list-item-avatar>

                <!--<v-list-item-content>
                  <v-list-item-title><h4>Sandra Niño -</h4>
                  <h5 class="mr-2">Antropóloga</h5></v-list-item-title>
                </v-list-item-content>-->
                <v-row align="center" justify="end">
                  <h4>22 años -</h4>
                  <h5 class="mr-2">Cali, Comuna 19</h5>
                </v-row>
              </v-list-item>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
h3 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: calc(18px + (24 - 18) * ((100vw - 300px) / (1600 - 300)));
  color: #0c186d;
}

h4 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1600 - 300)));
  text-align: justify;

  color: #0c186d;
}

h2 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: calc(24px + (48 - 24) * ((100vw - 300px) / (1600 - 300)));
  color: #000000;
}

h5 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: calc(16px + (20 - 16) * ((100vw - 300px) / (1600 - 300)));
  color: #000000;
}

p {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 21px;

  color: #000000;
}
</style>