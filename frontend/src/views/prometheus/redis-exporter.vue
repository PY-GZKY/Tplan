<template>
  <div class="app-container">
    <iframe
      :src="redis_exporter_api"
      frameborder="0" scrolling="auto" width="100%" height="950px" style="overflow-y:scroll;"></iframe>
  </div>
</template>

<script>
import {
  redis_exporter,
} from "@/api/prometheus2.0";

export default {
  name: "xWz",
  data() {
    return {
      redis_exporter_api: redis_exporter,
    };
  },
}
</script>


<style>
</style>
