<script setup lang="ts">
import type { Media } from "@/interfaces/Media.js";
import dayjs from "dayjs";
import type { PropType } from "vue";
</script>

<template>
  <div class="flex">
    <div class="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
      <h5 class="text-gray-900 text-xl leading-tight font-medium mb-2">
        {{ media.name }}
      </h5>

      <p class="text-gray-700 text-base mb-4">
        <p><span class="font-bold">Method:</span> {{ media.inoculation_type }}</p>
        <p><span class="font-bold">Inoculated:</span> {{ $filters.dateFilter(media.inoculation_date) }}</p>
        <p v-if="media.full_colonization_date"><span class="font-bold">Colonized:</span> {{ fullColonizationDate }}</p>
        <p><span class="font-bold">Notes:</span> {{ media.notes }}</p>
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
    media: {
      type: Object as PropType<Media>,
      required: true,
    },
  },
  data() {
    const data = {};
    return data;
  },
  mounted() {},
  methods: {},
  computed: {
    inoculationDate(): String{
      return dayjs(this.media.inoculation_date).format("MM/DD/YYYY");
    },
    fullColonizationDate(): String{
      return dayjs(this.media.full_colonization_date).format("MM/DD/YYYY");
    },
  }
};
</script>
