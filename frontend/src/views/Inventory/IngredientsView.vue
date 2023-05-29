<script setup lang="ts">
import Modal from "@/components/base/Modal.vue";
// import IngredientForm from "@/components/ingredients/IngredientForm.vue";
import type { Ingredient } from "@/interfaces/Ingredient.js";
// import IngredientCard from "@/components/ingredients/IngredientCard.vue";
import IngredientService from "@/networking/ingredient.service.js";
</script>

<template>
  <div class="w-full text-right">
    <v-btn color="secondary" @click="showCreateModal = true">Create Ingredient</v-btn>
  </div>

  <div class="flex">
    <div class="mr-4" v-for="ingredient in ingredients" :key="ingredient.name">
      <IngredientCard :ingredient="ingredient"></IngredientCard>
    </div>
  </div>

  <Modal v-model="showCreateModal">
    <h2 name="title">Create Ingredient</h2>
    <IngredientForm @ingredientCreated="closeCreateForm"></IngredientForm>
  </Modal>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      ingredients: Array<Ingredient>(),
      showCreateModal: false,
    };
    return data;
  },
  mounted() {
    console.log("mounting ingredients");
    console.log(IngredientService);
  },
  methods: {
    getIngredients() {
      IngredientService.list().then((response) => {
        this.ingredients = response.data;
      });
    },
    closeCreateForm() {
      this.showCreateModal = false;
      this.getIngredients();
    }
  },
};
</script>
