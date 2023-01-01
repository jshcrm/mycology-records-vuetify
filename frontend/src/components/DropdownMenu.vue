<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div>
    <button
      id="dropdownDefault"
      @click="dropdownActive = !dropdownActive"
      class="font-medium text-sm px-4 py-2.5 text-right inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      type="button"
    >
      <svg viewBox="0 0 100 80" width="20" height="20">
        <rect width="100" height="20"></rect>
        <rect y="30" width="100" height="20"></rect>
        <rect y="60" width="100" height="20"></rect>
      </svg>
    </button>
    <!-- Dropdown menu -->
    <div
      id="dropdown"
      :class="{ hidden: !dropdownActive }"
      class="z-50 fixed right-[70px] w-40 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700"
    >
      <ul
        class="py-1 text-sm text-gray-700 dark:text-gray-200"
        aria-labelledby="dropdownDefault"
      >
        <li @click="dropdownActive = false">
          <RouterLink
            class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
            to="/"
            >Item</RouterLink
          >
        </li>
      </ul>
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
  methods: {
    toggleDropdown(e: Event) {
      this.dropdownActive = !this.dropdownActive;
    },
    close(e: Event) {
      if (!this.$el.contains(e.target)) {
        this.dropdownActive = false;
      }
    },
  },
  mounted() {
    document.addEventListener("click", this.close);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.close);
  },
};
</script>
