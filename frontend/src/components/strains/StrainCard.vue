<script setup lang="ts">
import type { Strain } from "@/interfaces/Strain.js";
import type { PropType } from "vue";
</script>

<template>
  <div class="d-flex">
    <v-card>
      <v-card-title> {{ strain.name }} ({{ strain.short_name }}) </v-card-title>

      <v-card-text>
        <span class="font-bold">Notes:</span> {{ strain.notes }}
      </v-card-text>
    </v-card>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    strain: {
      type: Object as PropType<Strain>,
      required: true,
    },
  },
  data() {
    const data = {};
    return data;
  },
  mounted() {},
  methods: {},
};
</script>
