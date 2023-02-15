<script setup lang="ts">
import type { Strain } from "@/interfaces/Strain.js";
import type { PropType } from "vue";
</script>

<template>
  <div class="flex">
    <div class="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
      <h5 class="text-gray-900 text-xl leading-tight font-medium mb-2">
        {{ strain.name }} ({{ strain.short_name}})
      </h5>

      <p class="text-gray-700 text-base mb-4">
        <span class="font-bold">Notes:</span> {{ strain.notes }}
      </p>

      <button
        type="button"
        class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
      >
        Button
      </button>
    </div>
  </div>
  <div></div>
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
