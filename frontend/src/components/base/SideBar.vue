<template>
  <sidebar-menu :menu="menu" />
</template>

<script lang="ts">
export default {
  data() {
    const data = {
      menu: [
        {
          header: "Main Navigation",
          hiddenOnCollapse: true,
        },
        {
          href: "/",
          title: "Grows",
        },
        {
          href: "/spawns",
          title: "Spawns",
        },
        {
          href: "/strains",
          title: "Strains",
        },
        {
          href: "/ingredients",
          title: "Ingredients",
        },
        {
          href: "/media",
          title: "Media",
        },
      ],
    };
    return data;
  },
};
</script>
