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

import "vuetify/styles";
import { createVuetify } from "vuetify";
import { aliases, mdi } from "vuetify/iconsets/mdi";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi",
    aliases,
    sets: {
      mdi,
    },
  },
});

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
  .use(vuetify)
  .use(VueSidebarMenu)
  .use(VueApexCharts)
  .mount("#app");
