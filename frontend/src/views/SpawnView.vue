<script setup lang="ts">
import Button from "@/components/base/Button.vue";
import Modal from "@/components/base/Modal.vue";
import SpawnCard from "@/components/spawn/SpawnCard.vue";
import SpawnForm from "@/components/spawn/SpawnForm.vue";
import type { Spawn } from "@/interfaces/Spawn.js";
import SpawnService from "@/networking/spawn.service.js";
</script>

<template>
  <div class="w-full text-right">
    <Button size="xl " @click="showCreateSpawnModal = true"
      >Create Spawn</Button
    >
  </div>

  <div class="flex">
    <div class="mr-4" v-for="spawn in spawns" :key="spawn.strain">
      <SpawnCard :spawn="spawn"></SpawnCard>
    </div>
  </div>

  <Modal v-model="showCreateSpawnModal">
    <h2 name="title">Create Spawn</h2>
    <SpawnForm @spawnCreated="closeSpawnForm"></SpawnForm>
  </Modal>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      spawns: Array<Spawn>(),
      showCreateSpawnModal: false,
    };
    return data;
  },
  mounted() {
    this.getSpawn();
  },
  methods: {
    getSpawn() {
      SpawnService.list().then((response) => {
        this.spawns = response.data;
      });
    },
    closeSpawnForm() {
      this.showCreateSpawnModal = false;
      this.getSpawn();
    }
  },
};
</script>
