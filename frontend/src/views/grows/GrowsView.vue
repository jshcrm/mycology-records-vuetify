<script setup lang="ts">
import Button from "@/components/base/Button.vue";
import Modal from "@/components/base/Modal.vue";
import GrowCard from "@/components/grows/GrowCard.vue";
import GrowForm from "@/components/grows/GrowForm.vue";
import type { Grow } from "@/interfaces/Grow.js";
import GrowService from "@/networking/grow.service.js";
</script>

<template>
  <div class="w-full text-right">
    <Button size="xl " @click="showCreateModal = true">Create Grow</Button>
  </div>

  <div class="flex">
    <div class="mr-4" v-for="grow in grows" :key="grow.id">
      <GrowCard @mediaCreated="listGrows" :grow="grow"></GrowCard>
    </div>
  </div>

  <Modal v-model="showCreateModal">
    <h2 name="title">Create Grow</h2>
    <GrowForm @growCreated="closeGrowForm"></GrowForm>
  </Modal>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      grows: Array<Grow>(),
      showCreateModal: false,
    };
    return data;
  },
  mounted() {
    this.listGrows();
  },
  methods: {
    listGrows() {
      GrowService.list().then((response) => {
        this.grows = response.data;
      });
    },
    closeGrowForm() {
      this.showCreateModal = false;
      this.listGrows();
    },
  },
};
</script>
