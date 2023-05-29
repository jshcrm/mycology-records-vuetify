<script setup lang="ts">
import type { Media } from "@/interfaces/Media.js";
import MediaService from "@/networking/media.service";
import dayjs from "dayjs";
import type { PropType } from "vue";
</script>

<template>
  <div class="d-flex">
    <div class="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
      <v-card>
        <v-card-title>
          {{ media.name }}
        </v-card-title>

        <v-card-text>
          <p class="text-gray-700 text-base mb-4">
            <p><span class="font-weight-bold">Method:</span> {{ media.inoculation_type }}</p>
            <p><span class="font-weight-bold">Inoculated:</span> {{ $filters.dateFilter(media.inoculation_date) }}</p>
            <p v-if="media.full_colonization_date"><span class="font-weight-bold">Colonized:</span> {{ fullColonizationDate }}</p>
            <p v-if="media.notes"><span class="font-weight-bold">Notes:</span> {{ media.notes }}</p>
          </p>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn @click=" deleteMedia"><v-icon class="text-red" icon="mdi-trash-can"></v-icon></v-btn>
        </v-card-actions>
      </v-card>
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
  methods: {
    deleteMedia() {
      MediaService.delete(String(this.media.id))
    }
  },
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
