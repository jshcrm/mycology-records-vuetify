<template>
  <button
    type="button"
    class="border rounded-md px-4 py-2 m-2 transition duration-500 ease select-none focus:outline-none focus:shadow-outline"
    :class="getButtonTypeClasses"
    :style="{ width: getSize }"
  >
    <slot />
  </button>
</template>

<script lang="ts">
export default {
  props: {
    buttonType: {
      type: String,
      required: true,
      default: "primary",
    },
    size: {
      type: String,
      required: true,
      default: "md",
    },
  },
  computed: {
    getButtonTypeClasses() {
      const buttonTypes: { [buttonType: string]: Array<string> } = {
        primary: [
          "border-indigo-500",
          "bg-indigo-500",
          "text-white",
          "hover:bg-indigo-600",
        ],
        success: [
          "border-green-500",
          "bg-green-500",
          "text-white",
          "hover:bg-primary-white",
        ],
        error: [
          "border-red-500",
          "bg-red-500",
          "text-white",
          "hover:bg-red-600",
        ],
        warning: [
          "border-yellow-500",
          "bg-yellow-500",
          "text-white",
          "hover:bg-yellow-600",
        ],
        info: [
          "border-teal-500",
          "bg-teal-500",
          "text-white",
          "hover:bg-teal-600",
        ],
        dark: [
          "border-gray-700",
          "bg-gray-700",
          "text-white",
          "hover:bg-gray-800",
        ],
        light: [
          "border-gray-200",
          "bg-gray-200",
          "text-gray-700",
          "hover:bg-gray-300",
        ],
      };
      return buttonTypes[this.buttonType];
    },
    getSize() {
      const sizes: { [size: string]: string } = {
        sm: "60px",
        md: "100px",
        lg: "140px",
        xl: "160px",
      };
      return sizes[this.size];
    },
  },
  methods: {},
};
</script>
