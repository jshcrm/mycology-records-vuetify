<script setup lang="ts">
import { RouterView } from "vue-router";
import NavBar from "./components/base/NavBar.vue";
import SideBar from "./components/base/SideBar.vue";
</script>

<template>
  <div class="w-[290px]">
    <SideBar></SideBar>
  </div>

  <div class="ml-[290px]">
    <NavBar></NavBar>
    <div class="mt-[20px]">
      <RouterView />
    </div>
  </div>
</template>

<style scoped></style>
