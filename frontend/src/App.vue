<script setup lang="ts">
import { RouterView } from "vue-router";
import NavBar from "./components/base/NavBar.vue";
</script>

<template>
  <v-app>
    <v-main>
      <NavBar></NavBar>

      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped></style>
