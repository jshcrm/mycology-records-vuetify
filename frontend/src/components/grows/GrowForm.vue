<script setup lang="ts">
import Button from "@/components/base/Button.vue";
import TextInput from "@/components/forms/TextInput.vue";
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
      <select v-model="createForm.strain_id" name="strain" id="strain">
        <option v-for="strain in strains" :key="strain.id" :value="strain.id">
          {{ strain.name }}
        </option>
      </select>
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
export default {
  emits: ["growCreated"],
  data() {
    let createForm: CreateGrow = { strain_id: 0, notes: "" };

    const data = {
      createForm: createForm,
      strains: Array<Strain>(),
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
      });
    },
  },
};
</script>
