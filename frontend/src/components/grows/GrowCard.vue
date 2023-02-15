<script setup lang="ts">
import type { Grow } from "@/interfaces/Grow.js";
import type { PropType } from "vue";
import Button from "../base/Button.vue";
import Modal from "@/components/base/Modal.vue";
import MediaCard from "@/components/media/MediaCard.vue";
import MediaForm from "@/components/media/MediaForm.vue";
</script>

<template>
  <div class="flex w-full">
    <div class="block p-6 rounded-lg shadow-lg bg-white">
      <h5 class="inline text-gray-900 text-xl leading-tight font-medium mb-2">
        <RouterLink
          :to="{ name: 'grows-detail', params: { id: grow.id } }"
          class="flex items-center"
          >{{ grow.strain.name }}</RouterLink
        >
      </h5>

      <Button class="float-right" size="lg" @click="showMediaCreateModal = true"
        >Add Media</Button
      >

      <p class="text-gray-700 text-base mb-4">
        <span class="font-bold">Notes:</span> {{ grow.notes }}
      </p>

      <div class="flex">
        <div class="mr-4" v-for="media in grow.medias" :key="media.id">
          <MediaCard :media="media"></MediaCard>
        </div>
      </div>
    </div>
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
