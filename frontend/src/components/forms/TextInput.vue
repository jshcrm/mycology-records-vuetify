<template>
  <div class="flex flex-col inline-block">
    <div class="relative">
      <slot name="icon"></slot>
      <div class="mb-[3px] inline-block">
        <input
          type="text"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          :class="{
            'ring-error-red': !isValid,
            'pl-[51px]': hasIcon,
            'pl-[24px]': !hasIcon,
          }"
          :placeholder="label"
          :value="modelValue"
          :disabled="disabled"
          @change="emitChange($event)"
        />
      </div>
    </div>
    <div v-show="!isValid" class="ml-[24px] inline-block">
      <span class="text-error-red caption line-height-[14.06px]"
        >*{{ errorMessage }}</span
      >
      <!-- {{ validationErrors.customerName }} -->
    </div>
  </div>
</template>

<script lang="ts">
export default {
  emits: ["update:modelValue"],
  props: {
    label: {
      type: String,
      required: true,
    },
    errorMessage: {
      type: String,
      default: "",
    },
    modelValue: {
      type: String,
      default: "",
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    hasIcon: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isValid() {
      return true;
    },
  },
  methods: {
    emitChange(e: Event) {
      const target = e.target as HTMLInputElement;
      this.$emit("update:modelValue", target?.value);
    }
  },
};
</script>
