<template>
  <div class="app-container">
      <iframe :src="prometheus2_api" frameborder="0" scrolling="auto" width="100%" height="950px" style="overflow-y:scroll;"></iframe>
  </div>
</template>

<script>
import {
  prometheus2,
} from "@/api/prometheus2.0";

export default {
  name: "prometheus2",
  data() {
    return {
      prometheus2_api: prometheus2,
    };
  },
}
</script>


<style>
</style>
