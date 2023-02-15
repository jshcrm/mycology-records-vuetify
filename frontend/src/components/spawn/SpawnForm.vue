<script setup lang="ts">
import Button from "@/components/base/Button.vue";
import DateInput from "@/components/forms/DateInput.vue";
import TextInput from "@/components/forms/TextInput.vue";
import SpawnService from "@/networking/spawn.service.js";
import type { CreateSpawn } from "@/interfaces/Spawn";
</script>

<template>
  <div class="flex mb-4">
    <div class="w-[50%]">
      <TextInput
        class="pr-2"
        label="Strain"
        v-model="createForm.strain"
      ></TextInput>
    </div>
    <div class="w-[50%]">
      <TextInput
        label="Inoculation Type"
        v-model="createForm.inoculation_type"
      ></TextInput>
    </div>
  </div>

  <div class="flex mb-4">
    <div class="w-[50%]">
      <DateInput
        class="w-full pr-2"
        label="Inoculation Date"
        v-model="inoculationDate"
      ></DateInput>
    </div>
    <div class="w-[50%]">
      <DateInput
        label="Full Colonization Date"
        v-model="colonizationDate"
      ></DateInput>
    </div>
  </div>

  <div class="mb-4">
    <TextInput label="Notes" v-model="createForm.notes"></TextInput>
  </div>

  <div>
    <Button @click="submitForm">Submit</Button>
  </div>
</template>

<script lang="ts">
import dayjs from "dayjs";

export default {
  emits: ["spawnCreated"],
  data() {
    let createForm: CreateSpawn = {
      strain: "",
      inoculation_type: "",
      inoculation_date: "",
      full_colonization_date: "",
      notes: "",
    }

    const data = {
      inoculationDate: "",
      colonizationDate: "",
      createForm: createForm,
    };
    return data;
  },
  mounted() {},
  methods: {
    async submitForm() {
      this.createForm.inoculation_date = dayjs(
        this.inoculationDate
      ).toISOString();

      this.createForm.full_colonization_date = dayjs(
        this.colonizationDate
      ).toISOString();

      SpawnService.create(this.createForm).then(() => {
        this.$emit("spawnCreated");
      });
    },
  },
};
</script>
