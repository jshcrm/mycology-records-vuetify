<template>
  <button
    type="button"
    class="group relative h-12 w-48 overflow-hidden rounded-lg bg-white text-lg shadow"
    :class="getButtonTypeClasses"
    :style="{ width: getSize }"
  >
    <div
      class="absolute inset-0 w-3 bg-amber-400 transition-all duration-[250ms] ease-out group-hover:w-full"
    ></div>
    <span class="relative text-black group-hover:text-white"><slot /></span>
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
          "bg-primary-orange",
          "bg-primary-white",
          "hover:bg-dark-orange",
        ],
        secondary: [
          "bg-light-green",
          "text-dark-green",
          "hover:bg-dark-green",
          "hover:bg-primary-white",
        ],
        tertiary: ["bg-background-gray", "hover:bg-div-gray"],
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
