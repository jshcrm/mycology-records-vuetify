<script setup lang="ts">
import Button from "@/components/base/Button.vue";
import Modal from "@/components/base/Modal.vue";
import StrainForm from "@/components/strains/StrainForm.vue";
import type { Strain } from "@/interfaces/Strain.js";
import StrainCard from "@/components/strains/StrainCard.vue";
import StrainService from "@/networking/strain.service.js";
</script>

<template>
  <div class="w-full text-right">
    <Button size="xl " @click="showCreateModal = true">Create Strain</Button>
  </div>

  <div class="flex">
    <div class="mr-4" v-for="strain in strains" :key="strain.name">
      <StrainCard :strain="strain"></StrainCard>
    </div>
  </div>

  <Modal v-model="showCreateModal">
    <h2 name="title">Create Strain</h2>
    <StrainForm @strainCreated="closeCreateForm"></StrainForm>
  </Modal>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      strains: Array<Strain>(),
      showCreateModal: false,
    };
    return data;
  },
  mounted() {
    this.getStrains();
  },
  methods: {
    getStrains() {
      StrainService.list().then((response) => {
        this.strains = response.data;
      });
    },
    closeCreateForm() {
      this.showCreateModal = false;
      this.getStrains();
    }
  },
};
</script>
