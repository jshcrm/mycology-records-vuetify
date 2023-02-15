import { createApp } from "vue";
import { createPinia } from "pinia";
import vfmPlugin from "vue-final-modal";

import App from "./App.vue";
import router from "./router";

import VueSidebarMenu from "vue-sidebar-menu";
import "vue-sidebar-menu/dist/vue-sidebar-menu.css";
import dayjs from "dayjs";
import VueApexCharts from "vue3-apexcharts";

import "./assets/main.css";

const app = createApp(App);

app.config.globalProperties.$filters = {
  dateFilter(value: string) {
    return dayjs(value).format("MM/DD/YYYY");
  },
};

app
  .use(createPinia())
  .use(router)
  .use(vfmPlugin)
  .use(VueSidebarMenu)
  .use(VueApexCharts)
  .mount("#app");
