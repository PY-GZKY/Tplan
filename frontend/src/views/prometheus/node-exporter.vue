<template>
  <div class="app-container">
      <iframe :src="node_exporter_api" frameborder="0" scrolling="auto" width="100%" height="950px" style="overflow-y:scroll;"></iframe>
  </div>
</template>

<script>
import {
  node_exporter,
} from "@/api/prometheus2.0";

export default {
  name: "prometheus2",
  data() {
    return {
      node_exporter_api: node_exporter,
    };
  },
}
</script>

<style>
</style>
