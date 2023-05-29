<script setup lang="ts">
import type { Grow } from "@/interfaces/Grow.js";
import type { PropType } from "vue";
import Modal from "@/components/base/Modal.vue";
import MediaCard from "@/components/media/MediaCard.vue";
import MediaForm from "@/components/media/MediaForm.vue";
</script>

<template>
  <div class="d-flex">
    <v-card>
      <v-card-title>
        <RouterLink
          :to="{ name: 'grows-detail', params: { id: grow.id } }"
          class="flex items-center"
          >{{ grow.strain.name }}</RouterLink
        >
      </v-card-title>

      <v-card-text>
        <p class="text-gray-700 text-base mb-4">
          <span class="font-bold">Notes:</span> {{ grow.notes }}
        </p>

        <div class="d-flex">
          <div class="mr-4" v-for="media in grow.medias" :key="media.id">
            <MediaCard :media="media"></MediaCard>
          </div>
        </div>
      </v-card-text>

      <v-card-actions>
        <v-btn color="primary" @click="showMediaCreateModal = true"
          >Add Media</v-btn
        >
      </v-card-actions>
    </v-card>
  </div>
  <Modal v-model="showMediaCreateModal">
    <h2 name="title">Create Media</h2>
    <MediaForm :growID="grow.id" @mediaCreated="closeMediaForm"></MediaForm>
  </Modal>
</template>

<script lang="ts">
export default {
  emits: ["mediaCreated"],
  props: {
    grow: {
      type: Object as PropType<Grow>,
      required: true,
    },
  },
  data() {
    const data = { showMediaCreateModal: false };
    return data;
  },
  mounted() {},
  methods: {
    closeMediaForm() {
      this.showMediaCreateModal = false;
      this.$emit("mediaCreated");
    },
  },
};
</script>
