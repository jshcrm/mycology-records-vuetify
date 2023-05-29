<script setup lang="ts"></script>

<template>
  <v-app-bar :elevation="1">
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-app-bar-title>Mycology Records</v-app-bar-title>
  </v-app-bar>

  <v-navigation-drawer v-model="drawer" temporary>
    <v-list v-for="navItem in navItems" :key="navItem.title">
      <v-list-item :to="navItem.to">{{ navItem.title }}</v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      drawer: false,
      navItems: [
        {
          title: "Grows",
          to: "/",
        },
        {
          title: "Strains",
          to: "/strains",
        },
        {
          title: "Ingredients",
          to: "/ingredients",
        },
        {
          title: "Media",
          to: "/media",
        },
      ]
    };
    return data;
  },
  computed: {},
  methods: {},
};
</script>
