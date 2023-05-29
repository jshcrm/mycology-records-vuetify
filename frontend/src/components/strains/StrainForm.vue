<script setup lang="ts">
import TextInput from "@/components/forms/TextInput.vue";
import StrainService from "@/networking/strain.service.js";
import type { CreateStrain } from "@/interfaces/Strain";
</script>

<template>
  <div class="flex mb-4">
    <div class="w-[50%]">
      <TextInput
        class="pr-2"
        label="Name"
        v-model="createForm.name"
      ></TextInput>
    </div>
    <div class="w-[50%]">
      <TextInput
        label="Short Name (3 max)"
        v-model="createForm.short_name"
      ></TextInput>
    </div>
  </div>

  <div class="mb-4">
    <TextInput label="Notes" v-model="createForm.notes"></TextInput>
  </div>

  <div>
    <v-btn color="secondary" @click="submitForm">Submit</v-btn>
  </div>
</template>

<script lang="ts">
export default {
  emits: ["strainCreated"],
  data() {
    let createForm: CreateStrain = {
      name: "",
      short_name: "",
      notes: "",
    };

    const data = {
      createForm: createForm,
    };
    return data;
  },
  mounted() {},
  methods: {
    async submitForm() {
      StrainService.create(this.createForm).then(() => {
        this.$emit("strainCreated");
      });
    },
  },
};
</script>
