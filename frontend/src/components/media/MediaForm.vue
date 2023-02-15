<script setup lang="ts">
import Button from "@/components/base/Button.vue";
import DateInput from "../forms/DateInput.vue";
import TextInput from "@/components/forms/TextInput.vue";
import type { CreateMedia } from "@/interfaces/Media";
import MediaService from "@/networking/media.service.js";
</script>

<template>
  <div class="flex mb-4 w-full">
    <div class="w-[50%]">
      <TextInput
        class="pr-2"
        label="Name"
        v-model="createForm.name"
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
  emits: ["mediaCreated"],
  props: {
    growID: {
      type: Number,
      required: true,
    },
  },
  data() {
    let createForm: CreateMedia = {
      grow_id: this.growID,
      name: "",
      inoculation_type: "",
      inoculation_date: "",
      full_colonization_date: "",
      notes: "",
    };

    const data = {
      inoculationDate: "",
      colonizationDate: "",
      createForm: createForm,
    };

    console.log(createForm);
    return data;
  },
  mounted() {},
  methods: {
    async submitForm() {
      this.createForm.inoculation_date = dayjs(
        this.inoculationDate
      ).toISOString();

      if (this.createForm.full_colonization_date) {
        this.createForm.full_colonization_date = dayjs(
          this.colonizationDate
        ).toISOString();
      } else {
        delete this.createForm.full_colonization_date;
      }

      MediaService.create(this.createForm).then(() => {
        this.$emit("mediaCreated");
      });
    },
  },
};
</script>
