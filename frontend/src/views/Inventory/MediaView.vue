<script setup lang="ts">
import Modal from "@/components/base/Modal.vue";
import MediaCard from "@/components/media/MediaCard.vue";
import MediaForm from "@/components/media/MediaForm.vue";
import type { Media } from "@/interfaces/Media.js";
import MediaService from "@/networking/media.service.js";
</script>

<template>
  <div class="w-full text-right">
    <v-btn color="secondary" @click="showCreateModal = true">Create Media</v-btn>
  </div>

  <div class="flex">
    <div class="mr-4" v-for="media in medias" :key="media.name">
      <MediaCard :media="media"></MediaCard>
    </div>
  </div>

  <Modal v-model="showCreateModal">
    <h2 name="title">Create Media</h2>
    <MediaForm @mediaCreated="closeCreateForm"></MediaForm>
  </Modal>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      medias: Array<Media>(),
      showCreateModal: false,
    };
    return data;
  },
  mounted() {
    this.getMedias();
  },
  methods: {
    getMedias() {
      MediaService.list().then((response) => {
        this.medias = response.data;
      });
    },
    closeCreateForm() {
      this.showCreateModal = false;
      this.getMedias();
    },
  },
};
</script>
