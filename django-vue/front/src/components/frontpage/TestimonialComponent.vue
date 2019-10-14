<template>
  <div>
    <h3 align="center">Qué opinan</h3>
    <h2 align="center">Un proyecto que dá de que hablar</h2>
    <v-container>
      <v-row justify="center">
        <v-col v-for="n in 3" :key="n" class="d-flex child-flex" cols="3">
          <v-card class="mx-auto" max-width="400">
            
            <v-card-text class="headline font-weight-bold">
              <p class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore. </p>
            </v-card-text>

            <v-card-actions>
              <v-row align="center" justify="end">
                <h4>Sandra Niño - </h4>
                <h5 class="mr-2">Antropóloga </h5>
              </v-row>
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
  font-size: 24px;
  line-height: 36px;
  color: #0c186d;
}

h4 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 36px;
  text-align: justify;

  color: #0c186d;
}

h2 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: 48px;
  line-height: 72px;
  color: #000000;
}

h5 {
  font-family: Poppins;
  font-style: normal;
  font-weight: bold;
  font-size: 20px;
  line-height: 72px;
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