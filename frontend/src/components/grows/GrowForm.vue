<script setup lang="ts">
import GrowService from "@/networking/grow.service.js";
import StrainService from "@/networking/strain.service";
import type { CreateGrow } from "@/interfaces/Grow";
import type { Strain } from "@/interfaces/Strain";
</script>

<template>
  <div class="flex mb-4">
    <div class="w-full">
      <div>
        <label for="strain">Strain</label>
      </div>
      <div v-if="selectStrains.length > 0">
        <v-select
          :items="selectStrains"
          v-model="createForm.strain_id"
          label="Strain"
        ></v-select>
      </div>
    </div>
  </div>

  <div class="mb-4">
    <v-text-field label="Notes" v-model="createForm.notes"></v-text-field>
  </div>

  <div>
    <v-btn color="primary" @click="submitForm">Submit</v-btn>
  </div>
</template>

<script lang="ts">
export default {
  emits: ["growCreated"],
  data() {
    let createForm: CreateGrow = { strain_id: "", notes: "" };

    const data = {
      createForm: createForm,
      strains: Array<Strain>(),
      selectStrains: Array<Record<string, string>>(),
    };
    return data;
  },
  mounted() {
    this.listStrains();
  },
  methods: {
    submitForm() {
      GrowService.create(this.createForm).then(() => {
        this.$emit("growCreated");
      });
    },
    listStrains() {
      StrainService.list().then((response) => {
        this.strains = response.data;
        console.log(this.strains);
        for (let strain of this.strains) {
          this.selectStrains.push({
            title: strain.name,
            value: String(strain.id),
          });
        }

        console.log(this.selectStrains);
      });
    },
  },
};
</script>
