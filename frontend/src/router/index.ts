import { createRouter, createWebHistory } from "vue-router";
import GrowsView from "@/views/grows/GrowsView.vue";
import GrowDetail from "@/views/grows/GrowDetail.vue";
import SpawnView from "@/views/SpawnView.vue";
import StrainsView from "@/views/Inventory/StrainsView.vue";
import IngredientsView from "@/views/Inventory/IngredientsView.vue";
import MediaView from "@/views/Inventory/MediaView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "grows",
      component: GrowsView,
    },
    {
      path: "/grow/:id",
      name: "grows-detail",
      component: GrowDetail,
    },
    {
      path: "/spawns",
      name: "gpawns",
      component: SpawnView,
    },
    {
      path: "/strains",
      name: "strains",
      component: StrainsView,
    },
    {
      path: "/ingredients",
      name: "ingredients",
      component: IngredientsView,
    },
    {
      path: "/media",
      name: "media",
      component: MediaView,
    },
  ],
});

export default router;
