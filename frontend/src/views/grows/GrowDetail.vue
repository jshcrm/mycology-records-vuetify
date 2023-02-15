<script setup lang="ts">
import dayjs from "dayjs";
import Button from "@/components/base/Button.vue";
import Modal from "@/components/base/Modal.vue";
import GrowCard from "@/components/grows/GrowCard.vue";
import GrowForm from "@/components/grows/GrowForm.vue";
import MediaCard from "@/components/media/MediaCard.vue";
import type { Grow } from "@/interfaces/Grow.js";
import GrowService from "@/networking/grow.service.js";
import type { PropType } from "vue";
import { ref } from "vue";
</script>

<template>
  <div v-if="grow">
    <GrowCard :grow="grow"></GrowCard>
    <apexchart
      v-if="chart.render"
      width="500"
      type="rangeBar"
      :options="options"
      :series="medias"
    ></apexchart>
  </div>
</template>

<script lang="ts">
interface chartRangeData {
  data: { x: String; y: number[] }[];
}

export default {
  data() {
    const data = {
      grow: null as Grow | null | undefined,
      chart: {
        render: false,
        options: "{}",
      },
      medias: Array<chartRangeData>(),
      options: {
        chart: {
          id: "vuechart-example",
        },
        plotOptions: {
          bar: {
            horizontal: true
          }
        },
        xaxis: {
          type: 'datetime'
        }
      },
    };
    return data;
  },
  mounted() {
    this.readGrow();
  },
  methods: {
    readGrow() {
      GrowService.read(this.$route.params.id).then((response) => {
        this.grow = response.data;

        for (let media of this.grow.medias) {
          this.medias.push({
            data: [
              {
                x: media.name,
                y: [
                  dayjs(media.inoculation_date).valueOf(),
                  media.full_colonization_date
                    ? dayjs(media.full_colonization_date).valueOf()
                    : dayjs(media.inoculation_date).valueOf(),
                ],
              },
            ],
          });
        }

        const first_media = this.grow.medias[0];
        const last_media = this.grow.medias[this.grow.medias.length - 1];

        this.chart.start = first_media.inoculation_date;

        this.chart.end = last_media.full_colonization_date
          ? last_media.full_colonization_date
          : last_media.inoculation_date;

        this.chart.render = true;
      });
    },
  },
};
</script>
