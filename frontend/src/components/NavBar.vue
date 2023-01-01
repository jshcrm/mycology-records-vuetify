<script setup lang="ts">
import DropdownMenu from "./DropdownMenu.vue";
</script>

<template>
  <div class="flex border-b w-full h-[75px] p-[20px]">
    <div class="flex-1 my-auto">Logo</div>
    <div class="flex-1"></div>
    <div class="flex-1 my-auto">
      <div class="float-right">
        <DropdownMenu></DropdownMenu>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      dropdownActive: false,
    };
    return data;
  },
  computed: {},
  methods: {},
};
</script>
