<template>
  <div class="app-container">
      <iframe :src="mysql_exporter_api" frameborder="0" scrolling="auto" width="100%" height="950px" style="overflow-y:scroll;"></iframe>
  </div>
</template>

<script>
import {
  mysql_exporter,
} from "@/api/prometheus2.0";

export default {
  name: "prometheus2",
  data() {
    return {
      mysql_exporter_api: mysql_exporter,
    };
  },
}
</script>

<style>
</style>
