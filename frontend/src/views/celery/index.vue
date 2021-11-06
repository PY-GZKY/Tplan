<template>
  <div class="app-container">
      <iframe :src="celery_api" frameborder="0" scrolling="auto" width="100%" height="950px" style="overflow-y:scroll;"></iframe>
  </div>
</template>

<script>
import {
  celery_,
} from "@/api/celery";

export default {
  name: "prometheus2",
  data() {
    return {
      celery_api: celery_,
    };
  },
}
</script>


<style>
</style>
